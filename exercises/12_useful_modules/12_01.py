import subprocess

def check_ip(devices):
    available = []
    unavailable = []
    for device in devices:
        check = subprocess.run('ping {} -c 3'.format(device), shell = True, stdout = subprocess.DEVNULL)
        if check.returncode == 0:
            available.append(device)
        else:
            unavailable.append(device)
    return available, unavailable

if __name__ == '__main__':
    devices = ['192.168.100.1','8.8.8.8','ya.ru','10.10.10.10']
    data = check_ip(devices)
    print('Available devices: ', ', '.join(data[0]))
    print('Unavailable devices: ',', '.join(data[1]))
