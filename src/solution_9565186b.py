import numpy as np 

def solve(input):
  input_array = np.array(input)
  unique_code,count = np.unique(input_array, return_counts=True)
  code_count = dict(zip(unique_code,count))
  b = max(code_count, key = code_count.get)
  for input_lst in input_array:
    for j,lst_element in enumerate(input_lst):
      if (lst_element != b):
        input_lst[j] = 5
  print(input_array)
