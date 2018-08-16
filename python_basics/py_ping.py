#! /usr/bin/env python3

import subprocess
from ipaddress import ip_network
from multiprocessing import Pool
import argparse

def py_ping(target,count = 3):
    """
    Take ipv4 address (as a string)
    Check it with some number of icmp requests. (default - 3)
    Return host status (alive|unreachable|unknown) (as a string)
    """
    reply = subprocess.run('ping -c {count} {target}'.format(target=target, count=count), shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if reply.returncode == 0:
        return('alive')
    elif reply.returncode == 1:
        return('unreachable')
    else:
        return('unknown')

def py_net_check(net,proc = 16, count = 3):
    """
    Take ip network (as a string)
    Check all hosts in this networkself.
    Return result as a dictionary and list of hosts.
    Uses multiple processes (default = 16)
    """
    try:
        net = ip_network(net)
        hosts = [str(host) for host in net]
    except ValueError:
        return (False,[])
    with Pool(processes=proc) as p:
        result = dict(zip(hosts, p.map(py_ping, hosts, count)))
    return(result,hosts)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Chech of ip network')
    parser.add_argument('-c',action='store',dest='count',default=3,type=int,help='The number of icmp requests (3 by default)')
    parser.add_argument('-m',action='store',dest='proc',default=16,type=int,help='The number of multiple subprocess (16 by default)')
    parser.add_argument('-u',action='store',dest='unreachable',default=False,type=bool,help='Show unreachable hosts (False by default)')
    parser.add_argument('-f',action='store',dest='file_name',default=None,type=str,help='The name of file to save results (None by default)')
    parser.add_argument('net',action='store',help='IPv4 network (example - 192.168.0.0/24)')
    args = parser.parse_args()

    result,hosts = py_net_check(args.net,args.proc,args.count)
    if result:
        for host in hosts:
            if args.unreachable or result[host] =='alive':
                print('The {} is {}'.format(host,result[host]))
        if args.file_name:
            with open(args.file_name, 'w+') as f:
                for host in hosts:
                    if args.unreachable or result[host] =='alive':
                        f.write('{},{}\n'.format(host,result[host]))
    else:
        print('{} is not an IPv4 network!'.format(args.net))
