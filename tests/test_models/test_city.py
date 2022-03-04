#!/usr/bin/python3
"""unitest for city class"""

import unittest
import sys
import io
from models.city import City

class Testclasscity(unittest.TestCase):
    """
    city class tests
    """
    def test_classcitytype(self):
        c = City()
        a = type(c)
        print(a)
        self.assertEqual(type(c), type(City()))

if __name__ == "__main__":
    unittest.main()
