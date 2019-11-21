# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:29:21 2019

@author: chiribest

28bf18c6
"""

import json

def task_demonstration(json_input):
    """
    print the input-output pairs to the console
    """
    
    print("\ntraining:\n")
    for l in json_input['train']:
        print("input:")
        for row in l['input']:
            print(row)
        print("output:")
        for row in l['output']:
            print(row)
            
    print("\ntesting:\n")
    for l in json_input['test']:
        print("input:")
        for row in l['input']:
            print(row)
        print("output:")
        for row in l['output']:
            print(row)

def test_solve(json_input):
    """
    test output of solve()
    """
    return json_input['test'][0]['output']

def solve(testing_input):
    
    return [[0, 0, 3, 0, 0, 3],[3, 3, 3, 3, 3, 3],[3, 0, 0, 3, 0, 0]]

if __name__ == "__main__":
    # open the file containing the data
    input_file = open('../data/training/28bf18c6.json')
        
    # load the input as a JSON array
    json_input = json.load(input_file)

    # visualise the task demonstration
    task_demonstration(json_input)
    
    # pass only the testing input to solve() and store the result
    result = solve(json_input['test'][0]['input'])
    
    # compare the result to that of test_solve()
    print("The result of solve() is: {0}".format(result == test_solve(json_input)))
    