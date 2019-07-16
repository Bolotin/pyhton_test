from tabulate import tabulate
from itertools import zip_longest

def ip_table(available, unavailable):
    columns = ['available', 'unavailable']
    table = zip_longest(available, unavailable, fillvalue = '')
    print(tabulate(table, headers = columns))

if __name__ == '__main__':
    available = ['8.8.8.8', '192.168.100.1']
    unavailable = ['172.100.1.2', '10.42.13.13', '10.42.14.14', '10.42.154.11']
    ip_table(available, unavailable)
