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
        """
        test
        """
        c = Place()
        a = type(c)
        print(a)
        self.assertEqual(type(c), type(Place()))
        
def test_test(self):
        """
        test if attributes
        """
        c = Place()
        self.assertTrue(hasattr(c, 'city_id'))
        self.assertTrue(hasattr(c, 'user_id'))
        self.assertTrue(hasattr(c, 'name'))
        self.assertTrue(hasattr(c, 'description'))
        self.assertTrue(hasattr(c, 'number_rooms'))
        self.assertTrue(hasattr(c, 'number_bathrooms'))
        self.assertTrue(hasattr(c, 'max_guest'))
        self.assertTrue(hasattr(c, 'price_by_night'))
        self.assertTrue(hasattr(c, 'latitude'))
        self.assertTrue(hasattr(c, 'longitude'))
        self.assertTrue(hasattr(c, 'amenity_ids'))

def test_doc(self):
        """
        test documentation
        """
        self.assertTrue(Place.__str__.__doc__ != "")

        if __name__ == "__main__":
                unittest.main()
