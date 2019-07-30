from re import search

def parse_sh_ip_int_br(filename):
    result = []
    regex = '^(?P<Interface>\S+)\s+(?P<IP>\S+)\s+\w+\s+\w+\s+(?P<Status>.*?)\s+(?P<Protocol>up|down)$'
    with open(filename) as file:
        for line in file:
            capture = search(regex, line, )
            if capture:
                result.append(capture.groups())
    return result

if __name__ == '__main__':
    FILENAME = 'sh_ip_int_br.txt'
    for line in parse_sh_ip_int_br(FILENAME):
        print(line)
