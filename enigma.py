#Wehrmacht Enigma I (M3)

class Enigma:
    def __init__(self, reflector, rotor3, ring_setting3, rotor2, ring_setting2, rotor1, ring_setting1, plugboard, message):
        self.reflector = reflector
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.plugboard = plugboard

        self.ring_setting1 = ring_setting1
        self.ring_setting2 = ring_setting2
        self.ring_setting3 = ring_setting3

        self.message = message

        