# https://github.com/gregtwallace2/lab10-MFG-GTW
# Partner 1: Maria Guerra
# Partner 2: Gregory Wallace


import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######## Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2,2), 4)
        self.assertEqual(add(-5, -2), -7)
        self.assertEqual(add(-2, 3), 1)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(2, 2), 0)
        self.assertEqual(subtract(-5, -2), -3)
        self.assertEqual(subtract(-2, 3), -5)
    ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(2,5),10)
        self.assertEqual(mul(-4,5),-20)
        self.assertEqual(mul(0,10000),0)

    def test_divide(self):
        self.assertEqual(div(2,10),5.0)
        self.assertEqual(div(0.5,2.0),4.0)
        with self.assertRaises(ZeroDivisionError):
            div(0,100)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0,8)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 4),2)
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(2, 16), 4)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(0, 2)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(0,5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3,4),5.0)
        self.assertAlmostEqual(hypotenuse(5,12),13.0)
        self.assertAlmostEqual(hypotenuse(-6,-8),10.0)

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-9)
        self.asserAlmostEqual(square_root(9),3.0)
        self.assertAlmostEqual(square_root(0.25),0.5)
# Do not touch this
if __name__ == "__main__":
    unittest.main()