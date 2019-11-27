def print_solution(json_input, solve):
    """
    print the training grids and compute the solution for each one
    """
    
    # iterate over the contents of 'train'
    for l in json_input['train']:
        # each list represent a row of the grid
        for row in l['input']:
            print(row)
        print("")
        # compute the output using the solve method
        solution = solve(l['input'])
        # if the result of solve() matches the original output, print
        if solution == l['output']:
            for row in solution:
                print(row)
        else:
            print("Solution is wrong!")
        print("")
    
    # repeat above process for the contents of 'test'
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