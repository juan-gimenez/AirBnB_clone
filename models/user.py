#!/usr/bin/env python3
"""
User module that contains the user class

"""

from models.base_model  import BaseModel

class User(BaseModel):
    """
    User module which manages the users of the system
    """
    
    email = ""
    password = ""
    first_name = ""
    last_name = ""
