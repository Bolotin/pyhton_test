"""
Скрипт предназначен для составления отчёта по физическому расположению точек доступа.
Опрашиваются контроллеры Cisco и Huawei и составляется отчёт в формате .xlsx
Отчёт содержит - APMAC, CalledStationID, APName, APAddress, APLocation  (для Huawei CalledStationID - совпадает с APMAC, для Cisco - 'Это ')
Список контроллеров пока хранится в виде словаря прямо в скрипте. На будущее - сделать отдельный YAML файл
Для Huawei информация собирается функцией get_ap_huawei, которая использует одну команду и возвращает данные в виде словаря (ключ - MAC, данные в списке)
Для Cisco информация собирается функцией get_ap_cisco, которая использет две команды и возвращает данные в виде словаря (ключ - MAC, данные в списке)
Основной скрипт берет эти данные, добавляет данные по APLocation из предыдущего репорта и записывает в xlsx
"""

from netmiko import ConnectHandler
from datetime import datetime
import subprocess, getpass, re, csv, openpyxl
from pprint import pprint

def check_device_linux(ip):
    """
    Функция проверки доступности устройства. Ожидает адрес в формате строки. Возвращает True если девая доступен и False если не доступен.
    Проверялась только на linux
    """
    check = subprocess.run('ping -c 3 {}'.format(ip), shell = True, stdout = subprocess.DEVNULL)
    if check.returncode == 0:
        return True
    else:
        return False

def convert_huawei_mac_to_cisco(huawei_mac):
    """
    Функция получает MAC в формате Huawei и возвращает в формате Cisco
    """
    cisco_mac = '{}:{}:{}:{}:{}:{}'.format(*re.search('.*(\w\w)(\w\w)-(\w\w)(\w\w)-(\w\w)(\w\w).*',huawei_mac.strip()).groups())
    return cisco_mac

def get_ap_cisco(ip, user, password):
    """
    Функция для получения информации о точках с контроллера Cisco, ожидает адрес, логин, пароль. Возвращает словарь со списками данных
    """
    result = {}
    COMMAND = 'show ap summary'
    REGEX = '^(?P<APName>\S+).*(?P<APMAC>(\w\w:){5}\w\w).*\s+(?P<APAddress>(\d{1,3}\.){3}\d{1,3})'
    DeviceParams = {'device_type':'cisco_wlc', 'ip': ip, 'username': user, 'password': password, 'banner_timeout':16}
    with ConnectHandler(**DeviceParams) as connection:
        output = connection.send_command(COMMAND)
    for line in output.split('\n'):
        parse = re.search(REGEX, line)
        if parse:
            APMAC, APName, APAddress = parse.group('APMAC'), parse.group('APName'), parse.group('APAddress')
            result[APMAC] = [APName, APAddress]
    COMMAND = 'show ap join stats summary all'
    REGEX = '^(?P<CalledStationID>(\w\w:){5}\w\w)\s+(?P<APMAC>(\w\w:){5}\w\w)'
    with ConnectHandler(**DeviceParams) as connection:
        output = connection.send_command(COMMAND)
    for line in output.split('\n'):
        parse = re.search(REGEX, line)
        if parse:
            APMAC, CalledStationID = parse.group('APMAC'), parse.group('CalledStationID')
            if APMAC in result:
                result[APMAC].insert(0, CalledStationID)
    return result

def get_ap_huawei(ip, user, password):
    """
    Функция для получения информации о точках с контроллера Huawei, ожидает адрес, логин, пароль. Возвращает словарь со списками данных
    """
    result = {}
    COMMAND = 'display ap all'
    REGEX = '^(?P<AP_ID>\d+\s+(?P<APMAC>\w{4}-\w{4}-\w{4})\s+(?P<APName>\S+)\s+(?P<APGroup>\S+)\s+(?P<APAddress>(\d{1,3}\.){3}\d{1,3}))'
    DEVICE_PARAMS = {'device_type':'huawei', 'ip': ip, 'username': user, 'password': password, 'banner_timeout':16}
    with ConnectHandler(**DEVICE_PARAMS) as connection:
        output = connection.send_command(COMMAND)
    for line in output.split('\n'):
        parse = re.search(REGEX, line)
        if parse:
            APMAC, CalledStationID, APName, APAddress = parse.group('APMAC'), parse.group('APMAC'), parse.group('APName'), parse.group('APAddress')
            result[convert_huawei_mac_to_cisco(APMAC)] = [convert_huawei_mac_to_cisco(CalledStationID), APName, APAddress]
    return result

#Начало основного скрипта
if __name__ == '__main__':
    #Пока список контроллеров задаем локально тут, но в дальнейшем необходима внешняя БД
    devices = dict(CWC001 = dict(address = '10.47.208.1', vendor = 'cisco'),
                   CWC003 = dict(address = '10.47.208.17', vendor = 'cisco'),
                   HWC001 = dict(address = '10.47.208.65', vendor = 'huawei'))
    user = input('User: ')
    password = getpass.getpass('Password: ')
    OLD_REPORT_FILENAME = 'AP_Location_19_07_2019.xlsx'
    NEW_REPORT_FILENAME = 'AP_Location_27_08_2019.xlsx'
    data = {} #Словарь с итоговым результатом
    location = {} #Словарь с данными по локации из предыдущего отчета
    for device in devices:
        if not check_device_linux(devices[device]['address']):
            print('{} in unavailable. Sorry.'.format(device))
            continue
        if devices[device]['vendor'] == 'cisco':
            print('Start connection with {}'.format(device))
            data.update(get_ap_cisco(devices[device]['address'], user, password))
            print('Connection with {} done'.format(device))
        if devices[device]['vendor'] == 'huawei':
            print('Start connection with {}'.format(device))
            data.update(get_ap_huawei(devices[device]['address'], user, password))
            print('Connection with {} done'.format(device))
    #Собираем данные по локации точек из старого отчёта и добавляем в словарь location
    old_report = openpyxl.load_workbook(OLD_REPORT_FILENAME)
    rows = old_report.active.rows
    next(rows) #Проматываем первый ряд, который содержит заголовки
    for row in rows:
        APMAC = row[0].value
        APLocation = row[-1].value
        location.update({APMAC:APLocation})
    old_report.close()
    #Наконец записываем итоговый файл отчёта, куда добавляем инфу с контроллеров из словаря data и информациюю по локации из словаря location
    new_report = openpyxl.Workbook()
    ws = new_report.active
    ws.append(['APMAC', 'CalledStationID', 'APName', 'APAddress', 'APLocation'])
    for APMAC, Information in data.items():
        print(APMAC)
        print(Information)
        print(location.get(APMAC))
        ws.append([APMAC]+Information+[location.get(APMAC)])
    new_report.save(NEW_REPORT_FILENAME)
