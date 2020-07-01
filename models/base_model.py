#!/usr/bin/python3
"""new class BaseModel"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """new class"""
    def __init__(self, *args, **kwargs):
        """contructor methot"""
        if kwargs:
            for k, v in kwargs.items():

                if k == "created_at":
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')

                if k == "updated_at":
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')

                if k != "__class__":
                    self.__dict__[k] = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """update the atribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """return a dict with the name class and
         value in atribure created_at, updated_at"""
        new_dict = dict(self.__dict__)
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
