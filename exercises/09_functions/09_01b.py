def generate_access_config(interfaces, psecurity = False):
    access_template = ['switchport mode access',
                       'switchport access vlan',
                       'switchport nonegotiate',
                       'spanning-tree portfast',
                       'spanning-tree bpduguard enable']
    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
    result = {}
    for interface, vlan in interfaces.items():
        result[interface] = []
        for command in access_template:
            if command.endswith('access vlan'):
                result[interface].append(command + ' ' + (str(vlan)))
            else:
                result[interface].append(command)
        if psecurity:
            for command in port_security:
                result[interface].append(command)
    return result





access_dict = { 'FastEthernet0/12':10,
                'FastEthernet0/14':11,
                'FastEthernet0/16':17,
                'FastEthernet0/17':150 }

for interface,configuration in generate_access_config(access_dict, psecurity = True).items():
    print(interface)
    print(configuration)
