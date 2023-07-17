#!/usr/bin/python3
"""Unittest cases for the Rectangle class which is a subclass of Base clas"""
from models.rectangle import Rectangle
from models.base import Base
import unittest
import io
import sys
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """Unittest for the rectangle class"""

    def test_init_with_valid_arguments(self):
        r = Rectangle(5, 10, 1, 2, 15)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 15)

    def test_rectangle_is_instance_of_base(self):
        self.assertIsInstance(Rectangle(4, 3), Base)

    def test_is_rectangle_class(self):
        r = Rectangle(10, 3, 4, 5, 90)
        self.assertEqual(type(r), Rectangle)

    def test_with_too_many_args(self):
        self.assertRaises(TypeError, Rectangle, 1, 2, 3, 4, 5, 6)

    def test_init_with_no_args_or_one_arg(self):
        self.assertRaises(TypeError, Rectangle)
        self.assertRaises(TypeError, Rectangle, None)
        self.assertRaises(TypeError, Rectangle, 1)

    def test_init_with_invalid_arguments(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 1, 2, 3, 4)
            Rectangle([1, 2], 3, 4, 5, 6)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {"a": 10}, 3, 4, 5)
            Rectangle(4, (1, 2), 3, 4, 5)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 1, {20, 2}, 3, 4)
            Rectangle(10, 3, True, 5, 6)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 1, 4, None, 5)
            Rectangle(10, 1, 4, "3", 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-1, 2, 4, 5, 7)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0, 5, 6, 98)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(3, 4, -4, 8, 9)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(4, 5, 6, -1, 98)

    def test_with_less_args_given(self):
        r = Rectangle(10, 9)
        r1 = Rectangle(10, 9, 8)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 9)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, r1.id - 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 9)
        self.assertEqual(r1.x, 8)
        self.assertEqual(r1.y, 0)

    def test_private_attributes(self):
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_area(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        with io.StringIO() as buffr, redirect_stdout(buffr):
            Rectangle(4, 2).display()
            b = buffr.getvalue()
        self.assertEqual(b, '####\n####\n')
        with io.StringIO() as buffr, redirect_stdout(buffr):
            Rectangle(4, 2, 1, 2).display()
            b = buffr.getvalue()
        self.assertEqual(b, '\n\n ####\n ####\n')

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 1, 2, 15)
        expected = {"id": 15, "width": 5, "height": 10, "x": 1, "y": 2}
        self.assertEqual(r.to_dictionary(), expected)

    def test_str(self):
        r = Rectangle(5, 10, 1, 2, 15)
        expected = "[Rectangle] (15) 1/2 - 5/10"
        self.assertEqual(str(r), expected)

    def test_update_with_args(self):
        r = Rectangle(5, 10, 1, 2, 15)
        r.update(20, 8, 12, 3, 4)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
        self.assertEqual(str(r), '[Rectangle] (20) 3/4 - 8/12')

    def test_update_with_args_with_invalid_args(self):
        r = Rectangle(5, 10, 1, 2, 15)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(20, "8", 12, 3, 4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(20, 8, 0, 12, 3, 4)

    def test_update_with_kwargs(self):
        r = Rectangle(5, 10, 1, 2, 15)
        r.update(id=20, width=8, height=12, x=3, y=4)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 12)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
