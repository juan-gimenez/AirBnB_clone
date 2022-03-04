#!/usr/bin/python3
"""
Module place.py - contains the place class
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    place class
    """

    def __init__(self, *args):
        self.city_id = ""
        self.user_id = ""
        self.description = ""
        self.unmber_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super.__init__(*args)
