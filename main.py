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

rotor1 = Rotor(1,1)
rotor2 = Rotor(1,1)
rotor3 = Rotor(1,1)

refl = Reflector("B")

enigma = Enigma(refl, rotor3, 1, rotor2, 1, rotor1, 1, plugboard)

output = enigma.encrypt("AAA")

print(output)