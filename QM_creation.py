# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 09:09:27 2023

@author: Ahmad Al Musawi
"""
import json
qm_name = int(input('Enter sequence of QM?'))
NoN = int(input('Enter number of nodes?'))
QM = []
for i in range(NoN):
    node = {}
    node['name'] = input('enter name of the node? ')
    node['Node_ID'] = int(input('enter Node_ID?'))
    node['feature'] = ''
    node["success_features"] = []
    node["fail_features"] = []
    node["yes_child"] = int(input('enter target node_ID on Yes branch?(pass:99, fail:100, exclude:101)'))
    node["no_child"]  = int(input('enter target node_ID on No branch?(pass:99, fail:100, exclude:101)'))

    print(f'here is your new node: \n{node}\n')
    QM.append(node)


with open(f'QM{qm_name}.json', 'w') as json_file:
    json.dump(QM, json_file)