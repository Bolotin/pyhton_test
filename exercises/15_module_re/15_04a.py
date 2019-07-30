from exercise_15_04 import parse_sh_ip_int_br
from pprint import pprint

def convert_to_dict(names, data):
    result = []
    for line in data:
        result.append({name:item for name,item in zip(names,line)})
    return result

if __name__ == '__main__':
    NAMES = ['interface', 'status', 'protocol', 'ip']
    FILENAME = 'sh_ip_int_br.txt'
    data = parse_sh_ip_int_br(FILENAME)
    pprint(convert_to_dict(NAMES, data))
