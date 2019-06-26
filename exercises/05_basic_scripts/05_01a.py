from sys import argv

IP = argv[1]
IP, MASK = IP.split('/')

#Manipulations with IP
IP = IP.split('.')
IP = [int(octet) for octet in IP]
IP_BIN = ''.join('{:08b}'.format(octet) for octet in IP)

#Manipulations with MASK

MASK_INT = int(MASK)
MASK_BIN = ''
for i in range(32):
    if i <= MASK_INT:
        MASK_BIN += '1'
    else:
        MASK_BIN += '0'
MASK = [int(MASK_BIN[:8],2), int(MASK_BIN[8:16],2), int(MASK_BIN[16:24],2), int(MASK_BIN[24:],2)]
#manipulations with Network

NET_BIN = ''
for i in range(32):
    NET_BIN += str(int(IP_BIN[i]) and int(MASK_BIN[i]))

NET = [int(NET_BIN[:8],2), int(NET_BIN[8:16],2), int(NET_BIN[16:24],2), int(NET_BIN[24:],2)]

print('Network:')
print('{:<8} {:<8} {:<8} {:<8}'.format(*NET))
print('{:<08b} {:<08b} {:<08b} {:<08b}'.format(*NET))

print('Mask:')
print('/',MASK_INT)
print('{:<10} {:<10} {:<10} {:<10}'.format(*MASK))
print('{:<08b} {:<08b} {:<08b} {:<08b}'.format(*MASK))
