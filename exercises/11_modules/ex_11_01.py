def parse_cdp_neighbors(data):
    result = {}
    for line in data.split('\n'):
        if '>' in line:
            device = line.strip().split('>')[0]
            print(device)
        elif 'Eth' in line:
            line = line.strip().split()
            neighbor = line[0]
            local_int = line[1] + line[2]
            neighbor_int = line[-2] + line[-1]
            result[(device,local_int)] = (neighbor,neighbor_int)
    return result

# Main script
if __name__ == '__main__':
    filename = 'sh_cdp_n_r3.txt'
    with open(filename,'r') as file:
        data = file.read()
        print(parse_cdp_neighbors(data))
