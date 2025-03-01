#Wehrmacht Enigma I (M3)

class Enigma:
    def __init__(self, reflector, rotor3, pos3, rotor2, pos2, rotor1, pos1, plugboard):
        self.reflector = reflector
        self.rotor1 = rotor1
        self.rotor2 = rotor2
        self.rotor3 = rotor3
        self.plugboard = plugboard

        self.pos1 = pos1 -1
        self.pos2 = pos2 -1
        self.pos3 = pos3 -1

        """
        initial_settings = {
            "plugboard" : plugboard.copy(),
            "pos1" : pos1.copy(),
            "rotor1" : rotor1.copy(),
            "pos2" : pos2.copy(),
            "rotor2" : rotor2.copy(),
            "pos3" : pos3.copy(),
            "rotor3" : rotor3.copy(),
            "reflector" : reflector.copy(),
        }
        """

    def prep_message(self, msg):

        msg = msg.upper()
        prep_msg = ""
        for char in msg:
            if ord(char) == 32 or ord(char) >= 65 or char == " " or char == "\n":
                prep_msg += char
            
        return prep_msg
    
    def encrypt(self, msg):

        msg = self.prep_message(msg)
        msg_encrypt = ""

        for char in msg:

            if char == " " or char == "\n":
                msg_encrypt += char
                continue

            print("Keyboard Input: " + char)

            self.pos1 = (self.pos1 % 26) + 1

            if self.pos1 in self.rotor1.get_notch():

                self.pos2 = (self.pos2 % 26) + 1

                # Double Step Mechanismus für den mittleren Rotor
                if self.pos2 in self.rotor2.get_notch():
                    self.pos2 = (self.pos2 % 26) + 1
                    self.pos3 = (self.pos3 % 26) + 1

            print("Rotors Position: " + chr(self.pos3 + 65) + ", " +
                chr(self.pos2 + 65) + ", " + chr(self.pos1 + 65))

            # Verschlüsselungsschritt:
            char = self.plugboard.swap(char)
            print("Plugboard Encryption: " + char)


            char = self.rotor1.swap(char, self.pos1)
            print("Wheel 1 Encryption: " + char)

            char = self.rotor2.swap(char, self.pos2)
            print("Wheel 2 Encryption: " + char)

            char = self.rotor3.swap(char, self.pos3)
            print("Wheel 3 Encryption: " + char)


            char = self.reflector.swap(char)  # Reflektor bleibt unverändert
            print("Reflector Encryption: " + char)


            char = self.rotor3.reverse_swap(char, self.pos3)
            print("Wheel 3 Reverse Encryption: " + char)


            char = self.rotor2.reverse_swap(char, self.pos2)
            print("Wheel 2 Reverse Encryption: " + char)

 
            char = self.rotor1.reverse_swap(char, self.pos1)
            print("Wheel 1 Reverse Encryption: " + char)

            char = self.plugboard.swap(char)
            print("Plugboard Encryption: " + char)
            print("-----------------------------\n")

            msg_encrypt += char

        return msg_encrypt


    def decrypt(self, msg):
        return self.encrypt(msg)

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

    """
    def get_init_settings(self):
        return initial_settings
    """







