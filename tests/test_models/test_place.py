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
        self.asserTrue(hasattr(c, city_id))
        self.asserTrue(hasattr(c, user_id))
        self.asserTrue(hasattr(c, name))
        self.asserTrue(hasattr(c, description))
        self.asserTrue(hasattr(c, number_rooms))
        self.asserTrue(hasattr(c, number_bathrooms))
        self.asserTrue(hasattr(c, max_guest))
        self.asserTrue(hasattr(c, price_by_night))
        self.asserTrue(hasattr(c, latitude))
        self.asserTrue(hasattr(c, longitude))
        self.asserTrue(hasattr(c, amenity_ids))

        if __name__ == "__main__":
                unittest.main()
