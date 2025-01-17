# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 09:29:21 2019

@authors: Laura Gonzalez, Praneeth Jakkaraju, Tudor Chiribes

28bf18c6
"""

import sys
import json
from print_solution import print_solution

def solve(t):
    """
    receive the input part of the testing data and
    determine the output
    """
    
    # declare and initialise variables
    current = 0
    highest = 0
    grid = [[]]
    
    # iterate over the input and find the 3x3 grid with the highest sum
    for i in range(len(t)-2):
        for j in range(len(t)-2):
            # compute the total sum of the grid starting from current element
            current = t[i][j] + t[i][j+1] + t[i][j+2] +\
                t[i+1][j] + t[i+1][j+1] + t[i+1][j+2] +\
                t[i+2][j] + t[i+2][j+1] + t[i+2][j+2]
            
            if current > highest:
                highest = current
                
                # generate the 3x6 output grid to match the identified pattern
                grid = [[t[i][j],t[i][j+1],t[i][j+2],t[i][j],t[i][j+1],t[i][j+2]],
                     [t[i+1][j],t[i+1][j+1],t[i+1][j+2],t[i+1][j],t[i+1][j+1],t[i+1][j+2]],
                     [t[i+2][j],t[i+2][j+1],t[i+2][j+2],t[i+2][j],t[i+2][j+1],t[i+2][j+2]]]
            
    return grid

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
    print_solution(json_input, solve)
