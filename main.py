from BoardPrinterProject.src.boards_manager import BoardsManager
def main():
    board_name = input("Enter the name of your board: ")
    num_rows = int(input("Enter the number of rows for your board: "))
    num_columns = int(input("Enter the number of columns for your board: "))
    character = input("Enter the blank character to be used on your board: ")
    self_name = BoardsManager(board_name, num_rows, num_columns, character)
    self_name.initialize_board()
    print(repr(self_name.active))
    while True:
        print("Select your action from the list below.")
        print("1. Fill Spot")
        print("2. Erase Spot")
        print("3. Switch Board")
        print("4. Create Board")
        print("5. Quit")
        print("")
        choice = input("Enter the number of the action you would like to do: ")

        if choice == "1":
            self_name.add_character()


        if choice == "2":
            self_name.erase_character()

        if choice == "3":
            self_name.switch_board()

        if choice == "4":
            self_name.create_board()

        if choice == "5":
            self_name.terminate()

        print(repr(self_name.active))




if __name__ == '__main__':
    main()
