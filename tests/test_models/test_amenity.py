#!/usr/bin/python3
"""unitest for amenity subclass"""

import unittest
import sys
import io
from models.amenity import Amenity


class Testclassamenity(unittest.TestCase):
    """
    amenity sub class tests
    """
    def test_classamenitytype(self):
        c = Amenity()
        a = type(c)
        print(a)
        self.assertEqual(type(c), type(Amenity()))

    def test_publicclassattr(self):
        """
        test public class attributes
        """
        c = Amenity()
        self.assertTrue(hasattr(c, 'name'))

    def test_doc(self):
        """
        test documentation
        """
        self.assertTrue(Amenity.__str__.__doc__ != "")

if __name__ == "__main__":
    unittest.main()
