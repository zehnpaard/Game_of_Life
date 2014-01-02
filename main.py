#!usr/bin/env python
# -*- coding: utf-8 -*-

""" Runs entire application, gluing together the game
logic held under the board.py module and the display
and loop logic held under gui.py module
"""

import Tkinter
import board
import gui



class App(object):
    """ Main application handling event loop and
    gluing together the board logic and GUI display.
    """
    def __init__(self, rows, cols, speed):
        self.root = Tkinter.Tk()

        self._rows = rows
        self._cols = cols

        self._speed = speed 

        self._generation = 0
        self._active = False


        self._game_board = board.create_board(self._rows, self._cols)
        self._gui = gui.GuiApp(self,
                canvas_rows=self._rows, canvas_cols=self._cols, 
                speed=self._speed, generation=self._generation)
        self._gui.pack()


    def _tick(self):
        """ If game state is active:
        1) update data by one generation,
        2) represent that on gui canvas,
        3) update generation count and display, and
        4) schedule another run of this function in the future
        If game state is not active, do nothing
        """
        if self._active:
            self._game_board = board.next_board(self._game_board)


            self._gui.canvas.clear_live()
            for row, col in board.get_coords(self._game_board):
                self._gui.canvas.display_cell_as_alive(row, col)


            self._generation += 1
            self._gui.update_generation_display(self._generation)

            self.root.after(self._speed, self._tick)


    def update_cell_in_board_data(self, row, col):
        """ 'Flip' the value in cell on the board data
        """
        if board.get_value(self._game_board, row, col):
            board.set_dead(self._game_board, row, col)
        else:
            board.set_alive(self._game_board, row, col)

    def activate_game(self):
        """ 1) Set the game speed to match the entry,
        2) make the game state active, and
        3) run the next tick (which will then schedule the 
        next tick by itself.
        If inputted game speed is not valid, raise an Error
        """
        try:
            self._speed = int(self._gui.speed_text.get())
        except ValueError:
            raise ValueError
        self._active = True
        self._tick()

    def deactivate_game(self):
        self._active = False

    def is_active(self):
        return self._active


    def run(self):
        """ Run the first tick (which will schedule further ticks if game
        state is active), and then run mainloop.
        """
        self._tick()
        self.root.mainloop()


def main():
    app = App(rows=80, cols=80, speed=100)
    app.run()



if __name__ == '__main__':
    main()
