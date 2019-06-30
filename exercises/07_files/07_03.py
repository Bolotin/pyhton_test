file_name = 'CAM_table.txt'
data = {}
vlans = []

with open(file_name, 'r') as file:
    for line in file:
        line = line.strip().split()
        if line:
            if line[0].isdigit():
                line.pop(2)
                vlans.append(int(line[0]))
                data[line[0]] = line

vlans.sort()
for vlan in vlans:
    print(data[str(vlan)])
