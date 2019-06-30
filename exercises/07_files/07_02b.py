from sys import argv

source_file, destination_file = argv[1:]
ignore = ['duplex', 'alias', 'Current configuration']

with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
    for line in source:
        for item in ignore:
            if item in line:
                break
        else:
            destination.write(line)

with open(destination_file,'r') as file:
    for line in file:
        print(line.strip())
