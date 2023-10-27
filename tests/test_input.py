import unittest
from src.input import Input

class TestInput(unittest.TestCase):

    def test_inputed_values_transform(self):
        x_start="50"
        y_start="200"
        x_end="300"
        y_end="200"
        x_rotate="150"
        y_rotate="200"
        angular_speed="5"
        input=Input()
        res=input.inputed_values_transform(x_start,y_start,x_end,y_end,x_rotate,y_rotate,angular_speed)
        expected=(50,200,300,200,150,200,5)
        self.assertEqual(res,expected)

if __name__== '__main__':
    unittest.main()