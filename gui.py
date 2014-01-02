#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Gui for Conway Game of Life
"""

from Tkinter import *
import ttk


class GuiApp(ttk.Frame):
    """ Main GUI class that inherits from ttk.Frame
    """
    def __init__(self, app,
                canvas_rows, canvas_cols, speed, generation):
        ttk.Frame.__init__(self, app.root)

        self._app = app

        # Create canvas to display game state and allow interactive edits
        self.canvas = BoardCanvas(self, self._app, 
                canvas_rows, canvas_cols)
        self.canvas.grid(row=0, column=0, rowspan=20, 
                sticky=(N, W, S, E))

        # Create button to activate/deactivate game
        self.activate_button = ActivateButton(self, self._app)
        self.activate_button.grid(row=0, column=1, columnspan=2,
                sticky=(W, E))

        # Create entry box to set game speed
        self.speed_label = ttk.Label(self)
        self.speed_label.configure(text="Tick Length (ms):")
        self.speed_label.grid(row=1, column=1, sticky=(N, W))

        self.speed_text = StringVar()
        self.speed_text.set(speed)

        self.speed_entry = ttk.Entry(self)
        self.speed_entry.configure(textvariable=self.speed_text)
        self.speed_entry.grid(row=1, column=2, sticky=(N, W))

        # Display current generation count
        self.gen_str = 'Generation #{0:6d}'
        self.gen_text = StringVar()
        self.update_generation_display(generation)

        self.gen_label = ttk.Label(self)
        self.gen_label.configure(textvariable=self.gen_text)
        self.gen_label.grid(row=2, column=1, columnspan=2,
                sticky=(N, W))

    def update_generation_display(self, generation):
        self.gen_text.set(self.gen_str.format(generation))



class BoardCanvas(Canvas):
    """ Canvas widget to represent the game board graphically,
    and capture clicks to allow users to edit the state of the board
    if the game state is currently inactive.
    """
    def __init__(self, parent, app, rows, cols):
        Canvas.__init__(self, parent)
        self._app = app
        self._rows = rows
        self._cols = cols

        # Set canvas size
        self._size = 820
        self.configure(width=self._size, height=self._size)

        # Draw grid
        self._block = int((self._size - 20)/max(self._rows, self._cols))
        for i in xrange(self._rows+1):
            self.create_line(10,
                               10 + self._block * i, 
                               10 + self._block * (self._rows),
                               10 + self._block * i,
                               fill="grey")

        for i in xrange(self._cols+1):
            self.create_line(10 + self._block * i,
                               10,
                               10 + self._block * i,
                               10 + self._block * (self._cols),
                               fill="grey")


        self.bind("<Button-1>", self._update_clicked_cell)

    # Private methods

    def _update_clicked_cell(self, event):
        """If the user clicked within the grid when the game state is
        inactive, 'flip' both the canvas representation and the data 
        representation corresponding to the clicked cell (alive if dead, 
        dead if alive).
        If the user clicked outside the grid or the game state is active,
        do nothing.
        """
        if self._app.is_active() or not self._inside_range(event):
            return

        row, col = self._get_coord(event)
        if self.coords((row, col)):     # coords method inherited from Canvas
            self.display_cell_as_dead(row, col)
        else:
            self.display_cell_as_alive(row, col)
        self._app.update_cell_in_board_data(row, col)


    def _inside_range(self, event):
        """ Determine if the event occurred within game board grid.
        """
        return 10 <= event.x < (self._size-11) and \
               10 <= event.y < (self._size-11)


    def _get_coord(self, event):
        """ Convert the event's x,y to the row/col of the board
        """
        col, row = (event.x - 10) / self._block, (event.y - 10) / self._block
        return row, col


    # Public methods

    def display_cell_as_alive(self, row, col):
        """ Color the specified square in the grid to red
        """
        self.create_rectangle(11 + self._block*col,
                              11 + self._block*row,
                              9  + self._block*(col+1),
                              9  + self._block*(row+1),
                              fill='red',
                              tag=((row, col),'live'))


    def display_cell_as_dead(self, row, col):
        """ Uncolor the specified square in the grid
        """
        self.delete((row, col))


    def clear_live(self):
        """ Clear all live cells on grid
        """
        self.delete('live')



class ActivateButton(ttk.Button):
    """ Button to allow users to start/stop the passing of
    generations in the game.
    """
    def __init__(self, parent, app):
        ttk.Button.__init__(self, parent)
        self._app = app
        
        self._text = StringVar()
        self._text.set("Start")
        self.configure(textvariable=self._text)

        self.configure(command=self._switch_state)

    # Private method

    def _switch_state(self):
        """ If current game state is not active, then activate.
        Otherwise deactivate.
        """
        if self._app.is_active():
            self._app.deactivate_game()
            self._text.set('Start')
        else:
            try:
                self._app.activate_game()
            except ValueError:
                return
            self._text.set('Stop')


if __name__ == '__main__':
    pass
