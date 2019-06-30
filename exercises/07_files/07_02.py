from sys import argv

file_name = argv[1]
with open(file_name,'r') as file:
    for line in file:
        if not line.startswith('!'):
            print(line.rstrip())
