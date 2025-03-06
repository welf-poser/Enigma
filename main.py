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
