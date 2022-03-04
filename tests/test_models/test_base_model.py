#!/usr/bin/python3
"""unitest for base model"""

import unittest
import sys
import io
from models.base_model import BaseModel


class Testclassbase(unittest.TestCase):
    """
    class to test base model
    """

    def test_classbase(self):
        """
        tests
        """
        c = BaseModel()
        a = type(c)
        print(a)
        self.assertEqual(type(c), type(BaseModel()))

    def test_checkdict(self):
        """
        check dict
        """
        d = {}
        x = BaseModel()
        c = x.to_dict()
        a = type(c)
        b = type(d)
        self.assertEqual(a, b)

    def test_checkstrtype(self):
        """
        check str type
        """
        d = ""
        x = BaseModel()
        c = x.__str__()
        a = type(c)
        b = type(d)
        self.assertEqual(a, b)


if __name__ == "__main__":
    unittest.main()
