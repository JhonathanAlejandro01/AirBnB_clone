#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage():
    """class with which we can serializes and deserialize"""

    __file_path = 'file.json'
    __object = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__object

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = obj.__class__.__name__ + "." + obj.id
            self.__object[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        se_dic = {}
        for key in self.__object:
            se_dic[key] = self.__object[key].to_dict()
            with open(self.__file_path, 'w') as wri_f:
                json.dump(se_dic, wri_f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as read_file:
                all_obj = json.load(read_file)
                for key, value in all_obj.items():
                    name_class = value.get('__class__')
                    obj = eval(name_class + '(**value)')
                    self.__object[key] = obj

        except FileNotFoundError:
            pass
