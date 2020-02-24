# -*- coding: utf-8 -*-
'''
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

prefix = input('Input the prefix: ')
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
