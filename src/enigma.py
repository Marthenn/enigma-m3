"""
The enigma machine class
"""

from rotor import RotorI, RotorII, RotorIII, Reflector
from plugboard import Plugboard

class Enigma:
    """
    Enigma machine class (3 rotors, 1 reflector, 1 plugboard)
    The enigma is based of Enigma M3
    """
    def __init__(self):
        self.rotor = [RotorI(), RotorII(), RotorIII()]
        self.reflector = Reflector()
        self.plugboard = Plugboard()

    def __rotate__(self):
        """
        Rotate the rotors of the enigma machine
        """
        self.rotor[2].rotate()

        if self.rotor[2].position == self.rotor[2].notch:
            self.rotor[1].rotate()

        if self.rotor[1].position == self.rotor[1].notch:
            self.rotor[0].rotate()

    def encrypt(self, char):
        """
        Perform encryption on a single character in the enigma machine
        """
        # check if it's outside of alphabet
        if not char.isalpha():
            return char, char, char, char, char, char, char, char, char, char

        self.__rotate__()
        plugboard_input = self.plugboard.cypher(char)
        rl_3 = self.rotor[2].forward_cypher(plugboard_input)
        rl_2 = self.rotor[1].forward_cypher(rl_3)
        rl_1 = self.rotor[0].forward_cypher(rl_2)
        ref = self.reflector.forward_cypher(rl_1)
        lr_1 = self.rotor[0].reverse_cypher(ref)
        lr_2 = self.rotor[1].reverse_cypher(lr_1)
        lr_3 = self.rotor[2].reverse_cypher(lr_2)
        plugboard_output = self.plugboard.cypher(lr_3)
        return char, plugboard_input, rl_3, rl_2, rl_1, ref, lr_1, lr_2, lr_3, plugboard_output

    def set_left_rotor(self, rotor):
        """
        Set the left rotor of the enigma machine
        """
        pos = self.rotor[0].position
        self.rotor[0] = rotor
        self.rotor[0].position = pos

    def set_middle_rotor(self, rotor):
        """
        Set the middle rotor of the enigma machine
        """
        pos = self.rotor[1].position
        self.rotor[1] = rotor
        self.rotor[1].position = pos

    def set_right_rotor(self, rotor):
        """
        Set the right rotor of the enigma machine
        """
        pos = self.rotor[2].position
        self.rotor[2] = rotor
        self.rotor[2].position = pos

    def set_left_position(self, position):
        """
        Set the position of the left rotor of the enigma machine
        """
        self.rotor[0].position = position

    def set_middle_position(self, position):
        """
        Set the position of the middle rotor of the enigma machine
        """
        self.rotor[1].position = position

    def set_right_position(self, position):
        """
        Set the position of the right rotor of the enigma machine
        """
        self.rotor[2].position = position
