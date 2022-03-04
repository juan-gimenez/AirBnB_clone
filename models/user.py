#!/usr/bin/env python3
"""
User module that contains the user class

"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User module which manages the users of the system
    """

    def __init__(self, *args, **kwargs):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
