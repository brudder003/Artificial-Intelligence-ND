from Utils import *

__author__ = 'brudder'


class UtilsViz:
    def check(self):

        board1 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
        board2 = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
        board_choice = int(input("Enter 1 for easy, 2 for hard, 3 for manual entry: "))

        if board_choice == 1:
            board_ind = board1
        elif board_choice == 2:
            board_ind = board2
        else:
            board_ind = str(input('board '))

        values = grid_values(board_ind)
        print("\n LAYOUT OF THE INPUT BOARD: ")
        display(values)

        values = eliminate(values)
        print('\n LAYOUT AFTER ELIMINATE: ')
        display(values)

        values = only_choice(values)
        print('\n LAYOUT AFTER ONLY CHOICE: ')
        display(values)

        values = grid_values(board_ind)
        values = reduce_puzzle(values)
        print('\n LAYOUT AFTER BOARD REDUCE: ')
        display(values)

        values = grid_values(board_ind)
        values = search(values)
        print('\n LAYOUT AFTER SEARCH: ')
        display(values)

UtilsViz().check()
