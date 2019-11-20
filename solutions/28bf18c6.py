# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:29:21 2019

@author: chiribest

28bf18c6
"""

import json

input_file = open('../data/training/28bf18c6.json')
json_input = json.load(input_file)

for l in json_input['train']:
    print("the input:")
    for row in l['input']:
        print(row)
    print("the output:")
    for row in l['output']:
        print(row)

for l in json_input['test']:
    print("the input:")
    for row in l['input']:
        print(row)
    print("the output:")
    for row in l['output']:
        print(row)
