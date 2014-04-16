from config import BLACK, WHITE, EMPTY
import ast

"""
evaluator.py - Tian Zheng - GAOthello
CS 480 Truman State University
This is the evaluator that returns heuristics for Minimax Algorithm.
The other part of the game is based on Humberto Henrique Campos Pinheiro's
othello game on GitHub.
"""

class Evaluator(object):    
    WIPEOUT_SCORE = 1000    #a move that results a player losing all pieces
    
    def get_location_weight( self, deltaBoard ):
        """
        This is the method that read current move on the board, get the
        weight of current location, and add it to the heuristics.
        """
        # Read in weight and construct board
        f = open("input.txt", "r+")
        weightString = f.readline()
        weightArray = ast.literal_eval(weightString)
        weightBoard = [ [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0], \
                       [0,0,0,0,0,0,0,0] ]

        for i in range(0,4):
            for j in range(0,4):
                weightBoard[i][j] = weightArray[4*i+(j+1)-1]
        for i in range(0,4):
            for j in range(4,8):
                weightBoard[i][j] = weightArray[4*i+(8-j)-1]
        for i in range(4,8):
            for j in range(0,4):
                weightBoard[i][j] = weightArray[4*(7-i)+(j+1)-1]
        for i in range(4,8):
            for j in range(4,8):
                weightBoard[i][j] = weightArray[4*(7-i)+(8-j)-1]

        # Get piece location and add weight to score
        myScore = 0
        yourScore = 0
        for i in range(7):
            for j in range(7):
                if deltaBoard.board[i][j] == self.player:
                    myScore += weightBoard[i][j]
                elif deltaBoard.board[i][j] == self.enemy:
                    yourScore += weightBoard[i][j]         
        
        return (myScore-yourScore)

    def score( self, startBoard, board, currentDepth, player, opponent ):
        """ Determine the score of the given board for the specified player.
        - startBoard the board before any move is made
        - board the board to score
        - currentDepth depth of this leaf in the game tree
        - searchDepth depth used for searches.
        - player current player's color
        - opponent opponent's color
        """
        self.player = player
        self.enemy = opponent
        sc = 0
        whites, blacks, empty = board.count_stones()
        deltaBoard = board.compare( startBoard )        
        deltaCount = sum( deltaBoard.count_stones() )
        
        # Check wipe out
        if (self.player == WHITE and whites == 0) or (self.player == BLACK and blacks == 0):
            return -Evaluator.WIPEOUT_SCORE
        if (self.enemy == WHITE and whites == 0) or (self.enemy == BLACK and blacks == 0):
            return Evaluator.WIPEOUT_SCORE
        
        sc += self.get_location_weight( deltaBoard )

        return sc