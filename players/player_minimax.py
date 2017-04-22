#!/usr/bin/env python
# Four spaces as indentation [no tabs]

from player import Player
from util import *
from itertools import tee
# ==========================================
# Player Minimax
# ==========================================

class MinimaxPlayer(Player):

    # ------------------------------------------
    # Initialize
    # ------------------------------------------

    def __init__(self, symbol):
        super(MinimaxPlayer, self).__init__(symbol)
        self._possibilities = []

    # ------------------------------------------
    # Get next move
    # ------------------------------------------

    def get_next_move(self, board):

        # TODO Here you will implement the Minimax algorithm.
        # This method may return the best movement based on Minimax score
        # for the current board.

        # If you want, you can use here some helper functions:
        #
        # - find_winner(board): This method checks if someone wins in the
        #   parametrized board and return a tuple (Winner, Winner movement).
        #
        # - find_empty_cells(board): This method checks if there are available
        #   moves in the parametrized board. It returns an array containing
        #   the available moves.
        #
        # - print_board(board): This method helps you debugging your code.
        #   It prints a board filled with the executed moves.
        #   WARNING: printing can slow your code. Use it just for debug.
        #
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

        
    def min(self, board, level, move):
        level = level +1
        result = self.terminal_test(board,level)
        if result != None :
            return [result, move]
        else:
            n_min = [32768,0]
            for next_movement in self.successors(board,self.opp()):
                aux_min = self.max(next_movement[1], level, next_movement[0])
                if aux_min[0] < n_min[0]:
                    aux_min[1] = next_movement[0]
                    n_min = aux_min
            return n_min

    def max(self, board, level, move):
        leve = level +1
        result = self.terminal_test(board,level)
        if result != None :
            return [result, move]
        else:
            n_max = [-32768, 0]
            for next_movement in self.successors(board, self.me()):
                aux_max = self.min(next_movement[1], level, next_movement[0])
                if aux_max[0] > n_max[0]:
                    aux_max[1] = next_movement[0]
                    n_max = aux_max
            return n_max
    def min_max(self, board):
        level = 0
        result = self.max(board,level, 0)
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