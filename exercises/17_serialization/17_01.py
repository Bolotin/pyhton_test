import glob, re, csv
from re import search


def parse_sh_version(output):
    regex = 'Cisco IOS Software.*?Version (?P<ios>\S+),.*?uptime is (?P<uptime>\d+ days, \d+ hours, \d+ minutes).*?image file is "(?P<image>\S+)".*'
    capture = search(regex, output, re.DOTALL)
    if capture:
        return capture.group('ios'), capture.group('image'), capture.group('uptime')

def write_to_csv(filename, data):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

if __name__ == '__main__':
    FILES = glob.glob('sh_vers*')
    RESULT = 'routers_inventory.csv'
    NAMES = ['hostname', 'ios', 'image', 'uptime']
    data = [NAMES]
    for filename in FILES:
        hostname = search('sh_version_(\S+).txt',filename).group(1)
        with open(filename) as file:
            ios, image, uptime = parse_sh_version(file.read())
        data.append([hostname, ios, image, uptime])
    write_to_csv(RESULT, data)
    with open(RESULT) as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
