import datetime


class simpleBacktrackingchess():
    def __init__(self, initaial_coords, n_cells) -> None:
        self.n_cells = n_cells
        self.chess_board = [
            [-1 for _ in range(n_cells)] for _ in range(n_cells)]
        print(self.chess_board)
        self.initial_pos = initaial_coords
        self.current_pos = initaial_coords
        # initiating the starting position into the chess_board
        self.chess_board[self.current_pos[0]][self.current_pos[1]] = 0
        print(self.initial_pos)
        self.all_possible_paths = [
            (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        # self.no_of_steps = (n_cells**2)
        # self.all_filled = False
        self.current_step = 0
        self.mover()
        print(self.chess_board)

    def invalid_Step_checker(self, step):
        if((self.current_pos[0]+step[0] < 0) or (self.current_pos[0]+step[0] > self.n_cells-1)):
            return False
        elif((self.current_pos[1]+step[1] < 0) or (self.current_pos[1]+step[1] > self.n_cells-1)):
            return False
        elif(self.chess_board[self.current_pos[0]+step[0]][self.current_pos[1]+step[1]] > -1):
            return False
        else:
            return True

    def mover(self):
        if(self.current_step >= self.n_cells**2-1):
            return True
        else:
            for x in self.all_possible_paths:
                if(self.invalid_Step_checker(x)):
                    # print(self.current_pos, x)
                    self.current_pos = (
                        self.current_pos[0]+x[0], self.current_pos[1]+x[1])
                    self.current_step += 1
                    # print(self.chess_board[self.current_pos[0]])
                    self.chess_board[self.current_pos[0]
                                     ][self.current_pos[1]] = self.current_step
                    if(self.mover() == False):
                        self.chess_board[self.current_pos[0]
                                         ][self.current_pos[1]] = -1
                        self.current_pos = (
                            self.current_pos[0]-x[0], self.current_pos[1]-x[1])
                        self.current_step -= 1
                        continue
                    else:
                        return True
                else:
                    continue
            # coming out of the loop means that there is no valid step left and the current step has not reached 64
            return False


i = int(input("enter the chess board size "))
start = datetime.datetime.now()
a = simpleBacktrackingchess((0, 0), i)
print(datetime.datetime.now()-start, ' time elasped')
