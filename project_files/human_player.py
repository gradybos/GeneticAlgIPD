"""
Representation of a Human Prisoner's Dilemma Player
Author: Grady Bosanko
Version: Fall 2024
"""
class HumanPlayer:
    def get_input(self, _):
        print("Choose either cooperate, [C], or defect, [D].")
        return input("Enter your move: ")