import pytest
from plugboard import Plugboard


@pytest.fixture
def plugboard():
    plugboard = Plugboard({"A":"b", "c":"D", "e":"f", "G":"H"})
    return plugboard

def test_get_connections(plugboard):
    assert plugboard.get_connections() == {"A":"B", "B":"A", "C":"D", "D":"C", "E":"F", "F":"E", "G":"H", "H":"G" }

def test_swap(plugboard):
    assert plugboard.swap("a") == "B"
    assert plugboard.swap("A") == "B"
    assert plugboard.swap("Z") == "Z"
    assert plugboard.swap("z") == "Z"

def test_unplug(plugboard):
    plugboard.unplug("A")
    assert plugboard.get_connections() == {"C":"D", "D":"C", "E":"F", "F":"E", "G":"H", "H":"G" }

    plugboard = Plugboard({"A":"b", "c":"D", "e":"f", "G":"H"})

    plugboard.unplug("D")
    assert plugboard.get_connections() == {"A":"B", "B":"A", "E":"F", "F":"E", "G":"H", "H":"G" }

    plugboard.unplug("Z")

def test_plug(plugboard):
    plugboard.plug("A","A")
    assert plugboard.get_connections() == {"A":"B", "B":"A", "C":"D", "D":"C", "E":"F", "F":"E", "G":"H", "H":"G" }

    plugboard.plug("A","C")
    assert plugboard.get_connections() == {"A":"C", "C":"A", "E":"F", "F":"E", "G":"H", "H":"G" }