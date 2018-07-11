# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

print_template = """
Protocol:              OSPF
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
"""
with open('ospf.txt') as file:
    for line in file:
        line = line.split()
        line.remove('O')
        line.remove('via')
        line[1] = line[1].strip('[]')
        line[2] = line[2].strip(',')
        line[2] = line[2].strip(',')
        print(print_template.format(line[0],line[1],line[2], line[3], line[4]))
        
