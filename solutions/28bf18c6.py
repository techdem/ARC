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

def test_solve(result, json_input):
    """
    test output of solve()
    """
    return result == json_input['test'][0]['output']

def solve(t):
    """
    receive the input part of the testing data and
    determine the output
    """
    
    # find the 3x3 grid with the highest sum
    c = 0
    m = 0
    g = [[]]
    
    for i in range(len(t)-2):
        for j in range(len(t)-2):
            c = t[i][j] + t[i][j+1] + t[i][j+2] +\
                t[i+1][j] + t[i+1][j+1] + t[i+1][j+2] +\
                t[i+2][j] + t[i+2][j+1] + t[i+2][j+2]
            
            if c > m:
                m = c
                g = [[t[i][j],t[i][j+1],t[i][j+2],t[i][j],t[i][j+1],t[i][j+2]],
                     [t[i+1][j],t[i+1][j+1],t[i+1][j+2],t[i+1][j],t[i+1][j+1],t[i+1][j+2]],
                     [t[i+2][j],t[i+2][j+1],t[i+2][j+2],t[i+2][j],t[i+2][j+1],t[i+2][j+2]]]
            
    return g

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
    print("\nThe result of solve() is: {0}".format(test_solve(result, json_input)))
    