from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard
from enigma import Enigma

plugboard = Plugboard({
                        #"B":"Q", 
                        #"C":"R",
                        #"D":"I",
                        #"E":"J",
                        #"K":"W",
                        #"M":"T",
                        #"O":"S",
                        #"P":"X",
                        #"U":"Z",
                        #"G":"H"
                    })

rotor1 = Rotor(1, 1)
rotor2 = Rotor(2, 1)
rotor3 = Rotor(3, 1)
rotor4 = Rotor(4, 1)
rotor6 = Rotor(5, 1)
rotor3 = Rotor(6, 1)
rotor2 = Rotor(7, 1)
rotor3 = Rotor(8, 1)

for i in range(8):
    rotor1 = Rotor(i, 1)
    dict = rotor1.get_rotor()
    list = []

    for key, value in dict.items():
        list.append(ord(key)-64)
    print(list)

"""
reflector = Reflector("B")

enigma = Enigma(reflector, rotor3, 1, rotor2, 1, rotor1, 1, plugboard,)

orig_msg = ("The crucial point is: by changing ourselves, we change the world. As we become more loving on the inside, healing occurs on the outside. Much like the rising of the sea level lifts all ships, so the radiance of unconditional love within a human heart lifts all of life!")

test = "AAA"

print(enigma.rotor1.rotor)
print(enigma.rotor1.inverse_rotor)
encrypt_msg = enigma.encrypt(test)
print(encrypt_msg)

enigma = Enigma(reflector, rotor3, 1, rotor2, 1, rotor1, 1, plugboard,)
encrypt_msg = enigma.encrypt(encrypt_msg)
print(encrypt_msg)


    A -> D
    AA -> NZ
    AAA -> AYA
"""

rotor