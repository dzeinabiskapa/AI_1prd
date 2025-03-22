import random
from minimax_algo import MinimaxAI
class gameLogic:
    
    def __init__(self, update_ui):
        self.sequence = []
        self.scores = [0,0]
        self.player_turn = 0
        self.update_ui = update_ui

    def start_game(self, sequence_length):
        self.sequence = self.sequence_generation(sequence_length)
        self.scores = [0, 0]
        self.player_turn = 0
        self.update_ui(self.sequence, self.scores, self.player_turn)
        
    def sequence_generation(self, sequence_len):
        return random.choices([1,2,3,4], k = sequence_len)
    
    def take_number(self, i):
        if 0 <= i < len(self.sequence):
            self.scores[self.player_turn] += self.sequence.pop(i)
            self.switch_turn()
    
    def split_number(self, i):
        if 0 <= i < len(self.sequence):
            if self.sequence[i] == 2:
                self.sequence[i:i+1] = [1,1]
            elif self.sequence[i] == 4:
                self.sequence[i:i+1] = [2,2]
                self.scores[self.player_turn] += 1
            else:
                return False
            self.switch_turn()
            return True
        return False
              
    def switch_turn(self):
        self.player_turn = 1 - self.player_turn
        self.update_ui(self.sequence, self.scores, self.player_turn)
        
    def ai_move(self):
        if self.player_turn == 1:
            minimax_ai = MinimaxAI(self, max_depth = 3)
            bestMove = minimax_ai.getBestMove()
            
            if bestMove:
                move_type, index = bestMove
                if move_type == "take":
                    self.take_number(index)
                elif move_type == "split":
                    self.split_number(index)
            self.update_ui(self.sequence, self.scores, self.player_turn)
        
    def game_over(self):
        return len(self.sequence) == 0
        