# -*- coding: utf-8 -*-
'''
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']

from sys import argv

# param1 - config_sw1.txt
# param2 - config_sw1_cleared.txt
filename, result_filename = argv[1:]

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