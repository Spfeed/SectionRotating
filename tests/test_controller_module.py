import unittest
from src.controller_module import Controller_module
from unittest.mock import Mock

class TestConrollerModule(unittest.TestCase):

    def setUp(self):
        self.input_module = Mock()
        self.draw_module = Mock()
        self.tkinter_module = Mock()
        self.controller_module=Controller_module(self.input_module,self.draw_module,self.tkinter_module)

    def test_check_rotate_point_true(self):
        result_inside = self.controller_module.check_rotate_point(1, 1, 3, 3, 2, 2)
        self.assertTrue(result_inside)

    def test_check_rotate_point_false(self):
        result_inside = self.controller_module.check_rotate_point(1, 1, 3, 3, 2, 2)
        self.assertTrue(result_inside)

    def test_rotate(self):
        self.tkinter_module.get_inputed_values.return_value = (100, 100, 200, 100, 150, 100, 90)
        self.input_module.inputed_values_transform.return_value=(100, 100, 200, 100, 150, 100, 90)
        self.controller_module.rotate()

        self.draw_module.section_rotation.assert_called_once_with((100, 100, 200, 100), (150, 100), 90)

if __name__ == '__main__':
    unittest.main()