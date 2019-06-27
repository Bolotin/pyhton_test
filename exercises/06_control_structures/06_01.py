from sys import argv

IP = argv[1]
first_octet = int(IP.split('.')[0])

if IP == '0.0.0.0':
    print('unassigned')
elif IP == '255.255.255.255':
    print('local broadcast')
elif 1 < first_octet < 223:
    print('unicast')
elif 224 < first_octet < 239:
    print('multicat')
else:
    print('unused')
