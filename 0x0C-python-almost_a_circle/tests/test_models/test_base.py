#!/usr/bin/python3
"""Defines unittest for the Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """Unittest cases for the Base class"""

    def test_init_with_id(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_init_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_string_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(3.2, Base(3.2).id)

    def test_nb_instances(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)


class Test_to_json_string(unittest.TestCase):
    """Tests to_json_string"""

    def test_to_json_string_with_empty_list(self):
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_with_none(self):
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_with_list(self):
        list_dicts = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        expected = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json_string, expected)

    def test_to_json_string_with_more_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 2)

    def test_to_json_string_with_square(self):
        s = Square(10, 2, 3, 4)
        self.assertEqual(len(Base.to_json_string([s.to_dictionary()])), 39)

    def test_to_json_string_with_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 6)
        self.assertEqual(len(Base.to_json_string([r.to_dictionary()])), 53)


class Test_save_to_file(unittest.TestCase):
    """Tests Base.save_to_file"""

    def tearDown(self):
        """cleans up files"""
        try:
            os.remove("Base.json")
        except IOError:
            pass
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_save_to_file_with_empty_list(self):
        Base.save_to_file([])
        with open("Base.json", "r") as f:
            json_string = f.read()
            self.assertEqual(json_string, "[]")

    def test_save_to_file_with_none(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as f:
            json_string = f.read()
            self.assertEqual(json_string, "[]")

    def test_save_to_file_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as f:
            json_string = f.read()
            self.assertEqual(len(json_string), 53)

    def test_save_to_file_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            json_string = f.read()
            self.assertEqual(len(json_string), 39)

    def test_save_to_file_more_args(self):
        self.assertRaises(TypeError, Square.save_to_file, [], 1)

    def test_save_to_file_no_args(self):
        self.assertRaises(TypeError, Rectangle.save_to_file)


class Test_from_json_string(unittest.TestCase):
    """Test from_json_string"""

    def test_from_json_string_with_empty_string(self):
        result = Base.from_json_string("")
        self.assertEqual(result, [])

    def test_from_json_string_with_none(self):
        result = Base.from_json_string(None)
        self.assertEqual(result, [])

    def test_from_json_string_with_json_string(self):
        json_str = '[{"id": 1, "width": 3}, {"id": 2, "width": 4}]'
        expected = [{"id": 1, "width": 3}, {"id": 2, "width": 4}]
        result = Base.from_json_string(json_str)
        self.assertEqual(result, expected)

    def test_from_json_string_with_more_args(self):
        self.assertRaises(TypeError, Base.from_json_string, [], 1)

    def test_from_json_string_no_args(self):
        self.assertRaises(TypeError, Base.from_json_string)

    def test_from_json_string_square(self):
        expected = [{"id": 4, "width": 10, "height": 2, "y": 4}]
        json_list = Square.to_json_string(expected)
        result = Square.from_json_string(json_list)
        self.assertEqual(result, expected)


class Test_create(unittest.TestCase):
    """Test create of Base.create"""

    def test_create_rectangle(self):
        r = Rectangle(2, 3, 4, 6, 9)
        r_dict = r.to_dictionary()
        r1 = Rectangle.create(**r_dict)
        self.assertEqual("[Rectangle] (9) 4/6 - 2/3", str(r))
        self.assertEqual("[Rectangle] (9) 4/6 - 2/3", str(r1))
        self.assertEqual(str(r), str(r1))
        self.assertIsNot(r, r1)


class Test_load_from_file(unittest.TestCase):
    """Unittest for the Base class method load_from_file"""

    def tearDown(self):
        """cleans up files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_none_file(self):
        Rectangle.save_to_file(None)
        r = Rectangle.load_from_file()
        self.assertEqual(type(r), list)
        self.assertEqual(len(r), 0)

    def test_load_from_file(self):
        r = Rectangle(10, 7, 2, 8, 12)
        r1 = Rectangle(3, 4, 5, 7, 2)
        Rectangle.save_to_file([r, r1])
        rect = Rectangle.load_from_file()
        self.assertEqual(str(r), str(rect[0]))
        self.assertEqual(str(r1), str(rect[1]))

    def test_load_from_empty_file(self):
        Square.save_to_file([])
        result = Square.load_from_file()
        self.assertEqual(type(result), list)
        self.assertEqual(len(result), 0)
