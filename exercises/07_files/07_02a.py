from sys import argv

file_name = argv[1]

ignore = ['duplex', 'alias', 'Current configuration']

with open(file_name, 'r') as file:
    for line in file:
        if not line.startswith('!'):
            for item in ignore:
                if item in line:
                    break
            else:
                print(line.rstrip())
