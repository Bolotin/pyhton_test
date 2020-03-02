# -*- coding: utf-8 -*-
'''
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. Определить тип IP-адреса.
3. В зависимости от типа адреса, вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ip = input('Please, give me an ip address: ')
first_oct = int(ip.split('.')[0])

if ip == '0.0.0.0':
    type = 'unassigned'
elif ip == '255.255.255.255':
    type = 'local broadcast'
elif 0<first_oct<224:
    type = 'unicast'
elif 223<first_oct<240:
    type = 'multicast'
else:
    type = 'unused'

print(type)
