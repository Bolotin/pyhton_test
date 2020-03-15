# -*- coding: utf-8 -*-
'''
Задание 7.3

Скрипт должен обрабатывать записи в файле CAM_table.txt.
Каждая строка, где есть MAC-адрес, должна быть обработана таким образом,
 чтобы на стандартный поток вывода была выведена таблица вида (показаны не все строки из файла):

 100    01bb.c580.7000   Gi0/1
 200    0a4b.c380.7000   Gi0/2
 300    a2ab.c5a0.7000   Gi0/3
 100    0a1b.1c80.7000   Gi0/4
 500    02b1.3c80.7000   Gi0/5
 200    1a4b.c580.7000   Gi0/6
 300    0a1b.5c80.7000   Gi0/7

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

TEMPLATE = '{:<4}   {}   {}'
FILENAME = 'CAM_table.txt'

with open(FILENAME) as file:
    for line in file:
        if 'DYNAMIC' in line:
            line = line.strip().split()
            vlan, mac, interface = line[0], line[1], line[3]
            print(TEMPLATE.format(vlan, mac, interface))
