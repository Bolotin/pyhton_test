from re import search

def parse_cfg(filename):
    result = {}
    int_regex = '^interface (?P<interface>\S+)$'
    ip_regex = ' ip address (?P<ip>(?:\d{1,3}\.){3}\d{1,3}) (?P<mask>(?:\d{1,3}\.){3}\d{1,3})'
    with open(filename) as file:
        for line in file:
            capture_int = search(int_regex, line)
            capture_ip = search(ip_regex, line)
            if capture_int:
                interface = capture_int.group('interface')
            elif capture_ip and result.get(interface):
                result[interface].append(capture_ip.groups())
            elif capture_ip and not result.get(interface):
                result[interface] = []
                result[interface].append(capture_ip.groups())
    return result

if __name__ == '__main__':
    FILENAME = 'config_r2.txt'
    print(parse_cfg(FILENAME))
