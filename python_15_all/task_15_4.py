# -*- coding: utf-8 -*-
'''
Задание 15.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.

'''

from re import finditer
from pprint import pprint

def parse_sh_ip_int_br(filename):
    result = []
    regex = '(?P<interface>\S+) +(?P<ip_adress>[\d.]+|unassigned) +\S+ +\S+ +(?P<status>up|down|administratively down) +(?P<protocol>up|down)'
    with open(filename) as f:
        matches = finditer(regex,f.read())
        for match in matches:
            result.append(match.groups())
    return result

filename = 'sh_ip_int_br_2.txt'
if __name__=='__main__':
    pprint(parse_sh_ip_int_br(filename))
    

