#!/usr/bin/python3
"""unitest for place class"""

import unittest
import sys
import io
from models.place import Place

class Testclassplace(unittest.TestCase):
        """
    place class tests
        """
        def test_classplacetype(self):
            c = Place()
            a = type(c)
            print(a)
            self.assertEqual(type(c), type(Place()))

if __name__ == "__main__":
    unittest.main()
