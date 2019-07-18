import re

filename = 'HWC001.txt'
dest_filename = './tmp/HWC001_data.txt'
with open(filename, 'r') as file, open(dest_filename,'w') as dest_file:
    for line in file:
        regex = '^(?P<AP_ID>\d+\s+(?P<AP_MAC>\w{4}-\w{4}-\w{4})\s+(?P<AP_NAME>\S+)\s+(?P<AP_GROUP>\S+)\s+(?P<AP_ADDRESS>(\d{1,3}\.){3}\d{1,3}))'
        search = re.search(regex, line)
        if search:
            print('{:15} {:30} {:15}'.format(*search.group('AP_MAC', 'AP_NAME', 'AP_ADDRESS')))
            dest_file.write('{}, {}, {} \n'.format(*search.group('AP_NAME','AP_MAC','AP_ADDRESS')))
