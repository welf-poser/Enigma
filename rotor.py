class Rotor:
    
    rotors = {
        1 : [
            
            [5, 11, 13, 6, 12, 7, 4, 17, 22, 26, 14, 20, 15, 23, 25, 8, 24, 21, 19, 16, 1, 9, 2, 18, 3, 10]

            ,{
                "E": "A",
                "K": "B",
                "M": "C",
                "F": "D",
                "L": "E",
                "G": "F",
                "D": "G",
                "Q": "H",
                "V": "I",
                "Z": "J",
                "N": "K",
                "T": "L",
                "O": "M",
                "W": "N",
                "Y": "O",
                "H": "P",
                "X": "Q",
                "U": "R",
                "S": "S",
                "P": "T",
                "A": "U",
                "I": "V",
                "B": "W",
                "R": "X",
                "C": "Y",
                "J": "Z"
            }],

        2 : [
            
            [1, 10, 4, 11, 19, 9, 18, 21, 24, 2, 12, 8, 23, 20, 13, 3, 17, 7, 26, 14, 16, 25, 6, 22, 15, 5],
            
            {
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
            }],

        3 :  [

            [2, 4, 6, 8, 10, 12, 3, 16, 18, 20, 24, 22, 26, 14, 25, 5, 9, 23, 7, 1, 11, 13, 21, 19, 17, 15]
        
            ,{
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
            }],

        4 : [
        
            [5, 19, 15, 22, 16, 26, 10, 1, 25, 17, 21, 9, 18, 8, 24, 12, 14, 6, 20, 7, 11, 4, 3, 13, 23, 2]
        
            ,{
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
            }],

        5 : [
        
            [22, 26, 2, 18, 7, 9, 20, 25, 21, 16, 19, 4, 14, 8, 12, 24, 1, 23, 13, 10, 17, 15, 6, 5, 3, 11]
        
            ,{
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
            }],

        6 : [
        
            [10, 16, 7, 22, 15, 21, 13, 6, 25, 17, 2, 5, 14, 8, 26, 18, 4, 11, 1, 19, 24, 12, 9, 3, 20, 23]
        
            ,{
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
            }],

        7 : [
        
            [14, 26, 8, 7, 18, 3, 24, 13, 25, 19, 23, 2, 15, 21, 6, 1, 9, 22, 12, 16, 10, 11, 4, 5, 20, 17]
            
            ,{
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
            }],

        8 : [
        
            [6, 11, 17, 8, 20, 12, 24, 15, 3, 2, 10, 19, 16, 4, 26, 18, 1, 13, 5, 23, 14, 9, 21, 25, 7, 22]
        
        ,   {
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
}]

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
        self.rotor = self.rotors[rotor_type]

        offset = ring_setting - 1  
        self.ring_setting = offset

        

        
    #def print_rotor(self):


    def swap(self, letter, pos):
        letter = ord(letter) + pos
        list = self.rotor[0]
        return list[(letter-65)%25]


    #def reverse_swap(self, letter, pos):


    def get_rotor(self):
        return self.rotor
    
    def get_inv_rotor(self):
        return self.inverse_rotor
    
    def get_notch(self):
        return self.notch