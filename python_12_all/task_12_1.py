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

def check_ip_address(hosts):
    alive_hosts = []
    unreachable_hosts = []
    for host in hosts:
        reply = subprocess.run('ping -c 3 {}'.format(host), shell = True)
        if reply.returncode == 0:
            alive_hosts.append(host)
        else:
            unreachable_hosts.append(host)
    return(alive_hosts,unreachable_hosts)

if __name__=='__main__':
    test = ['192.168.0.190','192.168.0.191','192.168.0.192']
    
