# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 22:35:30 2019

@author: Laura Gonzalez, Praneeth Jakkaraju, Tudor Chiribes
"""
import numpy as np

def solve(t):
    arr = np.array(t)
    midvalue = int(len(arr.diagonal()) / 2 )
    filler = arr.diagonal()[midvalue]
    np.fill_diagonal(arr,filler)
    np.fill_diagonal(np.fliplr(arr),filler)
    print(arr)