# place your BoardsManager class in this file
from BoardPrinterProject.src.board import Board
class BoardsManager(Board):
    def __init__(self, title: str, rows: int, columns: int, character: str) -> None:
        super().__init__(title, rows, columns, character)
        self.list_of_boards = []
        self.title_lists = []
        self.active = None
    def initialize_board(self):
        first_board = Board(self.title, self.rows, self.columns, self.character)
        first_board.make_board_list()
        self.list_of_boards = [first_board] + self.list_of_boards
        self.active = self.list_of_boards[0]
        self.title_lists.append(self.title)

    def create_board(self):
        new_board_name = input("Enter the name of your board: ")
        new_num_rows = int(input("Enter the number of rows for your board: "))
        new_num_columns = int(input("Enter the number of columns for your board: "))
        new_character = input("Enter the blank character to be used on your board: ")
        creation = Board(new_board_name, new_num_rows, new_num_columns, new_character)
        creation.make_board_list()
        self.list_of_boards = [creation] + self.list_of_boards
        self.title_lists.insert(0, new_board_name)

    def switch_board(self):
        for pos,item in enumerate(self.title_lists):
            print(str(pos) + "." + " " + item)
        board_choice = int(input("Enter the number of the board you want to switch to: "))
        for pos,item in enumerate(self.list_of_boards):
            if pos == board_choice:
                self.active = self.list_of_boards[board_choice]



    def add_character(self):
        character = input("Enter the character you want to add to the board: ")
        position_choice = input("Enter the position to place the character in the form row,col: ")
        position = position_choice.split(",")
        for word in position:
            word = word.strip()
        row = int(position[0])
        column = int(position[1])
        self.active.place_character(character, row, column)

    def erase_character(self):
        position_choice = input("Enter the position you want to erase in the form row, col: ")
        position = position_choice.split(",")
        for word in position:
            word = word.strip()
        row = int(position[0])
        column = int(position[1])
        self.active.clear_character(row, column)

    def terminate(self):
        exit()



    


