"""
Clone of 2048 game.
Online version(python 2.6):
"""
__author__ = 'dare7'
try:
    import poc_2048_gui
except ImportError:
    import ext.poc_2048_gui as poc_2048_gui
try:
    import poc_simpletest
except ImportError:
    import ext.poc_simpletest as poc_simpletest
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # local variables
    zero_shift = []
    number_merge = []
    result = []
    blank = 0
    cache = 0

    # initializing blank list
    for idx in range(len(line)):
        number_merge.append(0)

    # shifting zeroes in initial list
    for val in line:
        if val != 0:
            zero_shift.append(val)
        else:
            blank += 1

    for idx in range(blank):
        zero_shift.append(0)

    # merging values in shifted list
    for idx, val in enumerate(zero_shift):
        #print("cache:", cache, "value:", val, "index:", idx, "shift_list", zero_shift, "merge_list", number_merge)
        if val == cache and val != 0:
            number_merge[idx-1] = val*2
            number_merge[idx] = 0
            cache = 0
        else:
            number_merge[idx] = val
            cache = val

    # shifting zeroes in merged list
    blank = 0
    for val in number_merge:
        if val != 0:
            result.append(val)
        else:
            blank += 1

    for idx in range(blank):
        result.append(0)

    return result

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self.grid_height = grid_height
        self.grid_width = grid_width
        self.cells = [[0 for col in range(self.grid_width)] for row in range(self.grid_height)]
        self.move_dir = []
        for col in range(self.grid_width):
            for row in range(self.grid_height):
                self.move_dir = []


    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self.cells = [[0 for col in range(self.grid_width)] for row in range(self.grid_height)]
        self.new_tile()
        self.new_tile()
        return self.cells

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self.cells)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self.grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self.grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        #self.cells = [[0 for col in range(self.grid_width)] for row in range(self.grid_height)]
        col = random.randrange(0,self.grid_width)
        row = random.randrange(0,self.grid_height)
        chance = random.randrange(0,10)
        if any(0 in sublist for sublist in self.cells):
            if self.cells[row][col] == 0:
                if chance == 9:
                    self.cells[row][col] = 4
                else:
                    self.cells[row][col] = 2
            else:
                col = random.randrange(0,self.grid_width)
                row = random.randrange(0,self.grid_height)
        else:
            print("no empty tiles")
        return self.cells

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self.cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self.cells[row][col]

if __name__ == "__main__":
    # tests
    #print("should return [4, 4, 0, 0]",merge([2, 0, 2, 4]))
    #print("should return [4, 0, 0, 0]",merge([0, 0, 2, 2]))
    #print("should return [4, 0, 0, 0]",merge([2, 2, 0, 0]))
    #print("should return [4, 4, 2, 0, 0]",merge([2, 2, 2, 2, 2]))
    #print("should return [8, 32, 8, 0]",merge([8, 16, 16, 8]))
    #poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
    field = TwentyFortyEight(3, 5)
    test = poc_simpletest.TestSuite()
    test.run_test(field.new_tile(), "[[2, 2, 0, 2, 0], [0, 0, 0, 0, 2], [0, 2, 2, 0, 0]]", "test1")
    test.report_results()
    #field.reset()
    field.new_tile()
    field.new_tile()
    field.new_tile()
    field.new_tile()
    field.new_tile()
    field.new_tile()
    field.reset()
    print(field.cells)