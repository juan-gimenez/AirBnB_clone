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
    c = State()

    def test_classstatetype(self):
        """
        test instance type
        """
        c = State()
        a = type(c)
        print(a)
        self.assertEqual(type(c), type(State()))

    def test_publicclassattr(self):
        """
        test public class attributes
        """        
        c = State()
        self.assertTrue(hasattr(c, 'name'))

if __name__ == "__main__":
    unittest.main()
