#!/usr/bin/python3
"""unitest for user class"""

import unittest
import sys
import io
from models.user import User

class Testclassuser(unittest.TestCase):
    """ 
    user class tests 
    """
    def test_classusertype(self):
        c = User()
        a = type(c)
        print(a)
        self.assertEqual(type(c), type(User()))

if __name__ == "__main__":
    unittest.main()
