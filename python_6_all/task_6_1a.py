# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

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
    else:
        print('Incorrect IPv4 address')
except:
        print('Incorrect IPv4 address')
