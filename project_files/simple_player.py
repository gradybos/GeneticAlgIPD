"""
Representation of a Prisoner's Dilemma Player
that uses a simple strategy
Author: Grady Bosanko
Version: Fall 2024
"""
class SimplePlayer:
    def __init__(self):
        self.count = 0

    def get_input(self, moves):
        length = len(moves)
        if length == 0:
            return "D"
        else:
            if length > 3:
                length = 3
            visible_moves = moves[-length:]
            d_count = 0
            c_count = 0
            for move in visible_moves:
                if move[1] == "D":
                    d_count += 1
                else:
                    c_count += 1
            if d_count > c_count:
                return "D"
            else:
                return "C"