# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''

from tabulate import tabulate
from itertools import zip_longest

def ip_table(reachable,unreachable):
    print(tabulate(zip_longest(reachable,unreachable),headers=['Reachable','Unreachable']))


if __name__=='__main__':
    reachable = ['10.1.1.1','10.1.1.2']
    unreachable = ['10.1.1.7','10.1.1.8','10.1.1.9']
    ip_table(reachable,unreachable)    
