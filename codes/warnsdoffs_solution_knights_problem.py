import datetime


class warnsdoffChess():
    def __init__(self, n, start) -> None:
        self.n = n
        self.currentPos = start
        self.chessBoard = [[-1 for _ in range(self.n)] for _ in range(self.n)]
        self.all_possible_paths = [
            (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
        self.chessBoard[self.currentPos[0]][self.currentPos[1]] = 0
        self.currentMove = 0
        self.totalUnfilled = self.n**2-1
        self.warnsdoff_mover()
        print(self.chessBoard)

    def degreeFinder(self, point):
        count = 0
        for x in self.all_possible_paths:
            if((point[0]+x[0] < 0) or (point[0]+x[0] > self.n-1) or (point[1]+x[1] < 0) or (point[1]+x[1] > self.n-1)):
                continue
            else:
                if(self.chessBoard[point[0]+x[0]][point[1]+x[1]] == -1):
                    count += 1
                else:
                    continue

        return count

    def shouldIMove(self, point):
        # print(self.chessBoard)
        a = []
        for x in self.all_possible_paths:
            if((point[0]+x[0] < 0) or (point[0]+x[0] > self.n-1)):
                a.append(10000000)
                continue
            elif((point[1]+x[1] < 0) or (point[1]+x[1] > self.n-1)):
                a.append(10000000)
                continue
            elif(self.chessBoard[point[0]+x[0]][point[1]+x[1]] > -1):
                a.append(10000000)
                continue
            else:

                new_point = (point[0]+x[0], point[1]+x[1])
                a.append(self.degreeFinder(new_point))
        # print(a)
        if(min(a) == 10000000):
            return (-1, -1)
        else:
            while True:
                # print(a)
                if(len(a) == 0):
                    return (-1, -1)
                min_val = a.index(min(a))
                a.pop(min_val)
                if(self.chessBoard[point[0]+self.all_possible_paths[min_val][0]][point[1]+self.all_possible_paths[min_val][1]] == -1):
                    ai = self.all_possible_paths[min_val]
                    # print(ai)
                    return ai
                else:
                    continue

    def warnsdoff_mover(self):
        if((self.currentMove == self.n**2-1) and (self.totalUnfilled == 0)):
            return True
        else:
            x = self.shouldIMove(self.currentPos)
            if(x == (-1, -1)):
                return False
            else:
                self.currentPos = (
                    self.currentPos[0]+x[0], self.currentPos[1]+x[1])
                self.currentMove += 1
                self.chessBoard[self.currentPos[0]
                                ][self.currentPos[1]] = self.currentMove
                self.totalUnfilled -= 1

                if(self.warnsdoff_mover() == False):
                    self.chessBoard[self.currentPos[0] -
                                    x[0]][self.currentPos[1]-x[1]] = -1
                    self.currentPos = (
                        self.currentPos[0]-x[0], self.currentPos[1]-x[1])
                    self.currentMove -= 1
                    self.totalUnfilled += 1

                else:
                    return True


start = datetime.datetime.now()
a = int(input("enter the size of chess board "))
warnsdoffChess(a, (0, 4))
print('elapsed time for warnsdoff solution ', datetime.datetime.now()-start)
