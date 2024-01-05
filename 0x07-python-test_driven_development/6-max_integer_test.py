#!/usr/bin/python3
"""The unittest for max_integer([..])"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """max_integer unittest class"""
    def test_module_docstring(self):
        """Tests the module docstring"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Tests the function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        """Test for empty list"""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test for single elements in list"""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_positive_integers(self):
        """Test for multiple positive ints"""
        self.assertEqual(max_integer([3, 7, 1, 9]), 9)

    def test_multiple_negative_integers(self):
        """Test for multiple negative ints"""
        self.assertEqual(max_integer([-5, -2, -8, -1]), -1)

    def test_mixed_integers(self):
        """Test for mixed types"""
        self.assertEqual(max_integer([-3, 4, 1, -2, 6]), 6)

    def test_duplicate_maximum_values(self):
        """Test for duplicate maximum types"""
        self.assertEqual(max_integer([4, 2, 4, 1]), 4)

    def test_non_integer_inputs(self):
        """Test for non_integer types"""
        with self.asserRaises(TypeError):
            max_integer([1, 'a', 3])

    def test_single_string_input(self):
        """Test for single string input"""
        with self.assertRaises(TypeError):
            max_integer('hello')

__name__ == '__main__':
 unittest.main()
