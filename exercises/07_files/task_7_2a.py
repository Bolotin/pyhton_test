# -*- coding: utf-8 -*-
'''
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv
filename = argv[1]

with open(filename) as file:
    for line in file:
        if line.strip().startswith('!'):
            continue
        for word in ignore:
            if word in line:
                break
        else:
            print(line.strip())
