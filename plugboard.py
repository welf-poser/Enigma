class Plugboard:
    def __init__(self, connections):
        #Not Failsave when A:A or A:B, B:A
        if len(connections) > 10:
            raise ValueError("Too many connections: " + str(len(connections.items())))
        
        self.connections = {}
        for key, value in connections.items():
            self.connections[key.upper()] = value.upper()
            self.connections[value.upper()] = key.upper()

    def get_connections(self):
        return self.connections

    def swap(self, letter):

        letter = letter.upper()

        if letter in self.connections.keys():
            return self.connections[letter]
        else:
            return letter.upper()

    def unplug(self, letter):

        letter = letter.upper()

        if letter in self.connections.keys():

            print("Letters " + letter + " <-> " + self.connections[letter] + " unplugged")

            val = self.connections[letter]

            self.connections.pop(letter)
            self.connections.pop(val)
        else:
            print("The letter " + letter + " wasn´t plugged")


    def plug(self, letter1, letter2):
        
        letter1 = letter1.upper()
        letter2 = letter2.upper()

        if letter1 == letter2:
            print("Letters must not be equal!")
            return
        
        if len(self.connections.keys()) == 20:
            print("Max connections reached!")
            return

        if letter1 in self.connections.keys():

            print("Letters " + letter1 + " <-> " + self.connections[letter1] + " unplugged")
            self.unplug(letter1)
        
        if letter2 in self.connections.keys():

            print("Letters " + letter2 + " <-> " + self.connections[letter2] + " unplugged")
            self.unplug(letter2)

        self.connections[letter1] = letter2
        self.connections[letter2] = letter1
        print("Letters " + letter1 + "<->" + letter2 + " plugged")

    def print_plugboard(self):
            print("Plugboard connections: " + str((len(self.connections.keys()))/2))

            for key, value in self.connections.items():
                print(key + " : " + value)
            print("\n")

    