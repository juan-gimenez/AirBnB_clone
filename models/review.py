#!/usr/bin/python3
"""
review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    review class
    """

    def __init__(self, *args, **kwargs):
        self.place = ""
        self.user = ""
        self.text = ""
        super().__init__(*args, **kwargs)
