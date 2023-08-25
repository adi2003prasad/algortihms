class maze():
    def __init__(self, n, input_all_points) -> None:
        ''' the points table will be a [[]*x axis]*y axis
        i.e input_all_points will have 0 for all the points we cannot go 
        and 1 for the path we can take 
        '''
        self.n = n
        self.board = input_all_points
        self.destination = (0, self.n-1)
        self.start = (0, 0)
        self.validMoves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.currentPos = self.start
        self.board[self.currentPos[0]][self.currentPos[1]] = 2
        self.mover()
        print(self.board)

    def checkValid_move(self, step):
        if((self.currentPos[0]+step[0] < 0) or (self.currentPos[0]+step[0] > self.n-1) or (self.currentPos[1]+step[1] < 0) or (self.currentPos[1]+step[1] > self.n-1)):
            return False
        elif(self.board[self.currentPos[0]+step[0]][self.currentPos[1]+step[1]] == 0):
            return False
        elif(self.board[self.currentPos[0]+step[0]][self.currentPos[1]+step[1]] == 2):
            return False
        else:
            return True

    def mover(self):
        if(self.currentPos == self.destination):
            return True
        else:
            for x in self.validMoves:
                if(self.checkValid_move(x) == False):
                    continue
                else:
                    self.currentPos = (
                        self.currentPos[0]+x[0], self.currentPos[1]+x[1])
                    self.board[self.currentPos[0]][self.currentPos[1]] = 2
                    if(self.mover() == False):
                        self.board[self.currentPos[0]][self.currentPos[1]] = 1
                        self.currentPos = (
                            self.currentPos[0]-x[0], self.currentPos[1]-x[1])
                        continue
                    else:
                        return True
            return False


maze_q = [[1, 0, 0, 0, 1],
          [1, 0, 0, 1, 1],
          [1, 0, 1, 1, 0],
          [1, 1, 1, 1, 0],
          [0, 0, 0, 0, 0]]
ratInMaze = maze(5, maze_q)
