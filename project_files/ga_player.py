"""
Representation of a Prisoner's Dilemma Player
that uses a given GA genome as its strategy
Author: Grady Bosanko
Version: Fall 2024
"""
class GAPlayer:
    def __init__(self, genome):
        self.gene = genome

    def get_input(self, moves):
        # find the most recent moves (up to 3)
        length = len(moves)
        num_known_moves = 3
        if length < num_known_moves:
            last_inputs = moves[-length:]
        else:
            last_inputs = moves[-num_known_moves:]
        # flatten inputs
        last_inputs_str = ""
        for input in last_inputs:
            last_inputs_str += input
        index = self.decode_input(last_inputs_str)
        # return "C" if no prev inputs
        if index == -1:
            return "C"
        else:
            return self.gene[index]

    def decode_input(self, input_str):
        bit_str = ""
        for char in input_str:
                if char == 'C':
                    bit_str += '0'
                else:
                    bit_str +='1'
        if len(bit_str) == 4:
            bit_str = bit_str[-2:]
            return int(bit_str, 2) + 66
        elif len(bit_str) == 2:
            return int(bit_str, 2) + 64
        elif len(bit_str) == 0:
            return -1
        else:
            return int(bit_str, 2)