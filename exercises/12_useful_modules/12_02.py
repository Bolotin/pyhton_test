import subprocess
import ipaddress

def check(data):
    available = []
    unavailable = []
    if len(data.split('-')) == 1:
        device_ip = ipaddress.ip_address(data)
        check = subprocess.run('ping {} -c 3'.format(device_ip), shell = True, stdout = subprocess.DEVNULL)
        if check.returncode == 0:
            available.append(data)
        else:
            unavailabel.append(data)
    else:
        device_ip = ipaddress.ip_address(data.split('-')[0])
        print(device_ip)
        device_range = int(data.split('-')[-1].split('.')[-1]) - int(data.split('-')[0].split('.')[-1])
        print(device_range)
        i = 0
        while i<=device_range:
            print('Checking ', device_ip)
            check = subprocess.run('ping {} -c 3'.format(device_ip), shell = True, stdout = subprocess.DEVNULL)
            if check.returncode == 0:
                available.append(str(device_ip))
            else:
                unavailable.append(str(device_ip))
            device_ip += 1
            i +=1
    return available, unavailable

if __name__ == '__main__':
    devices1 = '8.8.8.8'
    devices2 = '192.168.100.1-5'
    devices3 = '192.168.100.1-192.168.100.5'
    print(check(devices1))
    print(check(devices2))
    print(check(devices3))
