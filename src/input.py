class Input:
    """
        Класс Input предоставляет метод для преобразования введенных пользователем значений в числовой формат.

        Методы:
            inputed_values_transform(x_start, y_start, x_end, y_end, x_rotation, y_rotation, angular_speed):
                Преобразует введенные значения в числовой формат.

        """
    def inputed_values_transform(self,x_start,y_start,x_end,y_end,x_rotation,y_rotation,angular_speed):
        """
                Преобразует введенные значения в числовой формат.

                Аргументы:
                    x_start (str): Значение x-координаты начала отрезка.
                    y_start (str): Значение y-координаты начала отрезка.
                    x_end (str): Значение x-координаты конца отрезка.
                    y_end (str): Значение y-координаты конца отрезка.
                    x_rotation (str): Значение x-координаты точки вращения.
                    y_rotation (str): Значение y-координаты точки вращения.
                    angular_speed (str): Значение угловой скорости вращения.

                Возвращает:
                    Кортеж с числовыми значениями (x_start, y_start, x_end, y_end, x_rotation, y_rotation, angular_speed).
                """
        x_start=float(x_start)
        y_start=float(y_start)
        x_end=float(x_end)
        y_end=float(y_end)
        x_rotation=float(x_rotation)
        y_rotation=float(y_rotation)
        angular_speed=float(angular_speed)

        return x_start, y_start, x_end, y_end, x_rotation, y_rotation, angular_speed