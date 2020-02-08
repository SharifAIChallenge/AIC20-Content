class ConnectFour(object):
    """ Tic-Tac Toe Board 
        
        Board is represented through a board object, send the clumn number:

          0   1   2   3   4   5   6
        +---+---+---+---+---+---+---+
	|   |   |   |   |   |   |   |
	+---+---+---+---+---+---+---+
	|   |   |   |   |   |   |   |
	+---+---+---+---+---+---+---+
	|   |   |   |   |   |   |   |
	+---+---+---+---+---+---+---+
	|   |   |   |   |   |   |   |
	+---+---+---+---+---+---+---+
	|   |   |   |   |   |   |   |
	+---+---+---+---+---+---+---+
	|   |   |   |   |   |   |   |
	+---+---+---+---+---+---+---+ 
    """
    #static class variables - shared across all instances
    HEIGHT = 6
    WIDTH = 7

    def __init__(self):
        self.legal_players = ["X","O"]
        self.board = [[] for x in range(self.WIDTH)]
        self.numMoves = 0
        self.lastMove = None
        return

    #copy a new board
    def copy(self):
        new_board = self.__class__()
        new_board.board = [row[:] for row in self.board]
        return new_board
    
    # Puts a piece in the appropriate column and checks to see if it was a winning move
    # Pieces are either 1 or 0; automatically decided
    def move(self, column, turn):
        # update board data
        self.numMoves += 1
        self.board[column].append(turn)

    def get_moves(self):
        return [i for i in range(self.WIDTH) if len(self.board[i])<self.HEIGHT]

    # Returns:
    #  -1 if game is not over
    #   0 if the game is a draw
    #   1 if player 1 wins
    #   2 if player 2 wins
    def isTerminal(self):
        for i in range(0,self.WIDTH):
            for j in range(0,self.HEIGHT):
                try:
                    if self.board[i][j]  == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if self.board[i][j]  == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if not j + 3 > self.HEIGHT and self.board[i][j] == self.board[i+1][j + 1] == self.board[i+2][j + 2] == self.board[i+3][j + 3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass

                try:
                    if not j - 3 < 0 and self.board[i][j] == self.board[i+1][j - 1] == self.board[i+2][j - 2] == self.board[i+3][j - 3]:
                        return self.board[i][j] + 1
                except IndexError:
                    pass
        if self.numMoves == 42:
            return 0
        return -1

    # Prints out a visual representation of the board
    # X's are 1's and 0's are 0s
    def print(self):
        print("")
        print("+" + "---+" * self.WIDTH)
        for rowNum in range(self.HEIGHT - 1, -1, -1):
            row = "|"
            for colNum in range(self.WIDTH):
                if len(self.board[colNum]) > rowNum:
                    row += " " + ('X' if self.board[colNum][rowNum] else 'O') + " |"
                else:
                    row += "   |"
            print(row)
            print("+" + "---+" * self.WIDTH)
        try:
            print(self.lastMove[1])
        except:
            pass
        print(self.numMoves)

    def score_game(self):
        heur = 0
        state = self.board
        for i in range(0, self.WIDTH):
            for j in range(0, self.HEIGHT):
                # check horizontal streaks
                try:
                    # add player one streak scores to heur
                    if state[i][j] == state[i + 1][j] == 0:
                        heur += 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == 0:
                        heur += 100
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == 0:
                        heur += 10000

                    # subtract player two streak score to heur
                    if state[i][j] == state[i + 1][j] == 1:
                        heur -= 10
                    if state[i][j] == state[i + 1][j] == state[i + 2][j] == 1:
                        heur -= 100
                    if state[i][j] == state[i+1][j] == state[i+2][j] == state[i+3][j] == 1:
                        heur -= 10000
                except IndexError:
                    pass

                # check vertical streaks
                try:
                    # add player one vertical streaks to heur
                    if state[i][j] == state[i][j + 1] == 0:
                        heur += 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == 0:
                        heur += 100
                    if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == 0:
                        heur += 10000

                    # subtract player two streaks from heur
                    if state[i][j] == state[i][j + 1] == 1:
                        heur -= 10
                    if state[i][j] == state[i][j + 1] == state[i][j + 2] == 1:
                        heur -= 100
                    if state[i][j] == state[i][j+1] == state[i][j+2] == state[i][j+3] == 1:
                        heur -= 10000
                except IndexError:
                    pass

                # check positive diagonal streaks
                try:
                    # add player one streaks to heur
                    if not j + 3 > self.HEIGHT and state[i][j] == state[i + 1][j + 1] == 0:
                        heur += 100
                    if not j + 3 > self.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == 0:
                        heur += 100
                    if not j + 3 > self.HEIGHT and state[i][j] == state[i+1][j + 1] == state[i+2][j + 2] \
                            == state[i+3][j + 3] == 0:
                        heur += 10000

                    # add player two streaks to heur
                    if not j + 3 > self.HEIGHT and state[i][j] == state[i + 1][j + 1] == 1:
                        heur -= 100
                    if not j + 3 > self.HEIGHT and state[i][j] == state[i + 1][j + 1] == state[i + 2][j + 2] == 1:
                        heur -= 100
                    if not j + 3 > self.HEIGHT and state[i][j] == state[i+1][j + 1] == state[i+2][j + 2] \
                            == state[i+3][j + 3] == 1:
                        heur -= 10000
                except IndexError:
                    pass

                # check negative diagonal streaks
                try:
                    # add  player one streaks
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == 0:
                        heur += 10
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == 0:
                        heur += 100
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] \
                            == state[i+3][j - 3] == 0:
                        heur += 10000

                    # subtract player two streaks
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == 1:
                        heur -= 10
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] == 1:
                        heur -= 100
                    if not j - 3 < 0 and state[i][j] == state[i+1][j - 1] == state[i+2][j - 2] \
                            == state[i+3][j - 3] == 1:
                        heur -= 10000
                except IndexError:
                    pass
        return heur

