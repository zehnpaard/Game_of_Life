#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Gui for Conway Game of Life
"""

from Tkinter import *
import ttk


class App():
    """ Main GUI class
    """
    def __init__(self, rows=70, cols=70, speed=100):
        self.root = Tk()
        mainframe = ttk.Frame(self.root)
        mainframe.grid(row=0, column=0, sticky=(N, W, S, E))

        self.active = False

        self.rows = rows
        self.cols = cols

        self.speed = speed

        # Create canvas to display game state and allow interactive edits
        self.canvas = BoardCanvas(mainframe, self)
        self.canvas.grid(row=0, column=0, rowspan=20, 
                sticky=(N, W, S, E))

        # Create button to activate/deactivate game
        self.activate_button = ActivateButton(mainframe, self)
        self.activate_button.grid(row=0, column=1, columnspan=2,
                sticky=(W, E))

        # Create entry box to set game speed
        self.speed_label = ttk.Label(mainframe)
        self.speed_label.configure(text="Tick Length (ms):")
        self.speed_label.grid(row=1, column=1, sticky=(N, W))
        self.speed_text = StringVar()
        self.speed_text.set(self.speed)

        self.speed_entry = ttk.Entry(mainframe)
        self.speed_entry.configure(textvariable=self.speed_text)
        self.speed_entry.grid(row=1, column=2, sticky=(N, W))

        # Display current generation count
        self.generation = 0
        self.gen_str = 'Generation #{0:6d}'
        self.gen_text = StringVar()
        self.gen_text.set(self.gen_str.format(self.generation))

        self.gen_label = ttk.Label(mainframe)
        self.gen_label.configure(textvariable=self.gen_text)
        self.gen_label.grid(row=2, column=1, columnspan=2,
                sticky=(N, W))


    def update_board_data(self):
        """ Callback to be used to update board data by one generation
        """
        pass

    def get_live_cell_data(self):
        """ Request to get a generator that yields all the coords of
        cells that are currently alive in the board data
        """
        pass

    def update_cell_in_board_data(self, row, col):
        """ 'Flip' the value of one cell in the board data representation
        such that a dead cell becomes alive, and an alive cell becomes
        dead.
        """
        pass

    def tick(self):
        """ If game state is active, update data by one generation,
        represent that on canvas, update generation count and show,
        and schedule another run of this function in the future
        """
        if self.active:
            self.update_board_data()
            self.canvas.clear_live()
            for row, col in self.get_live_cell_data():
                self.canvas.turn_cell_active(row, col)
            self.generation += 1
            self.gen_text.set(self.gen_str.format(self.generation))
            self.root.after(self.speed, self.tick)

    def run(self):
        """ Run the first tick (which will schedule further ticks if game
        state is active), and then run mainloop.
        """
        self.tick()
        self.root.mainloop()



class BoardCanvas(Canvas):
    """ Canvas widget to represent the game board graphically,
    and capture clicks to allow users to edit the state of the board
    if the game state is currently inactive.
    """
    def __init__(self, parent, app):
        Canvas.__init__(self, parent)
        self.app = app

        # Set canvas size
        self.width = 820
        self.height = 820
        self.configure(width=self.width, height=self.height)

        # Draw grid
        self.block = int((self.width - 20)/max(self.app.rows, self.app.cols))
        for i in xrange(self.app.rows+1):
            self.create_line(10,
                               10 + self.block * i, 
                               10 + self.block * (self.app.rows),
                               10 + self.block * i,
                               fill="grey")

        for i in xrange(self.app.cols+1):
            self.create_line(10 + self.block * i,
                               10,
                               10 + self.block * i,
                               10 + self.block * (self.app.cols),
                               fill="grey")



        self.bind("<Button-1>", self.update_clicked_cell)

    def update_clicked_cell(self, event):
        """If the user clicked within the grid when the game state is
        inactive, 'flip' both the canvas representation and the data 
        representation corresponding to the clicked cell (alive if dead, 
        dead if alive).
        If the user clicked outside the grid or the game state is active,
        do nothing.
        """
        if self.app.active or self.outside_range(event):
            return

        row, col = self.get_coord(event)
        if self.coords((row, col)):
            self.turn_cell_inactive(row, col)
        else:
            self.turn_cell_active(row, col)
        self.app.update_cell_in_board_data(row, col)

    def outside_range(self, event):
        """ Determine if the event occurred outside of the
        game board grid.
        """
        return event.x < 10 or event.x > self.width-10 or \
                event.y < 10 or event.y > self.height-10

    def get_coord(self, event):
        """ Convert the event's x,y to the row/col of the board
        """
        col, row = (event.x - 10) / self.block, (event.y - 10) / self.block
        return row, col

    def turn_cell_active(self, row, col):
        """ Color the specified square in the grid to red
        """
        self.create_rectangle(11 + self.block*col,
                              11 + self.block*row,
                              9  + self.block*(col+1),
                              9  + self.block*(row+1),
                              fill='red',
                              tag=((row, col),'live'))

    def turn_cell_inactive(self, row, col):
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
        self.app = app
        
        self.text = StringVar()
        self.text.set("Start")
        self.configure(textvariable=self.text)

        self.configure(command=self.switch_state)

    def switch_state(self):
        """ If current game state is not active, then activate.
        Otherwise deactivate.
        """
        if self.app.active:
            self.app.active = False
            self.text.set('Start')
        else:
            try:
                self.app.speed = int(self.app.speed_text.get())
            except ValueError:
                return
            self.app.active = True
            self.app.tick()
            self.text.set('Stop')


if __name__ == '__main__':
    pass
