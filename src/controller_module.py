class Controller_module:
    """
       Класс Controller_module предоставляет контроль и управление вращением отрезка на холсте.

       Атрибуты:
           input_module: Объект модуля ввода данных.
           draw_module: Объект модуля визуализации отрезка.
           tkinter_module: Объект модуля пользовательского интерфейса Tkinter.

       Методы:
           __init__(input_module, draw_module, tkinter_module):
               Инициализация класса с указанными модулями.

           get_values():
               Получение введенных пользователем значений и преобразование их в числовой формат.

           check_rotate_point(x_start, y_start, x_end, y_end, x_rotate, y_rotate):
               Проверка, находится ли точка вращения на отрезке.

           rotate():
               Вызов метода вращения отрезка на холсте.

       """
    def __init__(self,input_module,draw_module,tkinter_module):
        """
        Инициализация класса с указанными модулями.

        Аргументы:
            input_module: Объект модуля ввода данных.
            draw_module: Объект модуля визуализации отрезка.
            tkinter_module: Объект модуля пользовательского интерфейса Tkinter.
        """
        self.input_module=input_module
        self.draw_module=draw_module
        self.tkinter_module=tkinter_module
        self.input_module.inputed_values_transform=self.input_module.inputed_values_transform
        self.tkinter_module.create_button=tkinter_module.create_button("Ввод", self.rotate)

    def get_values(self):
        """
        Получение введенных пользователем значений и преобразование их в числовой формат.

        Возвращает:
            Кортеж с числовыми значениями (x_start, y_start, x_end, y_end, x_rotate, y_rotate, angular_speed).
        """
        x_start,y_start,x_end,y_end,x_rotate,y_rotate, angular_speed=self.tkinter_module.get_inputed_values()
        return self.input_module.inputed_values_transform(x_start,y_start,x_end,y_end,x_rotate,y_rotate,angular_speed)

    def check_rotate_point(self, x_start,y_start,x_end,y_end, x_rotate, y_rotate):
        """
        Проверка, находится ли точка вращения на отрезке.

        Аргументы:
           x_start (float): Значение x-координаты начала отрезка.
           y_start (float): Значение y-координаты начала отрезка.
           x_end (float): Значение x-координаты конца отрезка.
           y_end (float): Значение y-координаты конца отрезка.
           x_rotate (float): Значение x-координаты точки вращения.
           y_rotate (float): Значение y-координаты точки вращения.

       Возвращает:
            True, если точка вращения находится на отрезке, в противном случае - False.
       """
        if (x_rotate-x_start)*(y_end-y_start) - (y_rotate-y_start)*(x_end-x_start) == 0:
            return True
        return False

    def rotate(self):
        """
        Вызов метода вращения отрезка на холсте.

        Описание:
            Метод вызывается при нажатии на кнопку "Ввод". Сначала производится
            проверка принадлежности точки вращения отрезку, затем выполняется
            метод вращения отрезка.

        """
        x_start,y_start,x_end,y_end,x_rotate,y_rotate,angular_speed=self.get_values()
        if not self.check_rotate_point(x_start,y_start,x_end,y_end,x_rotate,y_rotate):
             print("Указанная точка находится вне отрезка, вращение невозможно!")
             return
        self.draw_module.section_rotation((x_start,y_start,x_end,y_end),(x_rotate,y_rotate),angular_speed)