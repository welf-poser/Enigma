from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard
from enigma import Enigma

plugboard = Plugboard({
                        "B":"Q", 
                        "C":"R",
                        "D":"I",
                        "E":"J",
                        "K":"W",
                        "M":"T",
                        "O":"S",
                        "P":"X",
                        "U":"Z",
                        "G":"H"
                    })

rotor1 = Rotor(1, 1)
rotor2 = Rotor(1, 1)
rotor3 = Rotor(1, 1)

reflector = Reflector("B")

enigma = Enigma(reflector, rotor3, 1, rotor2, 1, rotor1, 1, plugboard,)

orig_msg = ("The crucial point is: by changing ourselves, we change the world. As we become more loving on the inside, healing occurs on the outside. Much like the rising of the sea level lifts all ships, so the radiance of unconditional love within a human heart lifts all of life!")

test = "AA"

encrypt_msg = enigma.encrypt(test)

print(encrypt_msg)
