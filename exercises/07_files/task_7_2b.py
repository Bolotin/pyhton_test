# -*- coding: utf-8 -*-
'''
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv
filename = argv[1]
RESULT_FILE = 'config_sw1_cleared.txt'

with open(filename) as file, open(RESULT_FILE,'w') as result:
    for line in file:
        for word in ignore:
            if word in line:
                break
        else:
            result.write(line)
