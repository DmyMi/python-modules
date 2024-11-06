"""
This test suite runs tests for testing.package.example module.
"""

import unittest # python standard library. No need to install

# You can use relative package in normal case
# this works for notebook example
from testing.package.example import *

class TestExample(unittest.TestCase):
    def test_addition(self):
        result = testable_function(2, 2, sum)
        self.assertEqual(result, 4)
    
    def test_substraction(self):
        result = testable_function(2, 2, minus)
        self.assertEqual(result, 0)
    
    def test_error(self):
        with self.assertRaises(ValueError) as context:
            testable_function(1,2, sum)
        self.assertEqual(str(context.exception), "a cannot be less than b")

    def setUp(self):
        print("Run before every test")
    
    @classmethod
    def setUpClass(cls):
        print("Run once before tests")
    
    def tearDown(self):
        print("Run after every test")
    
    @classmethod
    def tearDownClass(cls):
        print("Run once after tests")

if __name__ == '__main__':
    unittest.main()