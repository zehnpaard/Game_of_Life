#!usr/bin/env python
# -*- coding: utf-8 -*-

""" Testing board creation, loading and updating
"""

import unittest
import board

class TestBoardFunctions(unittest.TestCase):

    def setUp(self):
        """ Creating constructs for loading
        """

        self.construct1 = [
                [1, 0, 0],
                [1, 1, 1],
                [1, 1, 0],
                [1, 0, 0],
                [1, 0, 0],
                ]

        self.construct2 = [
                [0, 0, 1],
                [1, 1, 1],
                ]


    def tearDown(self):
        """ Destroy constructs for next test
        """

        del self.construct1
        del self.construct2


    def test_create_board1(self):
        """ Test if the create_board function correctly sets up
        a 9x9 board initialized with 0 values.
        """

        sample_board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]

        self.assertEqual(sample_board, board.create_board(9, 9))


    def test_create_board2(self):
        """ Test if the create_board function correctly sets up
        a 7x5 board initialized with 0 values.
        """

        sample_board = [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                ]

        self.assertEqual(sample_board, board.create_board(5, 7))


    def test_load_construct1(self):
        """ Test the loading of construct1 to a 9x9 board, with top
        left set to (1, 2).
        """

        sample_board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]

        sample_empty_board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]

        board.load_construct(sample_empty_board, self.construct1, 1, 2)
        self.assertEqual(sample_board, sample_empty_board)


    def test_load_construct2(self):
        """ Test the loading of construct1 and construct2 to a 
        9x9 board, with top left set to (1, 2) and (3, 1).
        """

        sample_board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]

        sample_empty_board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]

        board.load_construct(sample_empty_board, self.construct1, 1, 2)
        board.load_construct(sample_empty_board, self.construct2, 3, 1)

        self.assertEqual(sample_board, sample_empty_board)


    def test_load_construct3(self):
        """ Test the loading of construct1 to a 9x9 board, with 
        top left set to (7, 5) - should return IndexError, as the
        construct will not fit into the board.
        """

        sample_empty_board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]

        self.assertRaises(IndexError, board.load_construct,
                sample_empty_board, self.construct1, 7, 5)
     
    
    def test_get_coords1(self):
        """ Get coordinates of construct 1
        """

        coords = [
                 (0, 0), 
              	 (1, 0), (1, 1), (1, 2), 
              	 (2, 0), (2, 1), 
              	 (3, 0),
              	 (4, 0),
                 ]

        self.assertEqual(coords, list(board.get_coords(self.construct1)))
    

    def test_get_coords2(self):
        """ Get coordinates of construct 2
        """

        coords = [
                 (0, 2), 
              	 (1, 0), (1, 1), (1, 2), 
                 ]

        self.assertEqual(coords, list(board.get_coords(self.construct2)))


    def test_next_board1(self):
        """ Takes initial state with a blinker, block and a lone straggler.
        Checks next_board function can generate the next state correctly.
        """

        sample_initial_board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]

        sample_next_board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]

        self.assertEqual(sample_next_board, board.next_board(sample_initial_board))


    def test_next_board2(self):
        """ Takes initial state with a glider, beacon and blinker next to
        the board edge.
        Checks next_board function can generate the next state correctly.
        """

        sample_initial_board = [
                [0, 0, 0, 0, 0, 0, 1, 1, 1],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 0],
                ]

        sample_next_board = [
                [0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 0],
                ]

        self.assertEqual(sample_next_board, board.next_board(sample_initial_board))

    def test_get_value(self):
        """ Check the get_value function returns the correct value
        if available, and IndexError if out of range.
        """

        sample_board = [
                [0, 0, 0, 0, 0, 0, 1, 1, 1],
                [0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 0, 0],
                ]

        self.assertEqual(1, board.get_value(sample_board, 0, 8))
        self.assertEqual(0, board.get_value(sample_board, 4, 4))
        self.assertRaises(IndexError, board.get_value,
                sample_board, 9, 1)

    def test_set_alive(self):
        """ Check the set_alive function updates the board correctly
        if the cell is available, and IndexError if out of range.
        """

        sample_board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]

        sample_empty_board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]


        self.assertEqual(sample_board, board.set_alive(sample_empty_board, 4, 7))
        self.assertRaises(IndexError, board.set_alive,
                sample_empty_board, 5, 11)

    def test_set_dead(self):
        """ Check the set_dead function updates the board correctly
        if the cell is available, and IndexError if out of range.
        """

        sample_board1 = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]

        sample_board2 = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                ]


        board.set_dead(sample_board1, 6, 6)
        board.set_dead(sample_board1, 4, 1)

        self.assertEqual(sample_board1, sample_board2)
        self.assertRaises(IndexError, board.set_dead, sample_board1, 9, 8)



if __name__ == '__main__':
    unittest.main()
