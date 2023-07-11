#!/usr/bin/python3
"""Defines a class Student """


class Student:
    """
    representation of a student
    """
    def __init__(self, first_name, last_name, age):
        """
        initializes a new student

        Args:
            first_name (str): the first name of the student
            last_name (str): the last name of the student
            age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    json_dict[attr] = self.__dict__[attr]
            return json_dict

    def reload_from_json(self, json):
        """
        replaces all attributes of self with json
        """
        for key, value in json.items():
            setattr(self, key, value)
