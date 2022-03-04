#!/usr/bin/python3
"""unitest for state class"""

import unittest
import sys
import io
from models.state import State

class Testclassstate(unittest.TestCase):
    """
    state class tests
    """
    def test_classstatetype(self):
        c = State()
        a = type(c)
        print(a)
        self.assertEqual(type(c), type(State()))

if __name__ == "__main__":
    unittest.main()
