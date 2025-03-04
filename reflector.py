class Reflector:
    
    reflectors = {
        "A" : {
                "E": "A",
                "J": "B",
                "M": "C",
                "Z": "D",
                "A": "E",
                "L": "F",
                "Y": "G",
                "X": "H",
                "V": "I",
                "B": "J",
                "W": "K",
                "F": "L",
                "C": "M",
                "R": "N",
                "Q": "O",
                "U": "P",
                "O": "Q",
                "N": "R",
                "T": "S",
                "S": "T",
                "P": "U",
                "I": "V",
                "K": "W",
                "H": "X",
                "G": "Y",
                "D": "Z"
},

        "B" : {
                "Y": "A",
                "R": "B",
                "U": "C",
                "H": "D",
                "Q": "E",
                "S": "F",
                "L": "G",
                "D": "H",
                "P": "I",
                "X": "J",
                "N": "K",
                "G": "L",
                "O": "M",
                "K": "N",
                "M": "O",
                "I": "P",
                "E": "Q",
                "B": "R",
                "F": "S",
                "Z": "T",
                "C": "U",
                "W": "V",
                "V": "W",
                "J": "X",
                "A": "Y",
                "T": "Z"
},

        "C" : {
                "F": "A",
                "V": "B",
                "P": "C",
                "J": "D",
                "I": "E",
                "A": "F",
                "O": "G",
                "Y": "H",
                "E": "I",
                "D": "J",
                "R": "K",
                "Z": "L",
                "X": "M",
                "W": "N",
                "G": "O",
                "C": "P",
                "T": "Q",
                "K": "R",
                "U": "S",
                "Q": "T",
                "S": "U",
                "B": "V",
                "N": "W",
                "M": "X",
                "H": "Y",
                "L": "Z"
},

    }
    
    def __init__(self, reflector_type = "A" ):

        reflector_type = reflector_type.upper()

        self.reflector_type = reflector_type

        if reflector_type not in self.reflectors:
            raise ValueError("Invalid Reflector-Typ: " + reflector_type )

        self.reflector = self.reflectors[reflector_type]

    def print_reflector(self):
        print("Reflector-Typ: " + str(self.reflector_type))

        for key, value in self.reflector.items():
            print(key + " : " + value)
        print("\n")

    def swap(self, letter):
        letter = letter.upper()
        return self.reflector[letter]
    
    def get_reflector(self):
        return self.reflector