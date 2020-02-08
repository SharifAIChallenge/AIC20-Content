class TicTacToe:
    """ Tic-Tac Toe Board 
        
        Board is represented through a board object
        
        1 ¦ 2 ¦ 3
        --+---+--
        4 ¦ 5 ¦ 6
        --+---+--
        7 ¦ 8 ¦ 9
    """
    def __init__(self):
        self.spaces = 9
        self.blank = " "
        self.legal_players = ["X","O"]
        self.base =      " {} ¦ {} ¦ {} \n" + \
                          "---+---+--- \n" + \
                         " {} ¦ {} ¦ {} \n" + \
                          "---+---+--- \n" + \
                         " {} ¦ {} ¦ {} \n" 
        self.winning = [[0,1,2], # top horizontal
                        [3,4,5], # middle horizontal
                        [6,7,8], # bottom horizontal
                        [0,3,6], # left vertical
                        [1,4,7], # middle vertical
                        [2,5,8], # right vertical
                        [0,4,8], # diagonal \
                        [2,4,6]  # diagonal /
                       ]
        self.reset()
    
    def reset(self):
        """ Resets the board """
        self.board = [" "] * self.spaces

    def __str__(self):
        """ String representation of a game """
        return self.base.format(*self.board)
    
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.board == other.board
        return False

    def __hash__(self):
        return hash("".join(self.board))
    
    def copy(self):
        """ Creates a copy of the game object """
        new_board = self.__class__()
        new_board.board = self.board[:]
        return new_board
        
    def get_moves(self):
        """ Returns open moves on the board """
        return [idx + 1 for idx, player in enumerate(self.board) if player == self.blank]
    
    def move(self, player, move):
        """ Updates the board based on player and move 
            
            example: 
                game.move("X", 4)                
        """
        player = player.upper()
        assert move in self.get_moves(), "Illegal move"
        assert player in self.legal_players, "Illegal player"
        self.board[move - 1] = player
        
    def gameover(self):
        """ Returns whether there are any legal moves left """
        return len(self.get_moves()) == 0 or self.winner() is not None
    
    def winner(self):
        """ Returns the winner of a game, 'Draw' or None if game is ongoing """
        for winner in self.winning:
            players = [self.board[pos] for pos in winner]
            s_players = set(players)
            if len(s_players) == 1 and self.blank not in s_players:
                return players[0]
        
        if self.blank not in set(self.board):
            return "Draw"

    def score_game(self):
        winner = self.winner()
        if winner == "X":
            return 1
        elif winner == "O":
            return -1
        return 0

