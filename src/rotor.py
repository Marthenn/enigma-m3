"""
Rotor classes for the Enigma Machine
The rotors are based on the rotors used in the M3 Enigma Machine
https://www.cryptomuseum.com/crypto/enigma/wiring.htm
"""

class Rotor():
    """
    The parent class of all rotors (including the reflector)
    """
    def __init__(self):
        self.wiring = {}
        self.notch = ""
        self.position = "A"
    
    def rotate(self):
        """
        Rotate the rotor by one position
        """
        self.position = chr(ord(self.position) + 1)
        if self.position > "Z":
            self.position = "A"

    def forward_cypher(self, char):
        """
        The forward cypher of the rotor (right to left in the machine)
        """
        pass

    def reverse_cypher(self, char):
        """
        The reverse cypher of the rotor (left to right in the machine)
        """
        pass

class RotorI(Rotor):
    """
    The class representing Rotor I in Enigma M3
    """
    def __init__(self):
        Rotor.__init__(self)
        self.wiring = {
            "A" : "E",
            "B" : "K",
            "C" : "M",
            "D" : "F",
            "E" : "L",
            "F" : "G",
            "G" : "D",
            "H" : "Q",
            "I" : "V",
            "J" : "Z",
            "K" : "N",
            "L" : "T",
            "M" : "O",
            "N" : "W",
            "O" : "Y",
            "P" : "H",
            "Q" : "X",
            "R" : "U",
            "S" : "S",
            "T" : "P",
            "U" : "A",
            "V" : "I",
            "W" : "B",
            "X" : "R",
            "Y" : "C",
            "Z" : "J"
        }
        self.notch = "Q"
        self.position = "A"

class RotorII(Rotor):
    """
    The class representing Rotor II in Enigma M3
    """
    def __init__(self):
        Rotor.__init__(self)
        self.wiring = {
            "A" : "A",
            "B" : "J",
            "C" : "D",
            "D" : "K",
            "E" : "S",
            "F" : "I",
            "G" : "R",
            "H" : "U",
            "I" : "X",
            "J" : "B",
            "K" : "L",
            "L" : "H",
            "M" : "W",
            "N" : "T",
            "O" : "M",
            "P" : "C",
            "Q" : "Q",
            "R" : "G",
            "S" : "Z",
            "T" : "N",
            "U" : "P",
            "V" : "Y",
            "W" : "F",
            "X" : "V",
            "Y" : "O",
            "Z" : "E"
        }
        self.notch = "E"
        self.position = "A"

class RotorIII(Rotor):
    """
    The class representing Rotor III in Enigma M3
    """
    def __init__(self):
        Rotor.__init__(self)
        self.wiring = {
            "A" : "B",
            "B" : "D",
            "C" : "F",
            "D" : "H",
            "E" : "J",
            "F" : "L",
            "G" : "C",
            "H" : "P",
            "I" : "R",
            "J" : "T",
            "K" : "X",
            "L" : "V",
            "M" : "Z",
            "N" : "N",
            "O" : "Y",
            "P" : "E",
            "Q" : "I",
            "R" : "W",
            "S" : "G",
            "T" : "A",
            "U" : "K",
            "V" : "M",
            "W" : "U",
            "X" : "S",
            "Y" : "Q",
            "Z" : "O"
        }
        self.notch = "V"
        self.position = "A"

class Reflector(Rotor):
    """
    The class representing Reflector UKW-B in Enigma M3
    """
    def __init__(self):
        Rotor.__init__(self)
        self.wiring = {
            "A" : "Y",
            "B" : "R",
            "C" : "U",
            "D" : "H",
            "E" : "Q",
            "F" : "S",
            "G" : "L",
            "H" : "D",
            "I" : "P",
            "J" : "X",
            "K" : "N",
            "L" : "G",
            "M" : "O",
            "N" : "K",
            "O" : "M",
            "P" : "I",
            "Q" : "E",
            "R" : "B",
            "S" : "F",
            "T" : "Z",
            "U" : "C",
            "V" : "W",
            "W" : "V",
            "X" : "J",
            "Y" : "A",
            "Z" : "T"
        }
        self.position = "A"
