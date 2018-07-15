# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

result = {}

with open('CAM_table.txt') as f:
    for line in f:
        line = line.split()
        if line:
            if line[0].isdigit():
                vlan,mac,_,interface = line
                result[vlan] = [mac,interface]

print(result)               
for key in sorted(result.keys()):
    print('{}  {}  {}'.format(key,result[key][0],result[key][1]))
                
