"""
Пока список девайсов будет храниться тут в виде словаря словарей devices.
Ключ первого уровня - WLC_NAME, указывает на словарь с ключами address и vendor ('сisco' или 'huawei')
Потом стоит доделать его получение из внешнего файла.
Проверка доступности узлов реализована через ping (предполагаем что ICMP открыт всегда).
Если устройство не пингуется - обращаться к нему по ssh не пытаемся, Просто выводим диагностическое сообщение.
Результаты вывода с каждого контроллера хранятся в отдельном файле, <WLC name>.txt
После получения уже эти результаты парсятся (MAC адрес Huawei надо привести к виду XX:XX:XX:XX:XX:XX).
И сохраняются в отдельный репорт AP_INFO_<day>_<month>_<ear>.CSV
Репорт должен содержать столбцы AP_NAME, AP_MAC, AP_ADDRESS, AP_GROUP, WLC_NAME
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


if __name__ == '__main__':

    devices = dict(CWC001 = dict(address = '10.47.208.1', vendor = 'cisco'),
                   CWC003 = dict(address = '10.47.208.17', vendor = 'cisco'),
                   HWC001 = dict(address = '10.47.208.65', vendor = 'huawei'))

    user = input('User: ')
    password = getpass.getpass('Password: ')
    for device in devices:
        filename = '{}-{}.txt'.format(device,datetime.today().strftime('%d-%m-%Y'))
        ip = devices[device][address]
        if not check_device(ip):
            print('Device {} in unavailable =('.format(device))
            continue
