#Wehrmacht Enigma I (M3)

class Enigma:
    def __init__(self, reflector, rotor3, pos3, rotor2, pos2, rotor1, pos1, plugboard):
        self.reflector = reflector
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.plugboard = plugboard

        self.pos1 = pos1
        self.pos2 = pos2
        self.pos3 = pos3

        def prep_message(msg):

            msg = msg.upper()
            prep_msg = ""
            for char in msg:
                if ord(char) == 32 or ord(char) >= 65 or ord(char) <= 90:
                    prep_msg += char
                
            return prep_msg
        
        def encrypt(self, msg):

            msg = prep_message(msg)


            for char in msg:
                plugboard.swap(char)

                #Hier weitermachen!




        def decrypt(self, msg):
            return encrypt(msg)

        def change_pos(self, rotor, pos):
            
            if pos < 1 or pos > 26:
                raise ValueError("No valid position: " + str(pos))
            
            if rotor < 1 or rotor > 3:
                raise ValueError("No valid rotor-position: " + str(rotor))

            match rotor:
                case 1:
                    self.pos1 = pos
                    print("Rotor 1 changed to position " + str(pos))
                case 2:
                    self.pos2 = pos
                    print("Rotor 2 changed to position " + str(pos))
                case 3:
                    self.pos3 = pos
                    print("Rotor 3 changed to position " + str(pos))








