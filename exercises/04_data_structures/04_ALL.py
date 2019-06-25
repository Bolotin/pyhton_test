# 4.1

NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"
NAT = NAT.replace('FastEthernet', 'GigabitEthernet')
print(NAT)

#4.2

MAC = 'AAAA:BBBB:CCCC'
MAC = MAC.replace(':', ('.'))
print(MAC)

#4.3

CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'

vlans = CONFIG.split()[-1].split(',')
print(type(vlans))
print(vlans)

#4.4

command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

vlans1 = set(command1.split()[-1].split(','))
vlans2 = set(command2.split()[-1].split(','))
vlans = vlans1 & vlans2
print(vlans)

#4.5

VLANS = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
VLANS = list(set(VLANS))
VLANS.sort()
print(VLANS)

# 4.6

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

template = """
Protocol:               OSPF
Prefix:                 {}
AD/Metric:              {}
Next-Hop:               {}
Last update:            {}
Outbound Interface:     {}
"""

data = ospf_route.split()
data.pop(3)
data.pop(0)

for i in range(len(data)):
    data[i] = data[i].strip('[],')

PREFIX,METRIC,NEXT_HOP,LAST_UPDATE,INTERFACE = data
print(template.format(PREFIX,METRIC,NEXT_HOP,LAST_UPDATE,INTERFACE))
#print(template.format(Prefix, AD/Metric, Next-Hop, Last_updat, Interface))

#4.7
print('exercise 4.7')

MAC = 'AAAA:BBBB:CCCC'
MAC = MAC.split(':')
for i in range(len(MAC)):
    MAC[i] = bin(int(MAC[i],16))[2:]

MAC = ''.join(MAC)
print(MAC)
