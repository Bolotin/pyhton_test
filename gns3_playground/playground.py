from pprint import pprint
from netmiko import ConnectHandler
from concurrent.futures import ThreadPoolExecutor
from termcolor import cprint

# My functions (begin)
from env_list import create_env_list
from env_list import get_env_list
from py_ping import py_ping
# My functions (end)

# Playhround test data
# data = {'MSK-M10': {'device_type': 'juniper',
#                     'ip': '172.16.255.1'},
#         'MSK-M9': {'device_type': 'cisco_ios',
#                    'ip': '172.16.255.2'},
#         'SPB-CORE': {'device_type': 'cisco_ios',
#                      'ip': '172.16.255.3'},
#         'SIB-CORE': {'device_type': 'juniper',
#                      'ip': '172.16.255.4'}}

# create_env_list('gns3_playground.yaml', data)
dev_list = get_env_list('gns3_playground.yaml')
for device in dev_list:
    result = py_ping(dev_list[device]['ip'])
    if result == 'alive':
        color = 'green'
    else:
        color = 'red'
    cprint('{} - {}'.format(device, result), color)
