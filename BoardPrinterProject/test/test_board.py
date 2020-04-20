import unittest
from BoardPrinterProject.src.board import Board


class TestBoard(unittest.TestCase):
    def test_make_board_list(self):
        a = Board("Hello", 4, 4, "x")
        list = a.make_board_list()
        self.assertEqual(list, [[" ", "0", "1", "2", "3"], ["0", "x", "x", "x", "x"], ["1", "x", "x", "x", "x"], ["2", "x", "x", "x", "x"], ["3", "x", "x", "x", "x"]] )

    def test_place_character(self):
        a = Board("Hello", 2, 2, "x")
        list = a.make_board_list()
        a.place_character("o", 1, 1)
        self.assertEqual(list[2][2], "o")

    def clear_character(self):
        a = Board("Hello", 3, 3, "o")
        list = a.make_board_list()
        a.place_character("x", 0, 0)
        a.clear_character(0,0)
        self.assertEqual(list[1][1], "o")




if __name__ == '__main__':
    unittest.main()
