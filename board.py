#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

def main():
    pass

if __name__ == '__main__':
    main()

