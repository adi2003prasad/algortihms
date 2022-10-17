class chess():
    def __init__(self, n) -> None:
        self.n = n
        self.chess_board = [[0 for _ in range(self.n)] for _ in range(self.n)]
        self.current_col = 0
        # because there can only be one queen in one row
        self.data_rows = [0 for _ in range(self.n)]
        self.placer()
        [print(x) for x in self.chess_board]

    def isSafe(self, coordinates):
        # print(self.data_rows)
        list_of_all_possiblities = [(-1, -1), (0, -1), (+1, -1)]
        for x in list_of_all_possiblities:
            if((coordinates[0]+x[0] < 0) or (coordinates[0]+x[0] > self.n-1) or (coordinates[1]+x[1] < 0)):
                continue
            else:

                if(self.chess_board[coordinates[0]+x[0]][coordinates[1]+x[1]] == 1):
                    return False
                elif(self.data_rows[coordinates[0]] == 1):
                    return False
                else:
                    continue
        return True

    def placer(self):
        if(self.current_col == self.n):
            return True
        else:
            for x in range(self.n):
                if(self.isSafe((x, self.current_col)) == False):
                    continue
                else:
                    self.chess_board[x][self.current_col] = 1
                    self.current_col += 1
                    self.data_rows[x] = 1
                    if(self.placer() == False):
                        self.current_col -= 1
                        self.chess_board[x][self.current_col] = 0
                        self.data_rows[x] = 0
                        continue
                    else:
                        return True
            return False


a = int(input(""))
obj = chess(a)
