from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard

plugboard = Plugboard({"A":"b", "c":"D", "e":"f", "G":"H"})

plugboard.print_plugboard()

plugboard.unplug("D")

plugboard.print_plugboard()