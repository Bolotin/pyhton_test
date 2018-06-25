#4.1
NAT = "ip nat inside source list ACL interface FastEthernat0/1 overload"
NAT = NAT.replace('Fast','Gigabit')
print("4.1 -",NAT)

#4.2

MAC = "AAAA:BBBB:CCCC"
MAC = MAC.replace(':','.')
print("4.2 -",MAC)

#4.3

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
LIST = CONFIG.split()
LIST = LIST[-1].split(',')
print('4.3 -',LIST)

#4.4

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

vlans1 = command1.split()[-1].split(',')
vlans2 = command2.split()[-1].split(',')
vlans = list(set(vlans1).intersection(set(vlans2)))
vlans.sort()

print('4.4 -',vlans)


#4.5 

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
VLANS = list(set(VLANS))
VLANS.sort()
print('4.5 -',VLANS)

#4.6

ospf_route = 'O    10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = ospf_route.strip().split()
ospf_route.pop(3)
ospf_route.pop(0)
ospf_route[1] = ospf_route[1].strip('[]')
ospf_route[2] = ospf_route[2].strip(',')
ospf_route[3] = ospf_route[3].strip(',')

print_template = """
4.6
Protocol:            OSPF
Prefix:              {0[0]}
AD/Metric:           {0[1]}
Next-Hop:            {0[2]} 
Last Update:         {0[3]}
Outbound Interface:  {0[4]}

"""
print(print_template.format(ospf_route))

#4.7

MAC = 'AAAA:BBBB:CCCC'
MAC = MAC.replace(':','')
print('4.7 - {:b}'.format(int(MAC,16)))

#4.8

IP = '192.168.1.1'
IP = IP.split('.')
IP[0] = int(IP[0])
IP[1] = int(IP[1])
IP[2] = int(IP[2])
IP[3] = int(IP[3])

print(IP,len(IP))

print_template = """
4.8:
{0[0]:<8}  {0[1]:<8}  {0[2]:<8}  {0[3]:<8}
{0[0]:<8b}  {0[1]:<8b}  {0[2]:0<8b}  {0[3]:0<8b}
"""

print(print_template.format(IP))

