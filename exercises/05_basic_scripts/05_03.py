access_template = ['switchport mode access',
                   'switchport access vlan {}',
                   'switchport nonegotiate',
                   'spanning-tree portfast',
                   'spanning-tree bpduguard enable']

trunk_template = ['switchport trunk encapsulation dot1q',
                  'switchport mode trunk',
                  'switchport trunk allowed vlan {}']

templates = {'access':access_template,'trunk':trunk_template}
questions = {'access':'Enter VLAN number: ','trunk':'Enter allowed VLANs: '}

mode = input('Enter interface mode (access/trunk): ')
interface = input('Enter interface name: ')
vlans = input(questions[mode])
print('\n'.join(templates[mode]).format(vlans))
