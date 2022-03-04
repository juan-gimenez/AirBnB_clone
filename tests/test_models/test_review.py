#!/usr/bin/python3
"""unitest for review class"""

import unittest
import sys
import io
from models.review import Review


class Testclassreview(unittest.TestCase):
    """
    Review class tests
    """
    def test_classreviewtype(self):
        c = Review()
        a = type(c)
        print(a)
        self.assertEqual(type(c), type(Review()))

    def test_publicclassattr(self):
        """
        test public class attributes
        """
        c = Review()
        self.assertTrue(hasattr(c, 'user_id'))
        self.assertTrue(hasattr(c, 'text'))

        if __name__ == "__main__":
            unittest.main()
