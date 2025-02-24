import pytest 
from reflector import Reflector

@pytest.fixture
def reflector():
    reflector = Reflector("A")
    return reflector

def test_get_reflector(reflector):
    assert reflector.get_reflector() == {
                "A": "E", "B": "J", "C": "M", "D": "Z", "E": "A", "F": "L", "G": "Y", "H": "X",
                "I": "V", "J": "B", "K": "W", "L": "F", "M": "C", "N": "R", "O": "Q", "P": "U",
                "Q": "O", "R": "N", "S": "T", "T": "S", "U": "P", "V": "I", "W": "K", "X": "H",
                "Y": "G", "Z": "D"
            }
    
def test_swap(reflector):
    assert reflector.swap("A") == "E"