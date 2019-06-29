from sys import argv

IP = argv[1]
try:
    octets = [int(octet) for octet in IP.split('.')]
    octets[0] = int(IP.split('.')[0])
    if not len(octets) == 4:
        raise ValueError()
    for octet in octets:
        if octet not in range(256):
            raise ValueError()
    if IP == '0.0.0.0':
        print('unassigned')
    elif IP == '255.255.255.255':
        print('local broadcast')
    elif 1 < octets[0] < 223:
        print('unicast')
    elif 224 < octets[0] < 239:
        print('multicat')
    else:
        print('unused')
except ValueError:
    print('Incorrect IPv4 address')
