class Controller_module:

    def __init__(self,input_module,draw_module,tkinter_module):
        self.input_module=input_module
        self.draw_module=draw_module
        self.tkinter_module=tkinter_module
        self.input_module.inputed_values_transform=self.input_module.inputed_values_transform
        self.tkinter_module.create_button=tkinter_module.create_button("Ввод", self.rotate)

    def get_values(self):
        x_start,y_start,x_end,y_end,x_rotate,y_rotate, angular_speed=self.tkinter_module.get_inputed_values()
        return self.input_module.inputed_values_transform(x_start,y_start,x_end,y_end,x_rotate,y_rotate,angular_speed)

    def check_rotate_point(self, x_start,y_start,x_end,y_end, x_rotate, y_rotate):
        if (x_rotate-x_start)*(y_end-y_start) - (y_rotate-y_start)*(x_end-x_start) == 0:
            return True
        return False

    def rotate(self):

        x_start,y_start,x_end,y_end,x_rotate,y_rotate,angular_speed=self.get_values()
        # if not self.check_rotate_point(x_start,y_start,x_end,y_end,x_rotate,y_rotate):
        #     print("Указанная точка находится вне отрезка, вращение невозможно!")
        #     return
        self.draw_module.section_rotation((x_start,y_start,x_end,y_end),(x_rotate,y_rotate),angular_speed)