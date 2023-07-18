#!usr/bin/python3
"""
Data persistence module
Serialize a python dict to json file
Deserialize a json file to python dict
"""
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances:
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with
        key = <obj class name>.id
        value = instances of BaseModel class
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def classes_dict(self):
        """
        Returns a dict representation of classes
        """
        classes_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": city,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review}
        return classes_dict

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w", encoding='utf-8') as json_file:
            my_dict2 = {key: obj.to_dict()
                        for key, obj in FileStorage.__objects.items()}
            json.dump(my_dict2, json_file)

    def reload(self):
        """
        deserializes the JSON file to __objects if the JSON file path exists
        """
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, encoding='utf-8') as json_file:
            des_dict = json.load(json_file)
            des_dict = {key: self.classes_dict()[value['__class__']](**value)
                        for key, value in des_dict.items()}
            FileStorage.__objects = des_dict
