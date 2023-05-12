#!/usr/bin/python3
"""
Module containing the FileStorage class.
"""

import json


class FileStorage:
    """
    Class for serializing and deserializing instances to and from JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """
        Initializes a new instance of the FileStorage class.
        """
        self.__file_path = FileStorage.__file_path
        self.__objects = FileStorage.__objects

    def all(self, cls=None):
        """
        Returns a dictionary of all objects currently in storage.

        If a class is specified, only objects of that class are returned.
        """
        if cls is None:
            return self.__objects
        else:
            filtered = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    filtered[k] = v
            return filtered

    def new(self, obj):
        """
        Adds a new object to the storage dictionary.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the dictionary of objects to a JSON file.
        """
        serialized = {}
        for k, v in self.__objects.items():
            serialized[k] = v.to_dict()

        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            json.dump(serialized, f)

    def reload(self):
        """
        Deserializes the JSON file to a dictionary of objects.
        """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                data = json.load(f)

            for k, v in data.items():
                cls_name = v["__class__"]
                cls = eval(cls_name)
                obj = cls(**v)
                self.__objects[k] = obj

        except FileNotFoundError:
            pass

