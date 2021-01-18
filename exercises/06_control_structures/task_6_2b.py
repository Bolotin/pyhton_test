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
        ip = input('Give me an address: ')
        oct = ip.split('.')
        oct = [int(i) for i in oct]
        if len(oct) != 4:
            raise
        for i in oct:
            if i < 0 or i > 255:
                raise
    except:
        print('Wrong ip address!')
        continue
    else:
        if oct[0] in range(1,224):
            print('unicast')
        elif oct[0] in range(224,240):
            print('multicast')
        elif ip == '255.255.255.255':
            print('local broadcast')
        elif ip == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
    break
