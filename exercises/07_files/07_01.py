template = '''
Protocol:              OSPF
Prefix:                {}
AD/Metric:             {}
Next-Hop:              {}
Last update:           {}
Outbound Interface:    {}
'''

with open('ospf.txt','r') as file:
    for line in file:
        line = line.strip().split()
        line[4] = line[4].strip(',')
        line[5] = line[5].strip(',')
        line.pop(3)
        line[2] = line[2].strip('[]')
        line.pop(0)
        print(template.format(*line))
        print(line)
