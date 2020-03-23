# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from pprint import pprint

def get_int_vlan_map(config_filename):
    access_interfaces = {}
    trunk_interfaces = {}
    with open(config_filename) as file:
        for line in file:
            if 'interface' in line and 'Ethernet' in line:
                interface = line.strip().split()[1]
            elif 'switchport trunk allowed vlan' in line:
                trunk_interfaces[interface] = line.strip().split()[-1].split(',')
            elif 'switchport access vlan' in line:
                access_interfaces[interface] = line.strip().split()[-1]
    return (access_interfaces, trunk_interfaces)

CONFIG_FILENAME = 'config_sw1.txt'

pprint(get_int_vlan_map(CONFIG_FILENAME))
