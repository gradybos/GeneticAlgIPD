"""
Representation of a Random Prisoner's Dilemma Player
Author: Grady Bosanko
Version: Fall 2024
"""
import random
class RandomPlayer:
    def get_input(self, _):
        flip = random.randint(0,1)
        if flip == 0:
            return "C"
        else:
            return "D"