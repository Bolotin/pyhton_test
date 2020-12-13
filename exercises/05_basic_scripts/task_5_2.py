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

network_template = """
Network:
{oct_1:<8} {oct_2:<8}  {oct_3:<8}  {oct_4:<8}
{oct_1:08b} {oct_2:08b}  {oct_3:08b}  {oct_4:08b}
"""

mask_template = """
Mask:
/{mask}
{mask_1:<8}  {mask_2:<8}  {mask_3:<8}  {mask_4:<8}
{mask_1:08b}  {mask_2:08b}  {mask_3:08b}  {mask_4:08b}
"""

network, mask = input('Give me a network, beach! ').split('/')
mask = int(mask)
oct_1, oct_2, oct_3, oct_4 = list(network.split('.'))

mask_binary = '1'*mask + '0'*(32-mask)
mask_1, mask_2, mask_3, mask_4 = int(mask_binary[0:8],2), int(mask_binary[8:16],2), int(mask_binary[16:24],2), int(mask_binary[24:],2)

print(network_template.format(oct_1 = int(oct_1), oct_2 = int(oct_2), oct_3 = int(oct_3), oct_4 = int(oct_4)))
print(mask_template.format(mask_1 = mask_1, mask_2 = mask_2, mask_3 = mask_3, mask_4 = mask_4, mask = mask))
