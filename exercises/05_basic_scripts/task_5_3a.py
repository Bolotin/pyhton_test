# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]
templates = {'trunk':trunk_template, 'access': access_template}
dialogs = {'trunk': 'Input permited VLANs: ', 'access': 'Input the VLAN: '}

interface_type = input('Input interface type: ')
interface_name = input('Input interface name: ')
vlan = input(dialogs.get(interface_type))

result = ['interface {}'.format(interface_name)]
result += templates.get(interface_type)
result = '\n'.join(result).format(vlan)

print(result)
