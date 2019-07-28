from sys import argv
from re import search

filename, regex = argv[1:]

with open(filename,'r') as file:
    for line in file:
        if search(regex, line):
            print(line.strip())
