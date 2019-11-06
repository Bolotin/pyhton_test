import re
from pprint import pprint

def parse_sh_cdp_neighbors(data):
    dev_reg = '(?P<device>\S+)>'
    neigh_reg = '(?P<neighbor>\S+)\s+(?P<local_int>\w+\s?[\d/]+)\s+\d+\s+.*?\d\s+(?P<neighbor_int>\w+\s?[\d/]+)'
    device = re.search(dev_reg, data).group('device')
    result = {device:{}}
    capture = re.finditer(neigh_reg, data)
    for item in capture:
        neighbor, local_int, neighbor_int = item.groups()
        result[device].update({local_int : {neighbor: neighbor_int}})
    return result

if __name__ == '__main__':
    FILENAME = 'sh_cdp_n_sw1.txt'
    with open(FILENAME) as file:
        data = file.read()
        pprint(parse_sh_cdp_neighbors(data))
