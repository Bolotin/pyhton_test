OUS_CONFIG_FILENAME = 'ous_cfg.txt'
RUS_CONFIG_FILENAME = 'rus_cfg.txt'
DELETE_INT_FILENAME = 'del_int_cfg.txt'

vlan_template = """
vlan {vlan}
name {vrf}_{prefix}/23
exit

"""

interface_template = """
interface vlan {vlan}
description {vrf}_{prefix}/23
no shutdown
mtu 9142
vrf member {vrf}
no ip redirect
ip address {int_address}/23
no ipv6 redirect
no ip arp gratuitous hsrp duplicate
hsrp version 2
hsrp {vlan}
authentication md5 key-chain HSRP_KEY
preempt delay reload 60
priority {priority}
timers 5 15
ip {hsrp_address}
track 1 decrement 50
exit
ip dhcp relay address 100.104.248.1
ip dhcp relay address 10.54.220.1
ip dhcp relay address 10.34.240.73
ip dhcp relay address 10.34.240.74
exit

"""

del_int_template = """
no interfaces vlan {vlan}
no vlan {vlan}
"""

with open(OUS_CONFIG_FILENAME,'w') as ous_cfg, open(RUS_CONFIG_FILENAME,'w') as rus_cfg, open(DELETE_INT_FILENAME,'w') as del_int_cfg:
    #e08z vlans and intefaces
    VRF = 'e08z'
    IP_TEMPLATE = '100.70.{octet_3}.{octet_4}'
    VLAN = 1801
    for octet_3 in range(64,96,2):
        #OUS first
        prefix = IP_TEMPLATE.format(octet_3 = str(octet_3), octet_4 = '0')
        int_address = IP_TEMPLATE.format(octet_3 = str(octet_3+1), octet_4 = '251')
        hsrp_address = IP_TEMPLATE.format(octet_3 = str(octet_3+1), octet_4 = '250')
        PRIORITY = '120'
        ous_cfg.write(vlan_template.format(vlan = str(VLAN), vrf = VRF, prefix = prefix))
        ous_cfg.write(interface_template.format(vrf = VRF, prefix = prefix, int_address = int_address, vlan = str(VLAN), priority = PRIORITY, hsrp_address = hsrp_address))
        del_int_cfg.write(del_int_template.format(vlan = str(VLAN)))
        #and now RUS_CONFIG_FILENAME
        PRIORITY = '80'
        int_address = IP_TEMPLATE.format(octet_3 = str(octet_3+1), octet_4 = '252')
        rus_cfg.write(vlan_template.format(vlan = str(VLAN), vrf = VRF, prefix = prefix))
        rus_cfg.write(interface_template.format(vrf = VRF, prefix = prefix, int_address = int_address, vlan = str(VLAN), priority = PRIORITY, hsrp_address = hsrp_address))
        VLAN += 1
    #e09z vlans and intefaces
    VRF = 'e09z'
    IP_TEMPLATE = '100.64.{octet_3}.{octet_4}'
    VLAN = 1901
    for octet_3 in range(0,128,2):
        #OUS first
        prefix = IP_TEMPLATE.format(octet_3 = str(octet_3), octet_4 = '0')
        int_address = IP_TEMPLATE.format(octet_3 = str(octet_3+1), octet_4 = '251')
        hsrp_address = IP_TEMPLATE.format(octet_3 = str(octet_3+1), octet_4 = '250')
        PRIORITY = '120'
        ous_cfg.write(vlan_template.format(vlan = str(VLAN), vrf = VRF, prefix = prefix))
        ous_cfg.write(interface_template.format(vrf = VRF, prefix = prefix, int_address = int_address, vlan = str(VLAN), priority = PRIORITY, hsrp_address = hsrp_address))
        del_int_cfg.write(del_int_template.format(vlan = str(VLAN)))
        #and now RUS_CONFIG_FILENAME
        PRIORITY = '80'
        int_address = IP_TEMPLATE.format(octet_3 = str(octet_3+1), octet_4 = '252')
        rus_cfg.write(vlan_template.format(vlan = str(VLAN), vrf = VRF, prefix = prefix))
        rus_cfg.write(interface_template.format(vrf = VRF, prefix = prefix, int_address = int_address, vlan = str(VLAN), priority = PRIORITY, hsrp_address = hsrp_address))
        VLAN +=1
