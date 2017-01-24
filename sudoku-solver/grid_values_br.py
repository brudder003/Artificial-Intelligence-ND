from utils import *

def grid_values(grid):
    # In this function, you will take a sudoku as a string
    # and return a dictionary where the keys are the boxes,
    # for example 'A1', and the values are the digit at each
    # box (as a string) or '.' if the box has no value
    # assigned yet.

    chars = list(grid)

    assert len(chars) == 81

    dictionary = dict(zip(boxes, chars))
    return dictionary