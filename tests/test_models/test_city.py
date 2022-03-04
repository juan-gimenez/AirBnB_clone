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
        """
        test instance type
        """
        c = City()
        a = type(c)
        print(a)
        self.assertEqual(type(c), type(City()))

    def test_publicclassattr(self):
        """
        test public class attributes
        """
        c = City()
        self.assertTrue(hasattr(c, 'name'))
        self.assertTrue(hasattr(c, 'state_id'))

if __name__ == "__main__":
    unittest.main()
