class Plugboard:
    def __init__(self, connections):

        if len(connections) > 10:
            raise ValueError("Too many connections: " + str(len(connections.items())))
        else:
            self.connections = connections.copy()

            for key, value in connections:
                self.connections[value] = key

    def swap(self, letter):

        letter = letter.upper()

        if letter in self.connections.keys():
            return self.connections[letter]
        else:
            return letter

    def unplug(self, letter):

        letter = letter.upper()

        if letter in self.connections.keys():

            print("Letter " + letter + " <-> " + self.connections[letter] + "unplugged")

            val = self.connections[letter]

            del self.connections[letter]
            del self.connections[val]
            
        else:
            print("The letter " + letter + " wasn´t plugged")

    def plug(self, letter1, letter2):
        if letter1 in self.connections.keys():

            print("Letters " + letter1 + " <-> " + self.connections[letter1] + " unplugged")
            self.unplug(self, letter1)
        
        if letter2 in self.connections.keys():

            print("Letters " + letter1 + " <-> " + self.connections[letter1] + " unplugged")
            self.unplug(self, letter2)

        if len(self.connections.keys()) > 20:
            print("Too many connections!")
            return
        else:
            self.connections[letter1] = letter2
            self.connections[letter2] = letter1
            print("Letters " + letter1 + "<->" + letter2 + " plugged")

    def print_plugboard(self):
            print("Plugboard connections " + str((len(self.connections.keys()))/2))

            for key, value in self.connections.items():
                print(key + " : " + value)
            print("\n")

    