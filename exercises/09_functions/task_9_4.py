# -*- coding: utf-8 -*-
'''
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

from pprint import pprint

def convert_config_to_dict(config_filename, ignore):
    result = {}
    with open(config_filename) as config_file:
        for line in config_file:
            line = line.strip('\n')
            if line.startswith('!') or any(word in line for word in ignore):
                continue
            elif not line.startswith(' '):
                first_tier_command = line.strip()
                result[first_tier_command] = []
            elif line.startswith(' '):
                result[first_tier_command].append(line.strip())

    return result



config_filename = 'config_sw1.txt'
ignore = ['duplex', 'alias', 'Current configuration']

pprint(convert_config_to_dict(config_filename, ignore))

