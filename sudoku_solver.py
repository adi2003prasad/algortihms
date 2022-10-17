class sudoku():
    '''
    A simple sudoku solver using backtracking algorithm'''

    def __init__(self, puzzle, size) -> None:
        self.sudoku_board = puzzle
        self.sudoku_size = size
        self.current_row = 0
        self.current_collumn = 0
        print('Starting all possible combination check ')
        self.sudoku_solver()
        [print(x) for x in self.sudoku_board]

    def isSafe(self, num_to_check):
        for x in range(0, self.sudoku_size):
            # checking whether in the same row
            if(self.sudoku_board[self.current_row][x] == num_to_check):
                return False
            # checking whether in the same column
            if(self.sudoku_board[x][self.current_collumn] == num_to_check):
                return False
        # for checking whether in same grid 3x3
        for row in range(self.current_row-self.current_row % 3, self.current_row+(3-self.current_row % 3)):
            for column in range(self.current_collumn-self.current_collumn % 3, self.current_collumn+(3-self.current_collumn % 3)):
                if(self.sudoku_board[row][column] == num_to_check):
                    return False
        return True

    def comparator(self):
        # increases the count to the next cell to validate
        if(self.current_collumn == self.sudoku_size-1):
            self.current_row += 1
            self.current_collumn = 0

        else:
            self.current_collumn += 1

    def sudoku_solver(self):
        # print(self.current_row, self.current_row)
        # print("going through current sudoku")
        # [print(x) for x in self.sudoku_board]
        if(self.current_row == self.sudoku_size):
            # checking whether we are at the end of the sudoku
            return True
        else:
            # so we are not at end of file
            # checking if the current cell is already solved
            if(self.sudoku_board[self.current_row][self.current_collumn] > 0):
                # if so then just go to the next cell
                self.comparator()
                return self.sudoku_solver()
            else:
                # so we need to solve for this block
                # looping from all possible value of the sudoku board
                for x in range(1, self.sudoku_size+1):
                    if(self.isSafe(x) == True):
                        # if it's safe then just append the value to the board
                        self.sudoku_board[self.current_row][self.current_collumn] = x
                        # and go to the next cell
                        self.comparator()
                        # but if at the end of recursion we get false then just backtrack to this cell
                        if(self.sudoku_solver() == False):
                            # backtracking
                            self.sudoku_board[self.current_row][self.current_collumn] = 0
                            if(self.current_collumn == 0):
                                self.current_collumn = self.sudoku_size-1
                                self.current_row -= 1
                            else:
                                self.current_collumn -= 1
                            # now test the other possible value
                            continue
                        else:
                            return True
                    else:
                        continue
                # coming out of the loop means that there was no possible value for the cell that means our combination was not right so we send a false which will start the backtracking
                return False


# test grid
a = 9
grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]
obj = sudoku(grid, a)
