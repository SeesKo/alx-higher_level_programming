#!/usr/bin/python3
"""
Unit tests for the `Rectangle` class.
"""

import io
import unittest
import unittest.mock
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        """
        Test Rectangle constructor.
        """
        r = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 5)

    def test_area(self):
        """
        Test Rectangle area method.
        """
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        """
        Test Rectangle display method.
        """
        r = Rectangle(3, 4, 1, 2)
        expected_output = "\n\n ###\n ###\n ###\n ###\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """
        Test Rectangle __str__ method.
        """
        r = Rectangle(3, 4, 1, 2, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 1/2 - 3/4")

    def test_to_dictionary(self):
        """
        Test Rectangle to_dictionary method.
        """
        r = Rectangle(3, 4, 1, 2, 5)
        expected_dict = {'id': 5, 'width': 3, 'height': 4, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_update(self):
        """
        Test Rectangle update method.
        """
        r = Rectangle(3, 4, 1, 2, 5)
        r.update(6, 7, 8, 9, 10)
        self.assertEqual(r.id, 6)
        self.assertEqual(r.width, 7)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)

    def test_invalid_width(self):
        """
        Test case: width is not an integer.
        """
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 4, 1, 2, 5)

    def test_negative_width(self):
        """
        Test case: width is a negative value.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(-3, 4, 1, 2, 5)

    def test_invalid_height(self):
        """
        Test case: height is not an integer.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(3, "invalid", 1, 2, 5)

    def test_negative_height(self):
        """
        Test case: height is a negative value.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(3, -4, 1, 2, 5)

    def test_invalid_x(self):
        """
        Test case: x is not an integer.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(3, 4, "invalid", 2, 5)

    def test_negative_x(self):
        """
        Test case: x is a negative value.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(3, 4, -1, 2, 5)

    def test_invalid_y(self):
        """
        Test case: y is not an integer.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(3, 4, 1, "invalid", 5)

    def test_negative_y(self):
        """
        Test case: y is a negative value.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(3, 4, 1, -2, 5)

    def test_invalid_id(self):
        """
        Test case: id is not an integer.
        """
        with self.assertRaises(TypeError):
            r = Rectangle(3, 4, 1, 2, "invalid_id")

    def test_negative_id(self):
        """
        Test case: id is a negative value.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(3, 4, 1, 2, -5)

    def test_zero_width(self):
        """
        Test case: width is zero.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 4, 1, 2, 5)

    def test_zero_height(self):
        """
        Test case: height is zero.
        """
        with self.assertRaises(ValueError):
            r = Rectangle(3, 0, 1, 2, 5)

    def test_zero_x(self):
        """
        Test case: x is zero.
        """
        r = Rectangle(3, 4, 0, 2, 5)
        self.assertEqual(r.x, 0)

    def test_zero_y(self):
        """
        Test case: y is zero.
        """
        r = Rectangle(3, 4, 1, 0, 5)
        self.assertEqual(r.y, 0)

    def test_width_setter_invalid_type(self):
        """
        Test case: invalid type in width setter.
        """
        r = Rectangle(3, 4, 1, 2, 5)
        with self.assertRaises(TypeError):
            r.width = "invalid_width"

    def test_height_setter_invalid_type(self):
        """
        Test case: invalid type in height setter.
        """
        r = Rectangle(3, 4, 1, 2, 5)
        with self.assertRaises(TypeError):
            r.height = "invalid_height"

    def test_x_setter_invalid_type(self):
        """
        Test case: invalid type in x setter.
        """
        r = Rectangle(3, 4, 1, 2, 5)
        with self.assertRaises(TypeError):
            r.x = "invalid_x"

    def test_y_setter_invalid_type(self):
        """
        Test case: invalid type in y setter.
        """
        r = Rectangle(3, 4, 1, 2, 5)
        with self.assertRaises(TypeError):
            r.y = "invalid_y"

    def test_area_after_resize(self):
        """
        Test case: calculating area after resizing.
        """
        r = Rectangle(3, 4, 1, 2, 5)
        r.width = 5
        r.height = 6
        self.assertEqual(r.area(), 30)

    def test_display_with_offset(self):
        """
        Test case: display with x and y offsets.
        """
        r = Rectangle(3, 4, 2, 1)
        expected_output = "\n  ###\n  ###\n  ###\n  ###\n"
        with unittest.mock.patch(
                'sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()
