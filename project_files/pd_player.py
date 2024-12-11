"""
Representation of a Prisoner's Dilemma Player
Author: Grady Bosanko
Version: Fall 2024
"""
class PDPlayer:
    def __init__ (self, player_type):
        self.moves = []
        self.points = 0
        self.type = player_type
    
    def get_input(self):
        input = ""
        while input != "C" and input != "D":
            input = self.type.get_input(self.moves).upper()
        return input
    
    def add_points(self, points):
        self.points += points

    def reset_points(self):
        self.points = 0