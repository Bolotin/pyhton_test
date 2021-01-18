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

filename = 'ospf.txt'
template = """
Protocol:              OSPF
Prefix:                {prefix}
AD/Metric:             {metric}
Next-Hop:              {next_hop}
Last update:           {last_update}
Outbound Interface:    {interface}
"""
with open(filename) as file:
    for line in file:
        line = line.strip().split()
        prefix = line[1]
        metric = line[2].strip('[]')
        next_hop = line[4].strip(',')
        last_update = line[5].strip(',')
        interface = line[6]
        print(template.strip().format(line=line, prefix=prefix, metric=metric, last_update=last_update, interface=interface, next_hop=next_hop))
        print()
