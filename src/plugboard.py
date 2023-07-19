"""
The plugboard class in the enigma machine
"""

class Plugboard:
    """
    Plugboard for the enigma machine, the plugboard use dictionary to map the wiring
    """
    def __init__(self):
        self.wiring = {
            "A" : "A",
            "B" : "B",
            "C" : "C",
            "D" : "D",
            "E" : "E",
            "F" : "F",
            "G" : "G",
            "H" : "H",
            "I" : "I",
            "J" : "J",
            "K" : "K",
            "L" : "L",
            "M" : "M",
            "N" : "N",
            "O" : "O",
            "P" : "P",
            "Q" : "Q",
            "R" : "R",
            "S" : "S",
            "T" : "T",
            "U" : "U",
            "V" : "V",
            "W" : "W",
            "X" : "X",
            "Y" : "Y",
            "Z" : "Z"
        }

    def cypher(self, char):
        """
        The cypher of the plugboard
        """
        char = char.upper()
        return self.wiring[char]

    def add_wiring(self, char1, char2):
        """
        Set the wiring of the plugboard
        """
        char1 = char1.upper()
        char2 = char2.upper()
        self.wiring[char1] = char2
        self.wiring[char2] = char1

    def remove_wiring(self, char):
        """
        Remove the wiring of the plugboard and return the removed character
        """
        char = char.upper()
        removed = self.wiring[char]
        self.wiring[char] = char
        self.wiring[removed] = removed
        return removed
