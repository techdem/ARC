# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:35:30 2019

@author: Laura Gonzalez, Praneeth Jakkaraju, Tudor Chiribes
"""
import numpy as np

def solve(t):
    input_array = np.array(t) # converting the input to array 
    midvalue = int(len(input_array.diagonal()) / 2 ) # calculating the middle value
    fill_with_color = input_array.diagonal()[midvalue] # select the color 
    np.fill_diagonal(input_array,fill_with_color) # filling with selected color 
    np.fill_diagonal(np.fliplr(input_array),fill_with_color) 
    return input_array.tolist() # convert back to a list of lists