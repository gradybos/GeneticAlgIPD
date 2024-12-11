"""
Representation of a Prisoner's Dilemma Player
that uses a TIT FOR TAT strategy.
Author: Grady Bosanko
Version: Fall 2024
"""
class TFTPlayer:

    def get_input(self, moves):
        length = len(moves)
        if length == 0:
            return "C"
        else:
            last_move = moves[-1]
            opponent_last_move = last_move[-1]
            return opponent_last_move