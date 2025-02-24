import unittest
from plugboard import Plugboard

class test_plugboard(unittest.TestCase):

    def setUp(self):
        self.prugboard = Plugboard({"A":"b", "C":"D", "E":"F", "G":"H"})

