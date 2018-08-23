# -*- coding: utf-8 -*-
'''
Задание 15.3b

Проверить работу функции parse_cfg из задания 15.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 15.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
from re import search
from pprint import pprint

def parse_cfg(filename, regex):
    result = {}
    with open(filename) as f:
        for line in f:
            match = search(regex,line)
            if match and match.lastgroup == 'interface':
                interface = match.group(match.lastgroup)
                result[interface] = []
            elif match:
                result[interface].append(tuple(item for item in match.groups() if item))
    result = {item:result[item] for item in result if result[item]}
    return result
    
filename = 'config_r2.txt'
regex = ('interface (?P<interface>\S+)'
         '|ip address (?P<address>(?:\d{1,3}\.){3}\d{1,3}) (?P<mask>(?:\d{1,3}\.){3}\d{1,3})')

pprint(parse_cfg(filename, regex))

