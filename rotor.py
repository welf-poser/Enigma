class Rotor:
    
    rotors = {
        1 : [
            
            [5, 11, 13, 6, 12, 7, 4, 17, 22, 26, 14, 20, 15, 23, 25, 8, 24, 21, 19, 16, 1, 9, 2, 18, 3, 10],
            [21, 23, 25, 7, 1, 4, 6, 16, 22, 26, 2, 5, 3, 11, 13, 20, 8, 24, 19, 12, 18, 9, 14, 17, 15, 10]
            
            ],
            
        2 : [
            
            [1, 10, 4, 11, 19, 9, 18, 21, 24, 2, 12, 8, 23, 20, 13, 3, 17, 7, 26, 14, 16, 25, 6, 22, 15, 5],
            [1, 10, 16, 3, 26, 23, 18, 12, 6, 2, 4, 11, 15, 20, 25, 21, 17, 7, 5, 14, 8, 24, 13, 9, 22, 19]
            
            ],

        3 :  [

            [2, 4, 6, 8, 10, 12, 3, 16, 18, 20, 24, 22, 26, 14, 25, 5, 9, 23, 7, 1, 11, 13, 21, 19, 17, 15],
            [20, 1, 7, 2, 16, 3, 19, 4, 17, 5, 21, 6, 22, 14, 26, 8, 25, 9, 24, 10, 23, 12, 18, 11, 15, 13]
            
            ],

        4 : [
        
            [5, 19, 15, 22, 16, 26, 10, 1, 25, 17, 21, 9, 18, 8, 24, 12, 14, 6, 20, 7, 11, 4, 3, 13, 23, 2],
            [8, 26, 23, 22, 1, 18, 20, 14, 12, 7, 21, 16, 24, 17, 3, 5, 10, 13, 2, 19, 11, 4, 25, 15, 9, 6]
            
            ],

        5 : [
        
            [22, 26, 2, 18, 7, 9, 20, 25, 21, 16, 19, 4, 14, 8, 12, 24, 1, 23, 13, 10, 17, 15, 6, 5, 3, 11],
            [17, 3, 25, 12, 24, 23, 5, 14, 6, 20, 26, 15, 19, 13, 22, 10, 21, 4, 11, 7, 9, 1, 18, 16, 8, 2]
            
            ],

        6 : [
        
            [10, 16, 7, 22, 15, 21, 13, 6, 25, 17, 2, 5, 14, 8, 26, 18, 4, 11, 1, 19, 24, 12, 9, 3, 20, 23],
            [19, 11, 24, 17, 12, 8, 3, 14, 23, 1, 18, 22, 7, 13, 5, 2, 10, 16, 20, 25, 6, 4, 26, 21, 9, 15]

            ],

        7 : [
        
            [14, 26, 8, 7, 18, 3, 24, 13, 25, 19, 23, 2, 15, 21, 6, 1, 9, 22, 12, 16, 10, 11, 4, 5, 20, 17],
            [16, 12, 6, 23, 24, 15, 4, 3, 17, 21, 22, 19, 8, 1, 13, 20, 26, 5, 10, 25, 14, 18, 11, 7, 9, 2]
            
            ],

        8 : [
        
            [6, 11, 17, 8, 20, 12, 24, 15, 3, 2, 10, 19, 16, 4, 26, 18, 1, 13, 5, 23, 14, 9, 21, 25, 7, 22],
            [17, 10, 9, 14, 19, 1, 25, 4, 22, 11, 2, 6, 18, 21, 8, 13, 3, 16, 12, 5, 23, 26, 20, 7, 24, 15]
            
            ]

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
        self.list_fwd = self.rotor[0]
        self.list_bwd = self.rotor[1]

        self.ring_setting = ring_setting - 1  
        

    #def print_rotor(self):

    def swap(self, letter, pos):
        print(letter)
        letter = letter - pos
        print(letter)
        print(pos)
        print(self.list_fwd[letter])
        return self.list_fwd[letter]

    def reverse_swap(self, letter, pos):
        letter = letter - pos
        return self.list_bwd[letter]

    def get_rotor(self):
        return self.rotor
    
    def get_inv_rotor(self):
        return self.inverse_rotor
    
    def get_notch(self):
        return self.notch