import math #math library has pre-written 
import unittest

def circleArea(radius):
    """Return the area of a circle"""
    return math.pi * radius * radius

def rectArea(base, height):
    """Return the area of a rect"""
    return base * height 

def trapArea(base1, base2, height):
    """Return the area of a trapezoid"""
    return base1 + base2 * 1/2 * height 

def triArea(base,height):
    """Return the area of a tri"""
    return base * height /2
    
	
class MyTest(unittest.TestCase):
    def testCircleArea(self):
        self.assertEqual(circleArea(5), 25*math.pi)
    #def testRectArea(self):
    
    #def testTrapArea(self):
    
    def testTriArea(self):
    self.assertEqual(triArea(3,3), 4.
    self.assertAlmostEqual(triArea(4.
    
    