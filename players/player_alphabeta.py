#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from player import Player
from util import *

# ==========================================
# Player Alphabeta
# ==========================================

class AlphabetaPlayer(Player):

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, symbol):
        super(AlphabetaPlayer, self).__init__(symbol)
        self._possibilities = []

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):
        # TODO Bonus
        self._possibilities = []
        return self.min_max(board)

    def score(self, winner,level):
        if winner == self.me():
            return 10-level
        elif winner == self.opp():
            return level-10
        else:
            return 0

    def successors(self, board, mark):
        for cell in self._possibilities:
            cp = board[:]
            cp[cell] = mark
            yield cell,cp

        
    def min(self, board, level, move,alpha,beta):
        level = level +1
        result = self.terminal_test(board,level)
        if result != None :
            return [result, move]
        else:
            n_min = [32768,0]
            for next_movement in self.successors(board,self.opp()):
                aux_min = self.max(next_movement[1], level, next_movement[0], alpha, beta)
                if aux_min[0] < n_min[0]:
                    aux_min[1] = next_movement[0]
                    n_min = aux_min
                if alpha is not None and aux_min[0] <= alpha:
                    return aux_min
                if beta is None or aux_min[0] < beta:
                        beta = aux_min[0]
            return n_min

    def max(self, board, level, move, alpha, beta):
        leve = level +1
        result = self.terminal_test(board,level)
        if result != None :
            return [result, move]
        else:
            n_max = [-32768, 0]
            for next_movement in self.successors(board, self.me()):
                aux_max = self.min(next_movement[1], level, next_movement[0], alpha, beta)
                if aux_max[0] > n_max[0]:
                    aux_max[1] = next_movement[0]
                    n_max = aux_max
                if beta is not None and aux_max[0] >= beta:
                    return aux_max
 
                if alpha is None and aux_max[0] > alpha:
                    alpha = aux_max[0]
            return n_max
            
    def min_max(self, board):
        self._possibilities = find_empty_cells(board)
        level = 0
        result = self.max(board,level, 0,None, None)
        return result[1]

    def terminal_test(self, board,level):
        self._possibilities = find_empty_cells(board)
        winner, move_sequence = find_winner(board)
        if winner != None :
            return self.score(winner,level)
        elif self._possibilities == []:
            return 0
        else:
            return None