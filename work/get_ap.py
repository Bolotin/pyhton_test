"""
Пока список девайсов будет храниться тут в виде словаря словарей devices.
Ключ первого уровня - WLC_NAME, указывает на словарь с ключами address и vendor ('сisco' или 'huawei')
Потом стоит доделать его получение из внешнего файла.
Проверка доступности узлов реализована через ping (предполагаем что ICMP открыт всегда).
Если устройство не пингуется - обращаться к нему по ssh не пытаемся, Просто выводим диагностическое сообщение.
Результаты вывода с каждого контроллера хранятся в отдельном файле, <WLC name>.txt
После получения уже эти результаты парсятся (MAC адрес Huawei надо привести к виду XX:XX:XX:XX:XX:XX).
И сохраняются в отдельный репорт AP_INFO_<day>_<month>_<ear>.CSV
Репорт должен содержать столбцы AP_MAC, AP_NAME, AP_ADDRESS. Позже надо доделать AP_GROUP, AP_LOCATION, WLC_NAME
"""
from netmiko import ConnectHandler
from pprint import pprint
from datetime import datetime
import subprocess
import getpass

def get_ap_cisco(ip, user, password, filename):
    """
    Функция для получения информации о точках с контроллера Cisco, ожидает адрес, логи, пароль и имя файла куда записать полученную информацию
    """
    COMMAND = 'show ap summary'
    DEVICE_PARAMS = {'device_type':'cisco_wlc', 'ip': ip, 'username': user, 'password': password, 'banner_timeout':16}
    with ConnectHandler(**DEVICE_PARAMS) as connection:
        result = connection.send_COMMAND(COMMAND)
        with open(filename,'w') as file:
            file.write(result)

def get_ap_huawei(ip, user, password, filename):
    """
    Функция для получения информации о точках с контроллера Huawei, ожидает адрес, логи, пароль и имя файла куда записать полученную информацию
    """
    COMMAND = 'display ap all'
    DEVICE_PARAMS = {'device_type':'huawei', 'ip': ip, 'username': user, 'password': password, 'banner_timeout':16}
    with ConnectHandler(**DEVICE_PARAMS) as connection:
        result = connection.send_COMMAND(COMMAND)
        with open(filename,'w') as file:
            file.write(result)

def check_device(ip):
    """
    Функция проверки доступности устройства. Ожидает адрес. Возвращает True если девая доступен и False если не доступен
    """
    check = subprocess.run('ping -c 3 {}'.format(ip), shell = True, stdout = subprocess.DEVNULL)
    if check.returncode == 0:
        return True
    else:
        return False

def parse_ap_cisco(src_filename, dst_filename):
    with open(src_filename, 'r') as src, open(dst_filename,'w') as dst:
        for line in src:
            regex = '^(?P<AP_NAME>\S+).*(?P<AP_MAC>(\w\w:){5}\w\w).*\s+(?P<AP_ADDRESS>(\d{1,3}\.){3}\d{1,3})'
            search = re.search(regex, line)
            if search:
                AP_MAC, AP_NAME, AP_ADDRESS = *search.group('AP_MAC','AP_NAME','AP_ADDRESS')
                dst.write('{}, {}, {} \n'.format(AP_MAC, AP_NAME, AP_ADDRESS))

def parse_ap_huawei(src_filename, dst_filename):
    with open(src_filename, 'r') as src, open(dst_filename,'w') as dst:
        for line in src:
            regex = '^(?P<AP_ID>\d+\s+(?P<AP_MAC>\w{4}-\w{4}-\w{4})\s+(?P<AP_NAME>\S+)\s+(?P<AP_GROUP>\S+)\s+(?P<AP_ADDRESS>(\d{1,3}\.){3}\d{1,3}))'
            search = re.search(regex, line)
            if search:
                AP_MAC, AP_NAME, AP_ADDRESS = *search.group('AP_MAC','AP_NAME','AP_ADDRESS')
                dst.write('{}, {}, {} \n'.format(convert_huawei_mac_to_cisco(AP_MAC), AP_NAME, AP_ADDRESS))

def convert_huawei_mac_to_cisco(huawei_mac):
    cisco_mac = '{}:{}:{}:{}:{}:{}'.format(*re.search('(\w\w)(\w\w)-(\w\w)(\w\w)-(\w\w)(\w\w)',huawei_mac).groups())
    return cisco_mac

if __name__ == '__main__':
    #Пока список контроллеров задаем локально тут, но в дальнейшем необходима внешняя БД
    devices = dict(CWC001 = dict(address = '10.47.208.1', vendor = 'cisco'),
                   CWC003 = dict(address = '10.47.208.17', vendor = 'cisco'),
                   HWC001 = dict(address = '10.47.208.65', vendor = 'huawei'))

    user = input('User: ')
    password = getpass.getpass('Password: ')
    for device in devices:
        filename = './tmp/{}_{}.txt'.format(device,datetime.today().strftime('%d_%m_%Y'))
        parsed_filename = './tmp/{}_{}_parsed.txt'.format(device,datetime.today().strftime('%d_%m_%Y'))
        ip = devices[device]['address']
        if not check_device(ip):
            print('{} in unavailable. Sorry.'.format(device))
            continue
        if devices[device]['vendor'] == 'cisco':
            print('Start connection with {}'.format(device))
            get_ap_cisco(ip, user, password, filename)
            print('Connection with {} closed. Infortainon in {}'.format(device, filename))
            print('Start parsing information in file {}'.format(filename))
            parse_ap_cisco(filename, parsed_filename)
            print('Finished parsing. Parsed information in {}'.format(parsed_filename))
        elif devices[device]['vendor'] == 'huawei':
            print('Start connection with {}'.format(device))
            get_ap_huawei(ip, user, password, filename)
            print('Connection with {} closed. Infortainon in {}'.format(device, filename))
            print('Start parsing information in file {}'.format(filename))
            parse_ap_huawei(filename, parsed_filename)
            print('Finished parsing. Parsed information in {}'.format(parsed_filename))
