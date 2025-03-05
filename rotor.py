class Rotor:
    
    rotors = {
        1 : {#["E","K","M","F","L","G","D","Q","V","Z","N","T","O","W","Y","H","X","U","S","P","A","I","B","R","C","J"]
                
                5 : 1,
                "K": 2,
                "M": 3,
                "F": 4,
                "L": 5,
                "G": 6,
                "D": 7,
                "Q": 8,
                "V": 9,
                "Z": 10,
                "N": 11,
                "T": 12,
                "O": 13,
                "W": 14,
                "Y": 15,
                "H": 16,
                "X": 17,
                "U": 18,
                "S": 19,
                "P": 20,
                "A": 21,
                "I": 22,
                "B": 23,
                "R": 24,
                "C": 25,
                "J": 26
            },

        2 : {
                "A": "A",
                "J": "B",
                "D": "C",
                "K": "D",
                "S": "E",
                "I": "F",
                "R": "G",
                "U": "H",
                "X": "I",
                "B": "J",
                "L": "K",
                "H": "L",
                "W": "M",
                "T": "N",
                "M": "O",
                "C": "P",
                "Q": "Q",
                "G": "R",
                "Z": "S",
                "N": "T",
                "P": "U",
                "Y": "V",
                "F": "W",
                "V": "X",
                "O": "Y",
                "E": "Z"
},

        3 :  {
                "B": "A",
                "D": "B",
                "F": "C",
                "H": "D",
                "J": "E",
                "L": "F",
                "C": "G",
                "P": "H",
                "R": "I",
                "T": "J",
                "X": "K",
                "V": "L",
                "Z": "M",
                "N": "N",
                "Y": "O",
                "E": "P",
                "I": "Q",
                "W": "R",
                "G": "S",
                "A": "T",
                "K": "U",
                "M": "V",
                "U": "W",
                "S": "X",
                "Q": "Y",
                "O": "Z"
},

        4 : {
                "E": "A", 
                "S": "B", 
                "O": "C",  
                "V": "D", 
                "P": "E", 
                "Z": "F",  
                "J": "G",  
                "A": "H", 
                "Y": "I",  
                "Q": "J",  
                "U": "K",  
                "I": "L",  
                "R": "M",  
                "H": "N",  
                "X": "O",  
                "L": "P",  
                "N": "Q",  
                "F": "R",  
                "T": "S",  
                "G": "T",  
                "K": "U",  
                "D": "V",  
                "C": "W",  
                "M": "X",  
                "W": "Y",  
                "B": "Z"  
},

        5 : {
                "V": "A",
                "Z": "B",
                "B": "C",
                "R": "D",
                "G": "E",
                "I": "F",
                "T": "G",
                "Y": "H",
                "U": "I",
                "P": "J",
                "S": "K",
                "D": "L",
                "N": "M",
                "H": "N",
                "L": "O",
                "X": "P",
                "A": "Q",
                "W": "R",
                "M": "S",
                "J": "T",
                "Q": "U",
                "O": "V",
                "F": "W",
                "E": "X",
                "C": "Y",
                "K": "Z"
},

        6 : {
                "J": "A",
                "P": "B",
                "G": "C",
                "V": "D",
                "O": "E",
                "U": "F",
                "M": "G",
                "F": "H",
                "Y": "I",
                "Q": "J",
                "B": "K",
                "E": "L",
                "N": "M",
                "H": "N",
                "Z": "O",
                "R": "P",
                "D": "Q",
                "K": "R",
                "A": "S",
                "S": "T",
                "X": "U",
                "L": "V",
                "I": "W",
                "C": "X",
                "T": "Y",
                "W": "Z"
},

        7 : {
                "N": "A",
                "Z": "B",
                "H": "C",
                "G": "D",
                "R": "E",
                "C": "F",
                "X": "G",
                "M": "H",
                "Y": "I",
                "S": "J",
                "W": "K",
                "B": "L",
                "O": "M",
                "U": "N",
                "F": "O",
                "A": "P",
                "I": "Q",
                "V": "R",
                "L": "S",
                "P": "T",
                "J": "U",
                "K": "V",
                "D": "W",
                "E": "X",
                "T": "Y",
                "Q": "Z"
},

        8 : {
                "F": "A",
                "K": "B",
                "Q": "C",
                "H": "D",
                "T": "E",
                "L": "F",
                "X": "G",
                "O": "H",
                "C": "I",
                "B": "J",
                "J": "K",
                "S": "L",
                "P": "M",
                "D": "N",
                "Z": "O",
                "R": "P",
                "A": "Q",
                "M": "R",
                "E": "S",
                "W": "T",
                "N": "U",
                "I": "V",
                "U": "W",
                "Y": "X",
                "G": "Y",
                "V": "Z"
}

    }
    
    notches = {

        1 : [18], # Q
        2 : [6], # E
        3 : [23], # V
        4 : [11], # J
        5 : [1], # Z
        6 : [1, 14], # Z, M
        7 : [1, 14], # Z, M
        8 : [1, 14], # Z, M

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
        print("Pos in swap " + str(pos))
        letter = (ord(letter.upper()) - 65 + pos) % 25
        return self.rotor[letter]


    def reverse_swap(self, letter, pos):
        print("Pos in swap " + str(pos))
        letter = (ord(letter.upper()) - 65 + pos) % 25
        return self.inverse_rotor[letter]
        #Maybe Bug here??
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