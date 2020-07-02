#!/usr/bin/python3
"""FileStorage Module"""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """class with which we can serializes and deserialize"""

    __file_path = 'file.json'
    __object = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__object

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            self.__object[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        se_dic = {}
        for key, value in FileStorage.__object.items():
            se_dic[key] = value.to_dict()
        with open(self.__file_path, 'w') as wri_f:
            json.dump(se_dic, wri_f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        dic_class={'BaseModel': BaseModel, 'User': User}
        try:
            with open(self.__file_path, 'r') as read_file:
                all_obj = json.load(read_file)
            for key, value in all_obj.items():
                if value['_class_'] in dic_class:
                    obj = eval(value['__class__'])(**value)
                self.__object[key] = obj

        except FileNotFoundError:
            pass
