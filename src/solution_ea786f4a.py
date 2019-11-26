# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:35:30 2019

@author: Laura Gonzalez, Praneeth Jakkaraju, Tudor Chiribes
"""
import numpy as np
import json
import sys

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
    input_array = np.array(t) # converting the input to array 
    midvalue = int(len(input_array.diagonal()) / 2 ) # calculating the middle value
    fill_with_color = input_array.diagonal()[midvalue] # select the color 
    np.fill_diagonal(input_array,fill_with_color) # filling with selected color 
    np.fill_diagonal(np.fliplr(input_array),fill_with_color) 
    return input_array.tolist() # convert back to a list of lists


if __name__ == "__main__":
    # read path to JSON file from command line arguments
    file_path = str(sys.argv[1])

    # open the file containing the data
    input_file = open(file_path)

    # relative path for development
    # input_file = open('../data/training/ea786f4a.json')

    # load the input as a JSON array
    json_input = json.load(input_file)

    # visualise the task demonstration
    print_solution(json_input)
