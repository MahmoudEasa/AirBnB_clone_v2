#!/usr/bin/python3
"""
if equal to db:
    import DBStorage class in this file
    create an instance of DBStorage and store it in the variable storage
else:
    import FileStorage class in this file
    create an instance of FileStorage and store it in the variable storage
"""
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
