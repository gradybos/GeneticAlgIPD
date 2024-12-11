"""
Representation of a Prisoner's Dilemma Player
that uses a given pattern as its strategy
Author: Grady Bosanko
Version: Fall 2024
"""
class PatternPlayer:
    def __init__(self, pattern):
        self.pattern = pattern
        self.count = 0

    def get_input(self, _):
        if self.count >= len(self.pattern):
            self.count = 0
        move = self.pattern[self.count]
        self.count += 1
        return move
    
    def set_pattern(self, new_pattern):
        self.pattern = new_pattern