# -*- coding: utf-8 -*-
'''
Задание 17.2c

С помощью функции draw_topology из файла draw_network_graph.py
сгенерировать топологию, которая соответствует описанию в файле topology.yaml

Обратите внимание на то, какой формат данных ожидает функция draw_topology.
Описание топологии из файла topology.yaml нужно преобразовать соответствующим образом,
чтобы использовать функцию draw_topology.

Для решения задания можно создать любые вспомогательные функции.

Не копировать код функции draw_topology.

В итоге, должно быть сгенерировано изображение топологии.
Результат должен выглядеть так же, как схема в файле task_10_2c_topology.svg

При этом:
* Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

'''
from draw_network_graph import draw_topology
from pprint import pprint
import yaml

if __name__ == '__main__':
    topology = {}
    topology_filename = 'topology.yaml'
    with open(topology_filename) as f:
        topology_yaml = yaml.load(f)
    for host, data in topology_yaml.items():
        for local_interface, neighbor_data in data.items():
            neighbor = tuple(neighbor_data.keys())[0]
            neighbor_interface = tuple(neighbor_data.values())[0]
            topology.update({(host, local_interface): (neighbor, neighbor_interface)})
    pprint(topology)
    draw_topology(topology, 'img/my_test_topology')
