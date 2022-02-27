#!/usr/bin/python3
"""
module which initializes the models folder
"""


from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
