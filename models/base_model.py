#!/usr/bin/python3
""" Define BaseModel Class"""
import uuid
from datetime import datetime
import models
from models.file_storage import storage

class BaseModel:
    """
    Base model class that define attributes and methods for all models
    """
    def __init__(self):
        """
        Initializes a new instances of the BaseModels class with default values
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'update_at']:
                        value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
                self.created_at = datetime.strptime(kwargs['created_at'],
                date_format)
                self.updated_at = datetime.strptime(kwargs['updated_at'],
                date_format)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance
        """
        return "[{}] ({}) {}".format(self.__class__,__name__,self.id,
        self.__dict__)

    def save(self):
        """
        Update the updated_at attribbute of the BaseModel instance with the
        current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = dict_copy['created_at'].isoformat()
        dict_copy['updated_at'] = dict_copy['updated_at'].isoformat()
        return dict_copy

