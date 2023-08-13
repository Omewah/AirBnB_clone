#!/usr/bin/python3
"""This defines attributes and methods"""
import uuid
from datetime import datetime
import models

class BaseModel:
    """BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Init BaseModel: arguments + key-value arguments"""
        if kwargs:
            time_stamp = '%Y-%m-%dT%H:%M:%S.%f'
            for key_kwarg, value_kwarg in kwargs.items():
                if key_kwarg == '__class__':
                    continue
                elif key_kwarg == 'created_at':
                    self.created_at = datetime.strptime(
                        kwargs['created_at'], time_stamp)
                elif key_kwarg == 'updated_at':
                    self.updated_at = datetime.strptime(
                        kwargs['updated_at'], time_stamp)
                else:
                    setattr(self, key_kwarg, value_kwarg)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Allows BaseModel to be read for display or debugging"""

        NameClass = self.__class__.__name__
        return "[{}] ({}) {}".format(NameClass, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with the current date + time"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Converts key_kwargs/value_kwargs to a dictionary"""
        dict_inst = self.__dict__.copy()
        dict_inst['updated_at'] = self.updated_at.isoformat()
        dict_inst['created_at'] = self.created_at.isoformat()
        dict_inst['__class__'] = self.__class__.__name__
        return dict_inst
