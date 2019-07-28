from re import search

def parse_cfg(filename):
    result = []
    regex = '^ip address (?P<address>(?:\d{1,3}\.){3}\d{1,3}) (?P<mask>(?:\d{1,3}\.){3}\d{1,3})'
    with open(filename) as file:
        for line in file:
            capture = search(regex, line.strip())
            if capture:
                result.append(capture.groups())
    return result


if __name__ == '__main__':
    FILENAME = 'config_r1.txt'
    print(parse_cfg(FILENAME))
