# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def int_vlan_map(file_name='config_sw2.txt'):
    result_trunk = {}
    result_access = {}
    with open(file_name) as f:
        for line in f:
            if 'FastEthernet' in line:
                interface = line.split()[1]
            elif 'trunk allowed' in line:
                result_trunk[interface] = [int(vlan) for vlan in line.split()[4].split(',')]
            elif 'mode access' in line:
                result_access[interface] = 1
            elif 'access vlan' in line:
                result_access[interface] = int(line.split()[3])
    return result_trunk,result_access
                
print(int_vlan_map()[0])
print(int_vlan_map()[1])
