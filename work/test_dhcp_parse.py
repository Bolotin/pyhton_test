import csv

FILENAME = 'AP_Location_19_07_2019.xlsx'
with open(FILENAME, encoding = 'cp1251') as file:
    for line in file:
        print(line)
