class Reflector:
    def __init__(self, reflector_type):
        self.reflector_type = reflector_type

        self.reflectors = {
            'A':{'A':'E', 'B':'J', 'C':'M', 'D':'Z', 'E':'A', 'F':'L', 'G':'Y', 'H':'X', 'I':'V', 'J':'B', 'K':'W', 'L':'F', 'M':'C', 'N':'R', 'O':'Q', 'P':'U', 'Q':'O', 'R':'N', 'S':'T', 'T':'S', 'U':'P', 'V':'I', 'W':'K', 'X':'H', 'Y':'G', 'Z':'D'},
            'B':{'A':'Y', 'B':'R', 'C':'U', 'D':'H', 'E':'Q', 'F':'S', 'G':'L', 'H':'D', 'I':'P', 'J':'X', 'K':'N', 'L':'G', 'M':'O', 'N':'K', 'O':'M', 'P':'I', 'Q':'E', 'R':'B', 'S':'F', 'T':'Z', 'U':'C', 'V':'W', 'W':'V', 'X':'J', 'Y':'A', 'Z':'T'},
            'C':{'A':'F', 'B':'V', 'C':'P', 'D':'J', 'E':'I', 'F':'A', 'G':'O', 'H':'Y', 'I':'E', 'J':'D', 'K':'R', 'L':'Z', 'M':'X', 'N':'W', 'O':'G', 'P':'C', 'Q':'T', 'R':'K', 'S':'U', 'T':'Q', 'U':'S', 'V':'B', 'W':'N', 'X':'M', 'Y':'H', 'Z':'L'},

        }
        self.reflector = self.reflectors[reflector_type]

    def swap(self, letter):
        return self.reflector[letter]