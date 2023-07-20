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
        if self.rotor[1].position == self.rotor[1].notch:
            self.rotor[0].rotate()

        if self.rotor[2].position == self.rotor[2].notch:
            self.rotor[1].rotate()
        
        self.rotor[2].rotate()

    def encrypt(self, char):
        """
        Perform encryption on a single character in the enigma machine
        """
        # check if it's outside of alphabet
        if not char.isalpha():
            return char, char, char, char, char, char, char, char, char, char

        uppercase = char.isupper()

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

        # handle lowercase
        if not uppercase:
            plugboard_input = plugboard_input.lower()
            rl_3 = rl_3.lower()
            rl_2 = rl_2.lower()
            rl_1 = rl_1.lower()
            ref = ref.lower()
            lr_1 = lr_1.lower()
            lr_2 = lr_2.lower()
            lr_3 = lr_3.lower()
            plugboard_output = plugboard_output.lower()

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

def __test_turing__(text, dummy):
    """
    Helper function to test whether or not the current setup is correct
    """
    CORRECT_TEXT = "HELLO SUDO"
    res = ""
    for i in range(len(CORRECT_TEXT)):
        temp = dummy.encrypt(text[i])
        temp = temp[9]
        # assume plugboard if mismatch
        if temp != CORRECT_TEXT[i]:
            if dummy.plugboard.wiring[text[i]] != CORRECT_TEXT[i]:
                return False
            dummy.plugboard.add_wiring(text[i], CORRECT_TEXT[i])
            temp = CORRECT_TEXT[i]
        res += temp
    return res == CORRECT_TEXT

def __num_to_rotor__(num):
    """
    Helper function to convert number to rotor
    """
    if num == 1:
        return RotorI()
    if num == 2:
        return RotorII()
    if num == 3:
        return RotorIII()
    return None

def __num_to_rotor_name__(num):
    """
    Helper function to convert number to rotor name
    """
    if num == 1:
        return "Rotor I"
    if num == 2:
        return "Rotor II"
    if num == 3:
        return "Rotor III"
    return None

def turing(text):
    """
    Turing the enigma machine to find the setting (brute force)
    The text is the text that is encrypted and it should start with "HELLO SUDO" when decrypted
    """
    dummy_enigma = Enigma()

    # the bruteforce loop
    for left_rotor in range(1,4):
        for middle_rotor in range(1,4):
            for right_rotor in range(1,4):
                for left_pos in range(ord("A"), ord("Z")+1):
                    for middle_pos in range(ord("A"), ord("Z")+1):
                        for right_pos in range(ord("A"), ord("Z")+1):
                            print("Testing: " + __num_to_rotor_name__(left_rotor) + " " + __num_to_rotor_name__(middle_rotor) + " " + __num_to_rotor_name__(right_rotor) + " " + chr(left_pos) + " " + chr(middle_pos) + " " + chr(right_pos))
                            dummy_enigma.set_left_rotor(__num_to_rotor__(left_rotor))
                            dummy_enigma.set_middle_rotor(__num_to_rotor__(middle_rotor))
                            dummy_enigma.set_right_rotor(__num_to_rotor__(right_rotor))
                            dummy_enigma.set_left_position(chr(left_pos))
                            dummy_enigma.set_middle_position(chr(middle_pos))
                            dummy_enigma.set_right_position(chr(right_pos))
                            if __test_turing__(text, dummy_enigma):
                                r1 = "Left Rotor is " + __num_to_rotor_name__(left_rotor) + " at position " + chr(left_pos)
                                r2 = "Middle Rotor is " + __num_to_rotor_name__(middle_rotor) + " at position " + chr(middle_pos)
                                r3 = "Right Rotor is " + __num_to_rotor_name__(right_rotor) + " at position " + chr(right_pos)
                                plugboard = "Plugboard is " + str(dummy_enigma.plugboard.wiring)
                                res = r1 + "\n" + r2 + "\n" + r3 + "\n" + plugboard
                                return res
    return None
