"""
Created on Sun Nov 24 22:35:30 2019

@author: Laura Gonzalez, Praneeth Jakkaraju, Tudor Chiribes
"""

import numpy as np
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


def solve(input):
    # convert the input to numpy array
    input_array = np.array(input)
    # get the count of cells with color code
    unique_code,count = np.unique(input_array, return_counts=True)
    # making a dictionary of color code and count of cells with color
    code_count = dict(zip(unique_code,count))
    # get the maximum count of cells colored same
    max_occured_code = max(code_count, key = code_count.get)
    # enumerate through input array
    for input_lst in input_array:
        for j,lst_element in enumerate(input_lst):
            """check if each cell is not colored the selected color code
            and replace it with color code 5"""
            if (lst_element != max_occured_code):
                input_lst[j] = 5
    return input_array.tolist()


if __name__ == "__main__":
    # read path to JSON file from command line arguments
    file_path = str(sys.argv[1])

    # open the file containing the data
    input_file = open(file_path)

    # relative path for development
    # input_file = open('../data/training/9565186b.json')

    # load the input as a JSON array
    json_input = json.load(input_file)

    # visualise the task demonstration
    print_solution(json_input)
