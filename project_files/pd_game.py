"""
Representation of a Prisoner's Dilemma Game
Author: Grady Bosanko
Version: Fall 2024
"""
class PDGame:
    def __init__ (self, player1, player2, rounds):
        self.rounds = rounds
        self.p1 = player1
        self.p2 = player2

    def play(self):
        self.p1.reset_points()
        self.p2.reset_points()
        round = 1
        while round <= self.rounds:
            self.play_one_round()
            round += 1
        #print("Player 1: ", self.p1.points, " Player 2: ", self.p2.points)
        #self.calculate_winner()

    def play_one_round(self):
        p1_input = self.p1.get_input()
        p2_input = self.p2.get_input()
        result = p1_input + p2_input
        self.p1.moves.append(result)
        self.p2.moves.append(result[::-1])
        scores = self.calculate_scores(result)
        self.p1.add_points(scores[0])
        self.p2.add_points(scores[1])

    def calculate_scores(self, result):
        if result == "CC":
            return (3, 3)
        elif result == "CD":
            return (0,5)
        elif result == "DC":
            return (5,0)
        else:
            return (1,1)
        
    def calculate_winner(self):
        if self.p1.points > self.p2.points:
            print("Player 1 wins!")
        elif self.p1.points < self.p2.points:
            print("Player 2 wins!")
        else:
            print("It's a draw!")

    def get_scores(self):
        return (self.p1.points, self.p2.points)
    
    def change_player(self, player_num, new_player):
        if player_num == 1:
            self.p1 = new_player
        else:
            self.p2 = new_player