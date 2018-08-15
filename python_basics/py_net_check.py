#! /usr/bin/env python3

import ipaddress

def py_net_check(net):
    result = {}
    try:
        net = ipaddress.ip_network(net)
    except ValueError:
        print('{} is not an IPv4 or IPv6 netwotk!'.format(net))
        return False
    for host in net:
        result[str(host)] = py_ping(str(host))
        print('{} is {}'.format(str(host), result[str(host)]))
    return(result)

if __name__ == '__main__':
    net = input('Give me a net: ')
    py_net_check(net)
    
    
