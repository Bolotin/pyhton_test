import re
from pprint import pprint

def parse_cfg(filename):
    result = {}
    regex = (
    'interface\s+(?P<interface>\S+)'
    '[^!]*?'
    'ip address (?P<address>(?:\d{1,3}\.){3}\d{1,3}) (?P<mask>(?:\d{1,3}\.){3}\d{1,3})'
    )
    with open(filename) as file:
        data = file.read()
        capture = re.finditer(regex, data, re.DOTALL)
        for item in capture:
            interface, address, mask = item.groups()
            result[interface] = (address, mask)
    return result

if __name__ == '__main__':
    FILENAME = 'config_r1.txt'
    pprint(parse_cfg(FILENAME))
