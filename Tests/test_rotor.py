from rotor import Rotor


def test_swap():
    rotor = Rotor(1)
    assert rotor.swap("A") == "E"
    assert rotor.swap("T") == "P"

    rotor = Rotor(2)
    assert rotor.swap("A") == "A"
    assert rotor.swap("T") == "N"

    rotor = Rotor(3)
    assert rotor.swap("A") == "B"
    assert rotor.swap("T") == "A"

    rotor = Rotor(4)
    assert rotor.swap("A") == "E"
    assert rotor.swap("T") == "G"

    rotor = Rotor(5)
    assert rotor.swap("A") == "V"
    assert rotor.swap("T") == "J"

    rotor = Rotor(6)
    assert rotor.swap("A") == "J"
    assert rotor.swap("T") == "S"

    rotor = Rotor(7)
    assert rotor.swap("A") == "N"
    assert rotor.swap("T") == "P"

    rotor = Rotor(8)
    assert rotor.swap("A") == "F"
    assert rotor.swap("T") == "W"

def test_get_rotor():
    rotor = Rotor(1)
    assert rotor.get_rotor() == {
                "A": "E", "B": "K", "C": "M", "D": "F", "E": "L", "F": "G", "G": "D", "H": "Q",
                "I": "V", "J": "Z", "K": "N", "L": "T", "M": "O", "N": "W", "O": "Y", "P": "H",
                "Q": "X", "R": "U", "S": "S", "T": "P", "U": "A", "V": "I", "W": "B", "X": "R",
                "Y": "C", "Z": "J"
            }
    
def test_reverse_swap():
    rotor = Rotor(1)
    assert rotor.reverse_swap("A") == "U"

def test_get_notch():
    rotor = Rotor(1)
    assert rotor.get_notch() == ["Q"]

    rotor = Rotor(7)
    assert rotor.get_notch() == ["Z", "M"]