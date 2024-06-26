import sys

import numpy as np

import Board
import algorithms as alg

if __name__ == '__main__':
    strategy = sys.argv[1]
    additional_parameter = sys.argv[2]
    input_filename = 'layouts/' + sys.argv[3]
    with open(input_filename, 'r') as input_file:
        input_file_contents_str = input_file.read().split()

    input_file_contents_int = [int(x) for x in input_file_contents_str]
    height = input_file_contents_int[0]
    width = input_file_contents_int[1]
    original_layout = np.array(input_file_contents_int[2:], dtype=int).reshape((height, width))
    original_board = Board.Board(original_layout)
    if strategy == 'bfs':
        alg.bfs(additional_parameter, original_board)
    elif strategy == 'dfs':
        alg.dfs(additional_parameter, original_board)
    elif strategy == 'astr':
        if additional_parameter == 'manh':
            alg.a_star_manhattan(original_board)
        elif additional_parameter == 'hamm':
            alg.a_star_hamming(original_board)
        else:
            print("Invalid additional parameter")
    else:
        print('Invalid strategy')
