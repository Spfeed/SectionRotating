import unittest
from src.draw_module import Draw_module
from unittest.mock import Mock

class TestDrawModule(unittest.TestCase):


    def test_rotate(self):
        canvas=Mock()
        draw_module=Draw_module(canvas)
        canvas.delete.return_value = None

        section=(100,100,200,100)
        rotation_point=(150,100)
        angular_speed=90
        draw_module.section_rotation(section,rotation_point,angular_speed)

        canvas.create_line.assert_called_once_with(150.0, 50.0, 150.0, 150.0, tags='line', fill='blue', width=2)

if __name__=='__main__':
    unittest.main()