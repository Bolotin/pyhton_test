# -*- coding: utf-8 -*-
'''
Задание 12.2


Функция check_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например,
192.168.100.1-10.

Создать функцию check_ip_availability, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.

IP-адреса могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо проверить доступность всех адресов диапазон
а включая последний.

Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последни
й октет адреса.

Функция возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов


Для выполнения задачи можно воспользоваться функцией check_ip_addresses из задания 12.1
'''

from ipaddress import ip_address
import subprocess

def check_ip_availability(addresses):
    result_available = []
    result_unreachable = []
    hosts = []
    ip1,*ip2 = addresses.split('-')
    if ip2:
        span = int(ip2[0].split('.')[-1]) - int(ip1.split('.')[-1])
        for i in range(span+1):
            hosts.append(str(ip_address(ip1)+i))
    else:
        hosts.append(ip1)
    for host in hosts:
        result = subprocess.run('ping -c 3 {}'.format(host), shell = True, stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            result_available.append(host)
        else:
            result_unreachable.append(host)
    return(result_available,result_unreachable)

if __name__=='__main__':
    test1 = '192.168.100.1'
    test2 = '192.168.100.1-10'
    test3 = '192.168.100.1-192.168.100.10'

    result_available,result_unreachable = check_ip_availability(test1)
    print('TEST1')
    print('Available host')
    for host in result_available:
        print(host)
    print('Unreachable hosts')
    for host in result_unreachable:
        print(host)

    result_available,result_unreachable = check_ip_availability(test2)
    print('TEST2')
    print('Available host')
    for host in result_available:
        print(host)
    print('Unreachable hosts')
    for host in result_unreachable:
        print(host)

    result_available,result_unreachable = check_ip_availability(test3)
    print('TEST3')
    print('Available host')
    for host in result_available:
        print(host)
    print('Unreachable hosts')
    for host in result_unreachable:
        print(host)
