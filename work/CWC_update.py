

from netmiko import ConnectHandler
from datetime import datetime
import subprocess, getpass, re, csv, openpyxl
from pprint import pprint
from get_ap_01 import get_ap_cisco



address = '10.47.208.17'
user = input('User: ')
password = getpass.getpass('Password: ')
filename = input('Filename: ')
DATA = get_ap_cisco(address, user, password)
print('AP Total: ', len(DATA))
if filename:
    print('Information saved in file', filename)
    with open(filename,'w') as file:
        for AP,information in DATA.items():
            file.write(str(AP)+','+','.join(information)+'\n')
