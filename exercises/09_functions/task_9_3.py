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

config_filename = 'config_sw1.txt'

def get_int_vlan_map(config_filename):
    access_intf = {}
    trunk_intf = {}
    with open(config_filename) as config_file:
        for line in config_file:
            line = line.strip()
            if line.startswith('interface'):
                intf = line.split()[-1]
            elif line.startswith('switchport access'):
                access_intf[intf] = line.split()[-1]
            elif line.startswith('switchport trunk allowed vlan'):
                trunk_intf[intf] = line.split()[-1].split(',')
    return (access_intf, trunk_intf)


pprint(get_int_vlan_map(config_filename))
