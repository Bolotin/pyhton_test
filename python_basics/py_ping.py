#! /usr/bin/env python3

import subprocess
from ipaddress import ip_network
from multiprocessing import Pool

def py_ping(target):
    reply = subprocess.run('ping -c 3 {}'.format(target), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if reply.returncode == 0:
        return('alive')
    elif reply.returncode == 1:
        return('unreachable')
    else:
        return('unknown')

def py_net_check(net):
    try:
        net = ip_network(net)
        hosts = [str(host) for host in net]
    except ValueError:
        print('{} is not an IPv4 or IPv6 network!'.format(net))
        return False
    with Pool(processes=32) as p:
        result = dict(zip(hosts, p.map(py_ping, hosts)))
    return(result,hosts)

if __name__ == '__main__':
    net = input('Give me a net: ')
    result,*hosts = py_net_check(net)
    if result:
        for host in hosts[0]:
            print('The {} is {}'.format(host,result[host]))
