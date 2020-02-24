# -*- coding: utf-8 -*-
'''
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv

prefix = argv[1]
network = prefix.split('/')[0].split('.') #get list net
mask = int(prefix.split('/')[-1]) #get int mask

network = [int(i) for i in network]
mask = '1'*mask +'0'*(32-mask)
mask = [int(mask[:8],base=2), int(mask[8:16],base=2),int(mask[16:24],base=2),int(mask[24:],base=2)]

net_template = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:0<8b}  {1:0<8b}  {2:0<8b}  {3:0<8b}
"""

mask_template = """
Network:
{0:<8}  {1:<8}  {2:<8}  {3:<8}
{0:0<8b}  {1:0<8b}  {2:0<8b}  {3:0<8b}
"""

print(net_template.format(*network))
print(mask_template.format(*mask))
