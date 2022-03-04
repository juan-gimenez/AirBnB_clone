#!/usr/bin/python3
"""
Module amenity.py - contains the amenity class
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    amenity class
    """

    def __init__(self, *args, **kwargs):
        self.name = ""
        super().__init__(*args, **kwargs)
