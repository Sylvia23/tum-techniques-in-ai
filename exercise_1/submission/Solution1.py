import sys
import numpy as np
import heapq


debug_on = False


def debug(*argv):
    if debug_on:
        for arg in argv:
            print(arg)


def get_allowed_moves():
    # Format: (vertical move, horizontal move, cost)
    return [(1, 0, 6), (1, -1, 10), (0, -1, 5), (-1, -1, 10), (-1, 0, 6), (-1, 1, 10), (0, 1, 5), (1, 1, 10)]


def find_source_and_dest(input_matrix):
    source = None
    dest = None
    for row_idx, row in enumerate(input_matrix):
        for col_idx, value in enumerate(row):
            if value == 'R':
                source = (row_idx, col_idx)
            if value == 'X':
                dest = (row_idx, col_idx)
    return (source, dest)


def is_move_allowed(input_matrix, next_node):
    height, width = input_matrix.shape
    row, col = next_node
    if col < 0 or row < 0:
        return False
    if col >= width or row >= height:
        return False
    if input_matrix[row][col] == '*':
        return False
    return True


def calculate_cost(input_matrix, source, dest):
    if source is None or dest is None:
        return 'No path found!'

    moves = get_allowed_moves()

    visited = {}
    pq = []
    heapq.heappush(pq, (0, source))
    while True:
        if len(pq) == 0:
            return 'No path found!'
        cur_node_dist, cur_node = heapq.heappop(pq)
        visited[cur_node] = True
        debug(cur_node, cur_node_dist)
        if cur_node == dest:
            return cur_node_dist
        for move in moves:
            next_node = (cur_node[0] + move[0], cur_node[1] + move[1])
            if next_node in visited:
                continue
            if is_move_allowed(input_matrix, next_node) == False:
                continue
            heapq.heappush(pq, (cur_node_dist+move[2], next_node))
    return 'No path found!'


def solve_task1(input_matrix):
	# Enter your code here.
	# Return the minimum cost or return No path found!
    
    # Find the source and destination
    source, dest = find_source_and_dest(input_matrix)
    debug(source, dest)

    cost = calculate_cost(input_matrix, source, dest)
    
    return cost

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


