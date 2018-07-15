# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

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

vlan = input('Please, enter number of vlan: ')         
print('{}   {}  {}'.format(vlan, result[vlan][0], result[vlan][1]))    
