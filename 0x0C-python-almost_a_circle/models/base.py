#!/usr/bin/python3
"""Defines a Base class"""
import json


class Base:
    """
    represents a Base object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initializes a new Base

        Args:
            id (int): The Base id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): a list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherit Base
            (eg Rectangle and Square)
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_string = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(json_string))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string

        Args:
            json_string (str): a string representing a list of dictionaries
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set

        Args:
            **dictionary: double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances loaded from a file
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                if json_string:
                    dicts = cls.from_json_string(json_string)
                    instances = [cls.create(**dic) for dic in dicts]
                    return instances
                else:
                    return []
        except FileNotFoundError:
            return []
