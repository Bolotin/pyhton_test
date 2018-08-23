# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

from re import search

def parse_cfg(filename, regex):
    result = {}
    with open(filename) as f:
        for line in f:
            match = search(regex,line)
            if match and match.lastgroup == 'interface':
                interface = match.group(match.lastgroup)
            elif match:
                result[interface] = tuple(item for item in match.groups() if item)
    return result

filename = 'config_r1.txt'
regex = ('interface (?P<interface>\S+)''|ip address (?P<address>(?:\d{1,3}\.){3}\d{1,3}) (?P<mask>(?:\d{1,3}\.){3}\d{1,3})')

print(parse_cfg(filename,regex)) 
        
