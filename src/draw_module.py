import math

class Draw_module:
    """
       Класс Draw_module предоставляет методы для визуализации вращения отрезка на холсте.

       Атрибуты:
           canvas (tk.Canvas): Холст, на котором происходит визуализация.
           line: Объект отрезка, отображаемого на холсте.

       Методы:
           __init__(canvas): Инициализация класса с заданным холстом.
           section_rotation(line, rotation_point, angular_speed): Визуализирует вращение отрезка на холсте.

       """
    def __init__(self,canvas):
        """
        Инициализация класса с заданным холстом.

        Аргументы:
            canvas (tk.Canvas): Холст, на котором происходит визуализация.
        """
        self.canvas=canvas
        self.line=None

    def section_rotation(self,line,rotation_point,angular_speed):
        """
        Визуализирует вращение отрезка на холсте.

        Аргументы:
            line (tuple): Кортеж с координатами начала и конца отрезка (x_start, y_start, x_end, y_end).
            rotation_point (tuple): Координаты точки вращения (x_rotate, y_rotate).
            angular_speed (float): Угловая скорость вращения в градусах в секунду.

        Описание:
            Данный метод осуществляет вращение отрезка с заданными координатами начала и конца
            вокруг заданной точки с указанной угловой скорость. Поворот производится на угол,
            равный параметру угловой скорости. Старый отрезок удаляется, строится новый. Метод
            является рекурсивным и вызывается каждые 10 милисекнуд.
        """
        x_start,y_start,x_end,y_end=line
        x_rotate,y_rotate=rotation_point
        radian_angle=math.radians(angular_speed)
        moved_x_start=x_rotate+(x_start-x_rotate)*math.cos(radian_angle)-(y_start-y_rotate)*math.sin(radian_angle)
        moved_y_start=y_rotate+(x_start-x_rotate)*math.sin(radian_angle)+(y_start-y_rotate)*math.cos(radian_angle)
        moved_x_end=x_rotate+(x_end-x_rotate)*math.cos(radian_angle)-(y_end-y_rotate)*math.sin(radian_angle)
        moved_y_end=y_rotate+(x_end-x_rotate)*math.sin(radian_angle)+(y_end-y_rotate)*math.cos(radian_angle)
        self.canvas.delete('line')
        self.line=self.canvas.create_line(moved_x_start,moved_y_start,moved_x_end,moved_y_end, tags='line', fill='blue', width=2)
        self.canvas.after(10, self.section_rotation, (moved_x_start,moved_y_start,moved_x_end,moved_y_end), (x_rotate,y_rotate), angular_speed)