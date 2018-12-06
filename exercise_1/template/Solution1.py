import sys
import numpy as np


def solve_task1(input_matrix):
	# Enter your code here.
	# Return the minimum cost or return No path found!
    return ""


# Use as many helper functions as you like


# Get input from command prompt and run the program
input_arg = sys.argv[1]
def run_program(file_name = input_arg):
    # Read the input matrix
    input_matrix = np.genfromtxt(file_name, dtype='str')
    
    # Your main function to solve the matrix
    print(solve_task1(input_matrix))


run_program()

# To test the result yourself,
# Open the command line tool, navigate to the folder and execute:
# python Solution1.py input_for_task1.txt


