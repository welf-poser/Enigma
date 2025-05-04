from enigma.rotor import Rotor
from enigma.reflector import Reflector
from enigma.plugboard import Plugboard

class enigma:
    def __init__(self, ukw: Reflector, rotor1: Rotor, rotor2: Rotor, rotor3: Rotor, plugboard: Plugboard):
        self.ukw = ukw
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.plugboard = plugboard

    def encrypt(self,string):
        string = str.upper(string)
        
        for chr in string:
            