#!/usr/bin/python3
"""
Unit tests for the `Square` class.
"""

import unittest
import unittest.mock
import io
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """
    def test_constructor(self):
        """
        Test the constructor of the Square class.
        """
        square = Square(5, 1, 2, 10)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 1)
        self.assertEqual(square.y, 2)
        self.assertEqual(square.id, 10)

    def test_str_method(self):
        """
        Test the __str__ method of the Square class.
        """
        square = Square(3, 4, 5, 15)
        self.assertEqual(str(square), "[Square] (15) 4/5 - 3")

    def test_size_setter(self):
        """
        Test the size setter.
        """
        square = Square(3, 4, 5, 15)
        square.size = 7
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)

    def test_size_setter_invalid_type(self):
        """
        Test case for invalid type in size setter.
        """
        square = Square(3, 4, 5, 15)
        with self.assertRaises(TypeError):
            square.size = "invalid_size"

    def test_update_method(self):
        """
        Test the update method.
        """
        square = Square(3, 4, 5, 15)
        square.update(20, 6, 7, 8)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_update_method_with_args(self):
        """
        Test the update method with *args.
        """
        square = Square(3, 4, 5, 15)
        square.update(20, 6, 7, 8)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_update_method_with_kwargs(self):
        """
        Test the update method with **kwargs.
        """
        square = Square(3, 4, 5, 15)
        square.update(size=6, x=7, y=8, id=20)
        self.assertEqual(square.id, 20)
        self.assertEqual(square.size, 6)
        self.assertEqual(square.x, 7)
        self.assertEqual(square.y, 8)

    def test_to_dictionary_method(self):
        """
        Test the to_dictionary method.
        """
        square = Square(3, 4, 5, 15)
        expected_dict = {'id': 15, 'size': 3, 'x': 4, 'y': 5}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_size_setter_negative_value(self):
        """
        Test case for setting size to a negative value.
        """
        square = Square(3, 4, 5, 15)
        with self.assertRaises(ValueError):
            square.size = -2

    def test_size_setter_zero_value(self):
        """
        Test case for setting size to zero.
        """
        square = Square(3, 4, 5, 15)
        with self.assertRaises(ValueError):
            square.size = 0

    def test_x_setter_negative_value(self):
        """
        Test case for setting x to a negative value.
        """
        square = Square(3, 4, 5, 15)
        with self.assertRaises(ValueError):
            square.x = -2

    def test_y_setter_negative_value(self):
        """
        Test case for setting y to a negative value.
        """
        square = Square(3, 4, 5, 15)
        with self.assertRaises(ValueError):
            square.y = -2

    def test_update_method_with_negative_size(self):
        """
        Test case for updating size to a negative value
        using update method.
        """
        square = Square(3, 4, 5, 15)
        with self.assertRaises(ValueError):
            square.update(size=-2)

    def test_update_method_with_negative_x(self):
        """
        Test case for updating x to a negative value using
        update method.
        """
        square = Square(3, 4, 5, 15)
        with self.assertRaises(ValueError):
            square.update(x=-2)

    def test_update_method_with_negative_y(self):
        """
        Test case for updating y to a negative value using
        update method.
        """
        square = Square(3, 4, 5, 15)
        with self.assertRaises(ValueError):
            square.update(y=-2)

    def test_area_after_resize(self):
        """
        Test case for calculating area after resizing.
        """
        square = Square(3, 4, 5, 15)
        square.size = 5
        self.assertEqual(square.area(), 25)

    def test_display(self):
        """
        Test the display method.
        """
        square = Square(3, 4, 5, 15)
        expected_output = "\n\n\n\n\n    ###\n    ###\n    ###\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_with_offset(self):
        """
        Test case for display with x and y offsets.
        """
        square = Square(3, 4, 5, 15)
        expected_output = "\n\n\n\n\n    ###\n    ###\n    ###\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_area_after_size_increase(self):
        """
        Test case for calculating area after increasing size.
        """
        square = Square(3, 4, 5, 15)
        square.size += 2
        self.assertEqual(square.area(), 25)

    def test_area_after_size_decrease(self):
        """
        Test case for calculating area after decreasing size.
        """
        square = Square(5, 2, 2, 20)
        square.size -= 2
        self.assertEqual(square.area(), 9)

    def test_update_method_invalid_arg(self):
        """
        Test case for update method with invalid argument.
        """
        square = Square(3, 4, 5, 15)
        with self.assertRaises(TypeError):
            square.update(size="invalid")

    def test_display_with_size_zero(self):
        """
        Test case for display method with size set to zero.
        """
        with self.assertRaises(ValueError):
            square = Square(0, 4, 5, 15)

    def test_display_with_size_one(self):
        """
        Test case for display method with size set to one.
        """
        square = Square(1, 4, 5, 15)
        expected_output = "\n\n\n\n\n    #\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_after_multiple_updates(self):
        """
        Test case for display method after multiple updates.
        """
        square = Square(3, 4, 5, 15)
        square.update(20, 2, 2, 2)
        expected_output = "\n\n  ##\n  ##\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
