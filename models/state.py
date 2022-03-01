#!/usr/bin/python3
"""
Module state.py - contains the state class
"""

BaseModel = __import__("base_models.py").BaseModel

Class State(BaseModel):
    """
    state class
    """
    name = ""
