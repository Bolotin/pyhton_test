from netmiko import ConnectHandler
from datetime import datetime
import subprocess, getpass, re, csv
from pprint import pprint
import openpyxl

def get_base_mac_cisco(ip, user, password):
    RESULT = {}
    COMMAND = 'show ap join stats summary all'
    DEVICE_PARAMS = {'device_type':'cisco_wlc', 'ip': ip, 'username': user, 'password': password, 'banner_timeout':16}
    regex = '^(?P<MAC_BASE>(\w\w:){5}\w\w)\s+(?P<MAC_ETHER>(\w\w:){5}\w\w)'
    with ConnectHandler(**DEVICE_PARAMS) as connection:
        result = connection.send_command(COMMAND).split('\n')
        for line in result:
            if line:
                search = re.search(regex, line.strip())
                if search:
                    print(search.group())
                    MAC_BASE, AP_MAC = search.group('MAC_BASE'), search.group('MAC_ETHER')
                    RESULT[AP_MAC] = MAC_BASE
    return RESULT




if __name__ == '__main__':
    devices = dict(CWC001 = dict(address = '10.47.208.1', vendor = 'cisco'),
                   CWC003 = dict(address = '10.47.208.17', vendor = 'cisco'))
    user = input('User: ')
    password = getpass.getpass('Password: ')
    data = {}
    for device in devices:
        data.update(get_base_mac_cisco(devices[device]['address'], user, password))
    pprint(data)

    #Вот теперь наконец заменим MAC в нашем файле
    OLD_DATA_FILENAME = 'AP_Location_19_07_2019.xlsx'
    result_filename = 'AP_Location_{}.xlsx'.format(datetime.today().strftime('%d_%m_%Y'))
    wb = openpyxl.load_workbook(OLD_DATA_FILENAME)
    columns = wb.active.columns
    first_column = next(columns)
    for cell in first_column:
        if cell.value in data:
            cell.value = data[cell.value]
    wb.save(result_filename)
