from Utils import *

__author__ = 'brudder'


class UtilsCheck:
    def check(self):

        board1 = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
        board_choice = int(input("Enter 1 for default board, 2 to enter your own: "))
        print(board_choice)

        if board_choice == 1:
            board = board1
        else:
            board = str(input('board '))

        values = grid_values(board)
        print("\n LAYOUT OF THE INPUT BOARD: ")
        display(values)

        values = eliminate(values)
        print('\n LAYOUT AFTER ELIMINATE: ')
        display(values)



UtilsCheck().check()
