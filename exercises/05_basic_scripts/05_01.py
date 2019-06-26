# exercise 5.1

IP = input('Please give me IP address ')
IP, MASK = IP.split('/')
IP = IP.split('.')
IP = [int(octet) for octet in IP]

print('Network:')
print('{:<10} {:<10} {:<10} {:<10}'.format(*IP))
print('{:<10b} {:<10b} {:<10b} {:<10b}'.format(*IP))

MASK_BIN = ''
for i in range(32):
    if i < int(MASK):
        MASK_BIN +='1'
    else:
        MASK_BIN +='0'
MASK_BIN = [MASK_BIN[:8],MASK_BIN[8:16],MASK_BIN[16:24],MASK_BIN[24:32]]
MASK_DEC = [int(octet,2) for octet in MASK_BIN]
print('Mask:')
print('/',MASK)
print('{:<10} {:<10} {:<10}{:<10}'.format(*MASK_DEC))
print('{:<10} {:<10} {:<10}{:<10}'.format(*MASK_BIN))
