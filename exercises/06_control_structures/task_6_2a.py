# -*- coding: utf-8 -*-
'''
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''


ip = input('Give me an address: ')

try:
    oct = ip.split('.')
    oct = [int(i) for i in oct]
    if len(oct) != 4:
        raise
    for i in oct:
        if i < 0 or i > 255:
            raise
except:
    print('Wrong ip address!')
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
