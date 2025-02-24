class Rotor:
    
    rotors = {
        1 : {
                "A": "E", "B": "K", "C": "M", "D": "F", "E": "L", "F": "G", "G": "D", "H": "Q",
                "I": "V", "J": "Z", "K": "N", "L": "T", "M": "O", "N": "W", "O": "Y", "P": "H",
                "Q": "X", "R": "U", "S": "S", "T": "P", "U": "A", "V": "I", "W": "B", "X": "R",
                "Y": "C", "Z": "J"
            },

        2 : {
                "A": "A", "B": "J", "C": "D", "D": "K", "E": "S", "F": "I", "G": "R", "H": "U",
                "I": "X", "J": "B", "K": "L", "L": "H", "M": "W", "N": "T", "O": "M", "P": "C",
                "Q": "Q", "R": "G", "S": "Z", "T": "N", "U": "P", "V": "Y", "W": "F", "X": "V",
                "Y": "O", "Z": "E"
            },

        3 : {
                "A": "B", "B": "D", "C": "F", "D": "H", "E": "J", "F": "L", "G": "C", "H": "P",
                "I": "R", "J": "T", "K": "X", "L": "V", "M": "Z", "N": "N", "O": "Y", "P": "E",
                "Q": "I", "R": "W", "S": "G", "T": "A", "U": "K", "V": "M", "W": "U", "X": "S",
                "Y": "Q", "Z": "O"
            },

        4 : {
                "A": "E", "B": "S", "C": "O", "D": "V", "E": "P", "F": "Z", "G": "J", "H": "A",
                "I": "Y", "J": "Q", "K": "U", "L": "I", "M": "R", "N": "H", "O": "X", "P": "L",
                "Q": "N", "R": "F", "S": "T", "T": "G", "U": "K", "V": "D", "W": "C", "X": "M",
                "Y": "W", "Z": "B"
            },

        5 : {
                "A": "V", "B": "Z", "C": "B", "D": "R", "E": "G", "F": "I", "G": "T", "H": "Y",
                "I": "U", "J": "P", "K": "S", "L": "D", "M": "N", "N": "H", "O": "L", "P": "X",
                "Q": "A", "R": "W", "S": "M", "T": "J", "U": "Q", "V": "O", "W": "F", "X": "E",
                "Y": "C", "Z": "K"
            },

        6 : {
                "A": "J", "B": "P", "C": "G", "D": "V", "E": "O", "F": "U", "G": "M", "H": "F",
                "I": "Y", "J": "Q", "K": "B", "L": "E", "M": "N", "N": "H", "O": "Z", "P": "R",
                "Q": "D", "R": "K", "S": "A", "T": "S", "U": "X", "V": "L", "W": "I", "X": "C",
                "Y": "T", "Z": "W"
            },

        7 : {
                "A": "N", "B": "Z", "C": "H", "D": "G", "E": "R", "F": "C", "G": "X", "H": "M",
                "I": "Y", "J": "S", "K": "W", "L": "B", "M": "O", "N": "U", "O": "F", "P": "A",
                "Q": "I", "R": "V", "S": "L", "T": "P", "U": "J", "V": "K", "W": "D", "X": "E",
                "Y": "T", "Z": "Q"
            },

        8 : {
                "A": "F", "B": "K", "C": "Q", "D": "H", "E": "T", "F": "L", "G": "X", "H": "O",
                "I": "C", "J": "B", "K": "J", "L": "S", "M": "P", "N": "D", "O": "Z", "P": "R",
                "Q": "A", "R": "M", "S": "E", "T": "W", "U": "N", "V": "I", "W": "U", "X": "Y",
                "Y": "G", "Z": "V"
            }

    }

    notches = {
        1 : ["Q"], # Dreht bei Q zu R
        2 : ["E"],
        3 : ["V"],
        4 : ["J"],
        5 : ["Z"],
        6 : ["Z", 'M'],
        7 : ["Z", 'M'],
        8 : ["Z", 'M'],

    }
    
    
    
    def __init__(self, rotor_type):
 
        self.rotor_type = rotor_type
        self.notch = self.notches[rotor_type]

        if rotor_type not in self.rotors:
            raise ValueError("Invalid Rotor-Typ: " + rotor_type)
        
        self.rotor = self.rotors[rotor_type]
        self.inverse_rotor = {}
        for key, value in self.rotor.items():
            self.inverse_rotor[value] = key
        
    def print_rotor(self):
        print("Rotor-Type: " + str(self.rotor_type))

        for key, value in self.rotor.items():
            print(key + " : " + value)
        print("\n")

    def swap(self, letter):
        letter = letter.upper()
        return self.rotor[letter]
    
    def reverse_swap(self, letter):
        letter.upper()
        return self.inverse_rotor[letter]
    
    def get_rotor(self):
        return self.rotor
    
    def get_inv_rotor(self):
        return self.inverse_rotor
    
    def get_notch(self):
        return self.notch