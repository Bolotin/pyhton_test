from netmiko import ConnectHandler
from pprint import pprint
import subprocess
import getpass

def get_ap_cisco(data):
    pass

def get_ap_huawei(data):
    pass

def check(devices):
    result = {}
    for device,ip in devices.items():
        check = subprocess.run('ping -c 3 {}'.format(ip), shell = True, stdout = subprocess.DEVNULL)
        if check.returncode == 0:
            result[device] = True
        else:
            result[device] = False
    return result


if __name__ == '__main__':
    devices = dict(CWC001 = '10.47.208.1', CWC003 = '10.47.208.17', HWC001 = '10.47.208.65' )
    COMMAND = 'show ap summary'
    USER = input('User: ')
    PASSWORD = getpass.getpass('Password: ')
    IP = devices['CWC001']

    DEVICE_PARAMS = {'device_type':'cisco_wlc', 'ip': IP, 'username': USER, 'password': PASSWORD, 'banner_timeout':16}

    with ConnectHandler(**DEVICE_PARAMS) as connection:
        result = connection.send_command(COMMAND)
        with open('CWC001.txt','w') as file:
            file.write(result)
