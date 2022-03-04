#!/usr/bin/python3
"""
Module city.py - contains the city class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    city class
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        self.state = ""
        self.name = ""
        super().__init__(*args, **kwargs)
