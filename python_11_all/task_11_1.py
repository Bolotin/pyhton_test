# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

def parse_cdp_neighbors(command):
    result = {}
    descriptions = ['Capability Codes','S - Switch','Device ID ']
    for line in command.split('\n'):
        if not line or any(word in line for word in descriptions):
            continue
        elif 'show cdp neighbors' in line:
            device = line.split('>')[0]
            print(device)
        else:
            line = [word.strip() for word in line.split('  ') if word]
            result[(device,line[1])] = (line[0],line[-1])
    return result


with open('sw1_sh_cdp_neighbors.txt') as f:
    print(parse_cdp_neighbors(f.read()))          

