class Reflector:
    
    reflectors = {

        "A" : [5, 10, 13, 26, 1, 12, 25, 24, 22, 2, 23, 6, 3, 18, 17, 21, 15, 14, 20, 19, 16, 9, 11, 8, 7, 4],

        "B" : [25, 18, 21, 8, 17, 19, 12, 4, 16, 24, 14, 7, 15, 11, 13, 9, 5, 2, 6, 26, 3, 23, 22, 10, 1, 20],

        "C" : [6, 22, 16, 10, 9, 1, 15, 25, 5, 4, 18, 26, 24, 23, 7, 3, 20, 11, 21, 17, 19, 2, 14, 13, 8, 12]

        }
    
    def __init__(self, reflector_type = "A" ):

        reflector_type = reflector_type.upper()

        if reflector_type not in self.reflectors:
            raise ValueError("Invalid Reflector-Typ: " + reflector_type )
        
        self.reflector_type = reflector_type

        self.reflector = self.reflectors[reflector_type]

    def print_reflector(self):
        print("Reflector-Typ: " + str(self.reflector_type))

        for key, value in self.reflector.items():
            print(key + " : " + value)
        print("\n")

    def swap(self, letter):
        
        return self.reflector[(letter-1)]
    
    def get_reflector(self):
        return self.reflector