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
