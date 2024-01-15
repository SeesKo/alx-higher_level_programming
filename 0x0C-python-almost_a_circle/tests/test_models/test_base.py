#!/usr/bin/python3
"""
Unit tests for the `Base` class.
"""

import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test case for the Base class.
    """
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_constructor_with_id(self):
        """
        Test constructor when id is provided.
        """
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_constructor_without_id(self):
        """
        Test constructor when id is not provided.
        """
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_constructor_with_negative_id(self):
        """
        Test constructor with a negative id.
        """
        obj = Base(-5)
        self.assertEqual(obj.id, -5)

    def test_constructor_with_float_id(self):
        """
        Test constructor with a float id.
        """
        obj = Base(3.14)
        self.assertEqual(obj.id, 3.14)

    def test_constructor_with_string_id(self):
        """
        Test constructor with a string id.
        """
        obj = Base("hello")
        self.assertEqual(obj.id, "hello")

    def test_constructor_with_zero_id(self):
        """
        Test constructor with a zero id.
        """
        obj = Base(0)
        self.assertEqual(obj.id, 0)

    def test_constructor_with_large_id(self):
        """
        Test constructor with a large id.
        """
        obj = Base(999999999)
        self.assertEqual(obj.id, 999999999)

    def test_constructor_with_multiple_instances(self):
        """
        Test constructor with multiple instances.
        """
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_to_json_string_empty_list(self):
        """
        Test to_json_string with an empty list.
        """
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_non_empty_list(self):
        """
        Test to_json_string with a non-empty list.
        """
        data = [{"name": "Tom", "age": 30}, {"name": "Ann", "age": 25}]
        result = Base.to_json_string(data)
        expected_result = (
                '[{"name": "Tom", "age": 30}, '
                '{"name": "Ann", "age": 25}]'
                )
        self.assertEqual(result, expected_result)

    def test_save_to_file_empty_list(self):
        """
        Test save_to_file with an empty list.
        """
        Base.save_to_file([])
        with open("Base.json", "r") as file:
            content = file.read()
        self.assertEqual(content, "[]")
        # Clean up the created file
        os.remove("Base.json")

    def test_from_json_string_invalid_json(self):
        """
        Test from_json_string with invalid JSON input.
        """
        with self.assertRaises(ValueError):
            Base.from_json_string("invalid_json")

    def test_create_with_dictionary(self):
        """
        Test create method with a dictionary.
        """
        data = {"id": 42, "width": 5, "height": 10}
        obj = Rectangle.create(**data)
        self.assertEqual(obj.id, 42)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 10)

    def test_load_from_file_not_exists(self):
        """
        Test load_from_file when the file does not exist.
        """
        loaded_objs = Base.load_from_file()
        self.assertEqual(loaded_objs, [])

    def test_load_from_file_empty_file(self):
        """
        Test load_from_file when the file exists but is empty.
        """
        with open("Square.json", "w") as file:
            file.write("")
        loaded_objs = Base.load_from_file()
        self.assertEqual(loaded_objs, [])
        # Clean up the created file
        os.remove("Square.json")

    def test_create_with_invalid_parameters(self):
        """
        Test the creation of a Rectangle instance
        with invalid parameters.
        """
        with self.assertRaises(ValueError):
            obj = Rectangle.create(
                    id="string_id",
                    width="invalid_width",
                    height="invalid_height"
                    )

    def tearDown(self):
        """
        Clean-up method executed after each test case.
        """
        # Cleaning up the created file if it exists
        file_path = "file_with_special_chars_@#$%.json"
        if os.path.exists(file_path):
            os.remove(file_path)

    def test_constructor_with_max_positive_int_id(self):
        """
        Test constructor with the maximum positive integer value as id.
        """
        obj = Base(2147483647)  # Max positive int value
        self.assertEqual(obj.id, 2147483647)

    def test_constructor_with_min_negative_int_id(self):
        """
        Test constructor with the minimum negative integer value as id.
        """
        obj = Base(-2147483648)  # Min negative int value
        self.assertEqual(obj.id, -2147483648)

    def test_constructor_with_max_positive_float_id(self):
        """
        Test constructor with the maximum positive float value as id.
        """
        obj = Base(3.4028235e38)  # Max positive float value
        self.assertEqual(obj.id, 3.4028235e38)

    def test_constructor_with_min_negative_float_id(self):
        """
        Test constructor with the minimum negative float value as id.
        """
        obj = Base(-3.4028235e38)  # Min negative float value
        self.assertEqual(obj.id, -3.4028235e38)

    def test_to_json_string_with_special_chars(self):
        """
        Test to_json_string with a dictionary containing special characters.
        """
        data = [{"name": "@!#%", "age": 30}, {"name": "$%^&", "age": 25}]
        result = Base.to_json_string(data)
        expected_result = (
                '[{"name": "@!#%", "age": 30}, '
                '{"name": "$%^&", "age": 25}]'
                )
        self.assertEqual(result, expected_result)

    def test_create_with_optional_attributes(self):
        """
        Test create method with a dictionary containing a mix
        of required and optional attributes.
        """
        data = {"id": 42, "width": 5, "height": 10}

        # Ensure that only integer values are passed to create
        for key, value in data.items():
            data[key] = int(value)

        obj = Rectangle.create(**data)
        self.assertEqual(obj.id, 42)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 10)

    def test_load_from_file_with_nonexistent_file(self):
        """
        Test load_from_file when the file does not exist.
        """
        loaded_objs = Base.load_from_file()
        self.assertEqual(loaded_objs, [])

    def test_load_from_file_with_special_chars_in_filename(self):
        """
        Test load_from_file when the file exists but has
        special characters in the filename.
        """
        test_file_name = "temp_special_chars_file.json"
        Base.save_to_file([], test_file_name)
        self.assertTrue(
                os.path.exists(test_file_name),
                "File not created successfully"
                )
        loaded_objs = Base.load_from_file()
        self.assertEqual(loaded_objs, [])
        if os.path.exists(test_file_name):
            os.remove(test_file_name)


if __name__ == '__main__':
    unittest.main()
