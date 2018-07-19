# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def get_int_vlan_map(file_name):
    result_access = {}
    result_trunk = {}
    with open(file_name) as f:
        for line in f:
            if 'FastEthernet' in line:
                interface = line.split()[1]
                #print(interface)
            elif 'trunk allowed' in line:
               # print(line.split()[4].split(','))
                result_trunk[interface] = [int(vlan) for vlan in line.split()[4].split(',')]
            elif 'access vlan' in line:
                #print(line.split()[3])
                result_access[interface] = int(line.split()[3])
    return result_access, result_trunk
             

print(get_int_vlan_map('config_sw1.txt')[0])
print(get_int_vlan_map('config_sw1.txt')[1])
print(ty1pe(get_int_vlan_map))


