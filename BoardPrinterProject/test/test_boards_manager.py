import unittest
from unittest.mock import patch
from BoardPrinterProject.src.boards_manager import BoardsManager


class TestBoardsManager(unittest.TestCase):
    def test_initialize_board(self):
        a = BoardsManager("Hello", 3, 3, "x")
        a.initialize_board()
        self.assertEqual(a.title_lists[0], "Hello")
        self.assertEqual("Hello", str(a.active))

    def test_create_board(self):
        user_input = ["Board_title", 5, 3, "|"]
        with patch('BoardPrinterProject.src.boards_manager.input', side_effect=user_input):
            a = BoardsManager("Hi", 4,4, "O")
            a.initialize_board()
            a.create_board()
            self.assertEqual(a.title_lists[0], "Board_title")
            self.assertEqual("Hi", str(a.active))

    def test_switch_board(self):
        user_input = ["Board_title", 5, 3, "|", 0]
        with patch('BoardPrinterProject.src.boards_manager.input', side_effect=user_input):
            a = BoardsManager("Hi", 4, 4, "O")
            a.initialize_board()
            a.create_board()
            a.switch_board()
            self.assertEqual("Board_title", str(a.active))

    def test_add_character(self):
        user_input = ["x", "1,1"]
        with patch('BoardPrinterProject.src.boards_manager.input', side_effect=user_input):
            a = BoardsManager("Hi", 4, 4, "O")
            a.initialize_board()
            a.add_character()
            self.assertEqual("x",a.active.board_list[2][2])

    def test_erase_character(self):
        user_input = ["x", "1,1", "1,1"]
        with patch('BoardPrinterProject.src.boards_manager.input', side_effect=user_input):
            a = BoardsManager("Hi", 4, 4, "O")
            a.initialize_board()
            a.add_character()
            a.erase_character()
            self.assertEqual("O", a.active.board_list[2][2])

if __name__ == '__main__':
    unittest.main()
