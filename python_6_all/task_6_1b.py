# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
while True:
    ip = input('Enter ip address:')
    try:
        IP = ip.split('.')
        for i in range(len(IP)):
            IP[i] = int(IP[i])
            if 0<=IP[i]<=255:
                check = True
            else:
                check = False
                break
        if len(IP) == 4 and check == True:
            if 1<=IP[0]<=223:
                print('unicast')
            elif 224<=IP[0]<=239:
                print('multicast')
            elif ip == '255.255.255.255':
                print('local broadcast')
            elif ip == '0.0.0.0':
                print('unassigned')
            else:
                print('unused')
            break
        else:
            print('Incorrect IPv4 address')
            continue
    except:
            print('Incorrect IPv4 address')
            continue
