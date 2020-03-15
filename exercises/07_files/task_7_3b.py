# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


TEMPLATE = '{:<4}   {}   {}'
FILENAME = 'CAM_table.txt'
result = []
vlan = input('Give me a number of vlan:')

with open(FILENAME) as file:
    for line in file:
        if 'DYNAMIC' in line:
            line = line.strip().split()
            result.append([line[0], line[1], line[3]])
    result.sort(key = lambda vlan: int(vlan[0]))
    for item in result:
        if item[0] == vlan:
            print(TEMPLATE.format(*item))
