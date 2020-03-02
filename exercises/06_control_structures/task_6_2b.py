# -*- coding: utf-8 -*-
'''
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
while True:
    try:
        ip = input('Please, give me an ip address: ')
        ip_list = [int(item) for item in ip.split('.')]
        if len(ip_list) != 4:
            raise
        elif any([item < 0 or item > 255 for item in ip_list]):
            raise

        if ip == '0.0.0.0':
            type = 'unassigned'
        elif ip == '255.255.255.255':
            type = 'local broadcast'
        elif 0<ip_list[0]<224:
            type = 'unicast'
        elif 223<ip_list[0]<240:
            type = 'multicast'
        else:
            type = 'unused'

        print(type)
    except:
        print('Incorrect IP address')
    else:
        break
