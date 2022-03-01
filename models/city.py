#!/usr/bin/python3
"""
Module city.py - contains the city class
"""

BaseModel = __import__("base_models.py").BaseModel

Class City(BaseModel):
    """
    city class
    """
    state_id = ""
    name = ""
