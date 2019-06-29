trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan']

fast_int = {'access':{'0/12':'10','0/14':'11','0/16':'17','0/17':'150'},
            'trunk':{'0/1':['add','10','20'],
                     '0/2':['only','11','30'],
                     '0/4':['del','17']} }

for intf, vlans in fast_int['trunk'].items():
    print('interfase FastEthernet' + intf)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            if vlans[0] == 'only':
                print(' {} {}'.format(command, ','.join(vlans[1:])))
            else:
                print(' {} {} {}'.format(command,vlans[0],','.join(vlans[1:])))
        else:
            print(' {}'.format(command))
