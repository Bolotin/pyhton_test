# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

users_vlan = int(input('Give me a vlan: '))
filename = 'CAM_table.txt'
result = []
with open(filename) as file:
    for line in file:
        if 'DYNAMIC' in line:
            vlan, mac, _, interface = line.strip().split()
            result.append([int(vlan), mac, interface])

result.sort()
for vlan, mac, interface in result:
    if users_vlan == vlan:
        print(f'{vlan:<4}   {mac}   {interface}')