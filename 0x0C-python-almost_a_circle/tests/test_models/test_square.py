#!/usr/bin/python3
"""unittest for the Square class"""
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
import unittest
import io
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """Test cases for the Square class"""

    def test_is_instance_of_base(self):
        s = Square(5, 1, 2, 12)
        self.assertIsInstance(s, Base)

    def test_is_subclass_of_rectangle(self):
        self.assertTrue(issubclass(Square, Rectangle))

    def test_type(self):
        s = Square(5, 1, 2, 12)
        self.assertEqual(type(s), Square)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Square(5, 1, 2, 12, 7, 3)

    def test_no_args(self):
        self.assertRaises(TypeError, Square, None)
        self.assertRaises(TypeError, Square)

    def test_init_with_valid_args(self):
        s = Square(5, 1, 2, 15)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 15)

    def test_init_with_default_arg(self):
        s = Square(7)
        self.assertEqual(s.size, 7)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertTrue(s.id is not None)

    def test_int_with_invalid_args(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1,), 2, 5, 9)
            Square([1, 2], 4, 5, 6)
            Square({1, 3}, 5, 6, 2)
            Square(None)
            Square({"a": 3}, 3, 5, 5)
            Square("3", 4, 5, 6)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
            Square(0)

    def test_size_property(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_area(self):
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_str(self):
        s = Square(5, 1, 2, 15)
        expected = "[Square] (15) 1/2 - 5"
        self.assertEqual(str(s), expected)

    def test_to_dictionary(self):
        s = Square(5, 1, 2, 15)
        expected = {"id": 15, "size": 5, "x": 1, "y": 2}
        self.assertEqual(s.to_dictionary(), expected)

    def test_update_with_args(self):
        s = Square(5, 1, 2, 15)
        s.update(20, 8, 3, 4)
        self.assertEqual(s.id, 20)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        self.assertEqual(str(s), '[Square] (20) 3/4 - 8')

    def test_update_with_kwargs(self):
        s = Square(5, 1, 2, 15)
        s.update(id=20, size=8, x=3, y=4)
        self.assertEqual(s.id, 20)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)
        self.assertEqual(str(s), '[Square] (20) 3/4 - 8')

    def test_display(self):
        with io.StringIO() as buffr, redirect_stdout(buffr):
            Square(3).display()
            b = buffr.getvalue()
        self.assertEqual(b, '###\n###\n###\n')
        with io.StringIO() as buffr, redirect_stdout(buffr):
            Square(3, 1, 2).display()
            b = buffr.getvalue()
        self.assertEqual(b, '\n\n ###\n ###\n ###\n')
