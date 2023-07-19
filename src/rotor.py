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
        # setup variables
        char = char.upper()
        offset = ord(self.position) - ord("A")
        idx = ord(char) - ord("A")

        print("idx: " + str(idx) + " offset: " + str(offset))

        mapped = self.wiring[(idx + offset) % 26]

        print("mapped: " + mapped)

        res_idx = (ord(mapped) - ord("A") - offset)%26
        if res_idx < 0:
            res_idx += 26
        res = chr(res_idx + ord("A"))

        return res

    def reverse_cypher(self, char):
        """
        The reverse cypher of the rotor (left to right in the machine)
        """
        char = char.upper() # Make sure the character is uppercase

        offset = ord(self.position) - ord("A") # The offset of the rotor
        pass

class RotorI(Rotor):
    """
    The class representing Rotor I in Enigma M3
    """
    def __init__(self):
        Rotor.__init__(self)
        self.wiring = list("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
        self.notch = "Q"
        self.position = "A"

class RotorII(Rotor):
    """
    The class representing Rotor II in Enigma M3
    """
    def __init__(self):
        Rotor.__init__(self)
        self.wiring = list("AJDKSIRUXBLHWTMCQGZNPYFVOE")
        self.notch = "E"
        self.position = "A"

class RotorIII(Rotor):
    """
    The class representing Rotor III in Enigma M3
    """
    def __init__(self):
        Rotor.__init__(self)
        self.wiring = list("BDFHJLCPRTXVZNYEIWGAKMUSQO")
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

if __name__ == "__main__":
    r1 = RotorI()
    r2 = RotorII()
    r3 = RotorIII()
    r1.position = "A"
    r2.position = "B"
    r3.position = "A"
    a3 = r3.forward_cypher("A")
    a2 = r2.forward_cypher(a3)
    a1 = r1.forward_cypher(a2)
    print(a3)
    print(a2)
    print(a1)
