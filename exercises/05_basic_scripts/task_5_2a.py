# -*- coding: utf-8 -*-
'''
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.1/30 - хост из сети 10.0.5.0/30

Если пользователь ввел адрес 10.0.1.1/24,
вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

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

prefix = input('Give me an address: ')
address = prefix.split('/')[0].split('.')
address = [int(i) for i in address]
mask = int(prefix.split('/')[1])

address = '{0:0<8b}{1:0<8b}{2:0<8b}{3:0<8b}'.format(*address)
network = address[:mask] + '0'*(32-mask)
network = [int(network[:8],base=2), int(network[8:16],base=2), int(network[16:24],base=2), int(network[24:],base=2)]
mask = '1'*mask +'0'*(32-mask)
mask = [int(mask[:8],base=2), int(mask[8:16],base=2),int(mask[16:24],base=2),int(mask[24:],base=2)]
print(net_template.format(*network))
print(mask_template.format(*mask))
