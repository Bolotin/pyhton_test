from ex_11_01 import parse_cdp_neighbors
from draw_network_graph import draw_topology
from pprint import pprint

filenames = ['sh_cdp_n_sw1.txt','sh_cdp_n_r1.txt','sh_cdp_n_r2.txt','sh_cdp_n_r3.txt']

data = {}
for filename in filenames:
    with open(filename,'r') as file:
        data.update(parse_cdp_neighbors(file.read()))

keys = list(data.keys())

for key in keys:
    if key in data.values():
        del(data[key])

draw_topology(data,'test')
