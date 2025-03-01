class Rotor:
    
    rotors = {
        1 : {
                "A": "E", # 1
                "B": "K", # 2
                "C": "M", # 3
                "D": "F", # 4
                "E": "L", # 5
                "F": "G", # 6
                "G": "D", # 7
                "H": "Q", # 8
                "I": "V", # 9
                "J": "Z", #10
                "K": "N", #11
                "L": "T", #12
                "M": "O", #13
                "N": "W", #14
                "O": "Y", #15
                "P": "H", #16
                "Q": "X", #17
                "R": "U", #18
                "S": "S", #19
                "T": "P", #20
                "U": "A", #21
                "V": "I", #22
                "W": "B", #23
                "X": "R", #24
                "Y": "C", #25
                "Z": "J"  #26
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
    #PRÜFEN OB FALSCH!!!!!!!!!!!!!!!!!!!!!!!!
    notches = {

        1 : [17], # Q
        2 : [5], # E
        3 : [22], # V
        4 : [10], # J
        5 : [26], # Z
        6 : [26, 13], # Z, M
        7 : [26, 13], # Z, M
        8 : [26, 13], # Z, M

    }
    
    
    
    def __init__(self, rotor_type, ring_setting):
        if rotor_type not in self.rotors:
            raise ValueError("Invalid Rotor-Typ: " + str(rotor_type))
        if ring_setting < 1 or ring_setting > 26:
            raise ValueError("Invalid Ring-Setting: " + str(ring_setting))
        
        self.rotor_type = rotor_type
        self.notch = self.notches[rotor_type]

        offset = ring_setting - 1  
        self.ring_setting = offset


        self.rotor = [None] * 26
        self.inverse_rotor = [None] * 26

        for key, value in self.rotors[rotor_type].items():

            idx = (ord(key) - ord("A") + offset) % 26
            self.rotor[idx] = value  
            
            inv_idx = (ord(value) - ord("A") + offset) % 26
            self.inverse_rotor[inv_idx] = key


        
    def print_rotor(self):
        print("Rotor-Type: " + str(self.rotor_type))
        print("Ring-Setting: " + str(self.ring_setting))
        for key, value in self.rotor.items():
            print(key + " : " + value)
        print("\n")

    def swap(self, letter, pos):
        letter = (ord(letter.upper()) - 64 + pos) % 25
        return self.rotor[letter]


    def reverse_swap(self, letter, pos):
        letter = (ord(letter.upper()) - 64 + pos) % 25
        return self.inverse_rotor[letter]

    """
    def reverse_swap(self, letter, pos):
        letter = letter.upper()
        new_ord = (ord(letter) - ord("A") - pos) % 26 + ord("A")
        new_letter = chr(new_ord)
        return self.inverse_rotor[new_letter]
    """
    def get_rotor(self):
        return self.rotor
    
    def get_inv_rotor(self):
        return self.inverse_rotor
    
    def get_notch(self):
        return self.notch