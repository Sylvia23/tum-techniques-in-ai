import sys
import numpy as np


# Use as many helper functions as you like


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def is_allowed(input_matrix, r, c):
    height, width = input_matrix.shape
    if r < 0 or c < 0 or r >= height or c >= width:
        return False
    if input_matrix[r][c] != '.':
        return False
    return True


def fill(input_matrix, r, c, visited):
    visited[r][c] = 1
    for direction in DIRECTIONS:
        next_r = r + direction[0]
        next_c = c + direction[1]
        if is_allowed(input_matrix, next_r, next_c) and visited[next_r][next_c] == 0:
            fill(input_matrix, next_r, next_c, visited)


def solve_task2(input_matrix):
	# Enter your code here.
    height, width = input_matrix.shape
    visited = np.zeros_like(input_matrix, dtype=int)
    
    # Start finding dots from bordering rows and columns
    for i in range(height):
        if visited[i][0] == 0 and input_matrix[i][0] == '.':
            fill(input_matrix, i, 0, visited)
        if visited[i][width-1] == 0 and input_matrix[i][width-1] == '.':
            fill(input_matrix, i, width-1, visited)
    
    for i in range(width):
        if visited[0][i] == 0 and input_matrix[0][i] == '.':
            fill(input_matrix, 0, i, visited)
        if visited[height-1][i] == 0 and input_matrix[height-1][i] == '.':
            fill(input_matrix, height-1, i, visited)

    # Fill up connected dots with X which are not open to border
    for i in range(height):
        for j in range(width):
            if visited[i][j] == 0 and input_matrix[i][j] == '.':
                input_matrix[i][j] = 'X'

    return input_matrix


# Get input from command prompt and run the program
input_arg = sys.argv[1]
def run_program(filename = input_arg):
    # Read the input matrix
    input_matrix = np.genfromtxt(filename, dtype='str')
    
    # Your main function to solve the matrix
    output = solve_task2(input_matrix)

    # print the matrix to a txt file
    np.savetxt('output_for_task2.txt', output, fmt="%s")


run_program()


# To test the result yourself,
# Open the command line tool, navigate to the folder and execute:
# python Solution2.py input_for_task2.txt
