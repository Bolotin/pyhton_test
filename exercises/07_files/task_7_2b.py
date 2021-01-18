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

# param - config_sw1.txt
filename = argv[1]
result_filename = 'config_sw1_cleared.txt'

with open(filename) as file, open(result_filename, 'w') as result:
    for line in file:
        if any(word in line for word in ignore):
            continue
        else:
            result.write(line)

#test
with open(result_filename) as result:
    for line in result:
        print(line.strip())