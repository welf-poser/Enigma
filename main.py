from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard


i = 1
while i < 9:
    rotor = Rotor(i) 

    vals = []
    for key, value in rotor.get_rotor().items():
        vals.append(value)
    
    print("Rotor: " + str(i))
    print(vals)

    i+=1