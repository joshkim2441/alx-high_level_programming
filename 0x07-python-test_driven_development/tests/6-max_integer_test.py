#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittest class for max_integer"""
    def test_module_docstring(self):
        """Tests for module docsting"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """Tests for empty list []"""
        empty = []
        self.assertIsNone(max_integer(empty))

    def test_no_args(self):
        """Tests for no arguments passed to func"""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """Tests for only one number in the list"""
        one_element = [1]
        self.assertEqual(max_integer(one_element), 1)

    def test_positive_end(self):
        """Tests for all positive with max at end"""
        pos_end = [3, 20, 9, 39, 16, 40]
        self.assertEqual(max_integer(pos_end), 40)

    def test_positive_middle(self):
        """Tests for all positive with max in middle"""
        pos_mid = [3, 20, 9, 250, 18, 60]
        self.assertEqual(max_integer(pos_mid), 250)

    def test_positive_beginning(self):
        """Tests for all positive with max at beginning"""
        pos_begin = [300, 20, 9, 38, 17, 80]
        self.assertEqual(max_integer(pos_begin), 300)

    def test_one_negative(self):
        """Tests for list with one negative number"""
        one_neg = [300, 20, 9, -46, 19, 70]
        self.assertEqual(max_integer(one_neg), 300)

    def test_all_negative(self):
        """Tests for list with all negative numbers"""
        all_neg = [-8, -70, -95, -1, -150]
        self.assertEqual(max_integer(all_neg), -1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """Tests for a non-int type in list"""
        string = [4, 5, "Hello", 7, 8]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()
