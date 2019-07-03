def generate_trunk_config(interfaces):
    trunk_template = ['switchport trunk encapsulation dot1q',
                      'switchport mode trunk',
                      'switchport trunk native vlan 999',
                      'switchport trunk allowed vlan']
    result = {}
    for interface, vlans in interfaces.items():
        result[interface] = []
        for command in trunk_template:
            if command.endswith('allowed vlan'):
                result[interface].append(command + ' ' + ','.join([str(vlan) for vlan in vlans]))
            else:
                result[interface].append(command)
    return result





trunk_dict = { 'FastEthernet0/1':[10,20,30],
               'FastEthernet0/2':[11,30],
               'FastEthernet0/4':[17] }

for key,value in generate_trunk_config(trunk_dict).items():
    print(key)
    print(value)
