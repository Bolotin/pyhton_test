# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

import subprocess
from ipaddress import ip_network

def check_ip_address(hosts):
    alive_hosts = []
    unreachable_hosts = []
    for host in hosts:
        reply = subprocess.run('ping -c 3 {}'.format(host), shell = True, stdout = subprocess.DEVNULL)
        print('.')
        if reply.returncode == 0:
            alive_hosts.append(host)
        else:
            unreachable_hosts.append(host)
    return(alive_hosts,unreachable_hosts)

if __name__=='__main__':
    net = ip_network('192.168.0.0/29')
    hosts = [str(host) for host in net]
    alive,unreach = check_ip_address(hosts)
    print('\nAlive hosts:')
    for host in alive:
        print(host)
    print('\nUnreachable host:')
    for host in unreach:
        print(host)
