def generate_trunk_config(interfaces):
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
    result = []
    for interface, vlans in interfaces.items():
        result.append('interface ' + interface)
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                result.append(command + ' ' + ','.join([str(vlan) for vlan in vlans]))
            else:
                result.append(command)
    return result





trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

for line in generate_trunk_config(trunk_dict):
    print(line)
