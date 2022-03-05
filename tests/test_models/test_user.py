#!/usr/bin/python3
"""unitest for user class"""

import io
import sys
import unittest
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

    def test_publicclassatrr(self):
        c = User()
        self.assertTrue(hasattr(c, 'email'))
        self.assertTrue(hasattr(c, 'password'))
        self.assertTrue(hasattr(c, 'first_name'))
        self.assertTrue(hasattr(c, 'last_name'))

    def test_doc(self):
        """
        test documentation
        """
        self.assertTrue(User.__str__.__doc__ != "")

if __name__ == "__main__":
    unittest.main()
