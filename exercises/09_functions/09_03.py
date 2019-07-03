def get_int_vlan_map(file_name):
    '''Give me a file name and I return you a lict of access ports and a list of trunk posts'''
    access_interfaces = {}
    trunk_interfaces = {}
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith('interface'):
                interface = line.split()[-1]
            if 'access vlan' in line:
                access_interfaces[interface] = line.strip().split()[-1]
            if 'allowed vlan' in line:
                trunk_interfaces[interface] =  line.strip().split()[-1].split(',')
        return(access_interfaces,trunk_interfaces)


file_name = 'config_sw1.txt'
access_interfaces, trunk_interfaces = get_int_vlan_map(file_name)
print(access_interfaces)
print(trunk_interfaces)
