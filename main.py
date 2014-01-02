#!usr/bin/env python
# -*- coding: utf-8 -*-

""" Runs entire application, gluing together the game
logic held under the board.py module and the display
and loop logic held under gui.py module
"""

import board
import gui

SIDE = 80

# global variable
game_board = board.create_board(SIDE, SIDE)

def main():
    app = gui.App(SIDE, SIDE)

    # Implement the "update_cell_in_board_data",
    # "update_board_data" and "get_live_cell_data" functions
    # required by the gui, using the global game_board and
    # functions contained in board.py.
    # Once created, insert into the App object created.
    def update_cell(row, col):
        """ 'Flip' the value in cell on the board data
        """
        global game_board
        if board.get_value(game_board, row, col):
            board.set_dead(game_board, row, col)
        else:
            board.set_alive(game_board, row, col)
    app.update_cell_in_board_data = update_cell

    def update_board_data():
        """ Update the game board data by one generation
        """
        global game_board
        game_board = board.next_board(game_board)
    app.update_board_data = update_board_data

    def get_live_cell_data():
        """ Return a generator with the coordinates of all
        live cells in the game_board.
        """
        global game_board
        return board.get_coords(game_board)
    app.get_live_cell_data = get_live_cell_data

    # Run mainloop
    app.run()




if __name__ == '__main__':
    main()
