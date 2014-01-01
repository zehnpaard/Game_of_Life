#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

""" Implements functions related to the creation, loading and updating
of the game board.
"""

def create_board(row_count, col_count):
    """ Creates a board representation, row_count x col_count, with 
    each cell initialized to 0.
    """
    return [[0]*col_count for x in xrange(row_count)]


def load_construct(board, construct, top_row=0, left_col=0):
    """ Takes each live cell in construct and loads to board, setting
    the top left based on the coordinates entered.
    """
    max_row, max_col = len(board), len(board[0])
    con_row, con_col = len(construct), len(construct[0])
    if max_row < con_row + top_row or max_col < con_col + left_col:
        raise IndexError

    for row, col in get_coords(construct):
        board[row+top_row][col+left_col] = 1


def get_coords(construct):
    """ Takes construct and yields the coord of each live cell
    """
    for i, row in enumerate(construct):
        for j, cell in enumerate(row):
            if cell:
                yield (i, j)

def next_board(board):
    """ Takes current board and returns new board with the next generation
    state, based on the following rules:
    1) If cell is alive, remains alive if 2 or 3 surrounding cells are alive,
    else the cell dies.
    2) If cell is dead, becomes alive if 3 surrounding cells are alive
    Surrounding cells are defined as the 8 cells horizontally, vertically 
    and diagonally adjacent.
    Edges of the board are treated as "dead".
    """
    max_row, max_col = len(board), len(board[0])
    new_board = create_board(max_row, max_col)

    coords = itertools.product(xrange(max_row), xrange(max_col))
    for cell_row, cell_col in coords:
        surrounding_alive = sum_neighbors(cell_row, cell_col, board)
        if board[cell_row][cell_col]:
            if surrounding_alive in (2, 3):
                new_board[cell_row][cell_col] = 1
        else:
            if surrounding_alive == 3:
                new_board[cell_row][cell_col] = 1

    return new_board

def sum_neighbors(cell_row, cell_col, board):
    """ Return sum of values of the 8 surrounding neighbors of a cell.
    Same as the number of alive neighbors of the cell.
    """
    max_row, max_col = len(board), len(board[0])

    valid_coords = ((i, j) for i in valid_range(cell_row, max_row)
                           for j in valid_range(cell_col, max_col))

    neighbor_vals = (board[row][col] for row, col in valid_coords)
    return sum(neighbor_vals) - board[cell_row][cell_col]


def valid_range(cell_index, side_count):
    """ Returns an xrange object that yields upto 9 cells, offset by
    -1 and 1 for each dimension, except where that hits against the
    borders of the board, in which case the valid neighbors is truncated.
    """
    return xrange(max(0, cell_index-1), min(cell_index+2, side_count)) 

def get_value(board, row, col):
    """ Get value of cell
    """
    pass

def set_alive(board, row, col):
    """ Set value of cell to alive
    """
    pass

def set_dead(board, row, col):
    """ Set value of cell to dead
    """
    pass


def main():
    pass

if __name__ == '__main__':
    main()

