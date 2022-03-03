#!/usr/bin/python3
"""unitest for base model"""

import unittest
import sys
import io
from models.base_model import BaseModel

class Testclassbase(unittest.TestCase):

    def test_classbase(self):
        c = BaseModel()
        a = type(c)
        print(a)
        self.assertEqual(type(c), type(BaseModel()))

if __name__ == "__main__":
    unittest.main()
