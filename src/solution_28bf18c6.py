# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:29:21 2019

@authors: Laura Gonzalez, Praneeth Jakkaraju, Tudor Chiribes

28bf18c6
"""

import sys
import json

def print_solution(json_input):
    """
    print the training grids and compute the solution for each one
    """
    
    for l in json_input['train']:
        for row in l['input']:
            print(row)
        print("")
        solution = solve(l['input'])
        if solution == l['output']:
            for row in solution:
                print(row)
        else:
            print("Solution is wrong!")
        print("")
            
    for l in json_input['test']:
        for row in l['input']:
            print(row)
        print("")
        solution = solve(l['input'])
        if solution == l['output']:
            for row in solution:
                print(row)
        else:
            print("Solution is wrong!")
        print("")

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
    # read path to JSON file from command line arguments
    file_path = str(sys.argv[1])
    
    # open the file containing the data
    input_file = open(file_path)
    
    # relative path for development
    #input_file = open('../data/training/28bf18c6.json')
    
    # load the input as a JSON array
    json_input = json.load(input_file)
    
    # visualise the task demonstration
    print_solution(json_input)
