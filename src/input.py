class Input:

    def inputed_values_transform(self,x_start,y_start,x_end,y_end,x_rotation,y_rotation,angular_speed):
        x_start=float(x_start)
        y_start=float(y_start)
        x_end=float(x_end)
        y_end=float(y_end)
        x_rotation=float(x_rotation)
        y_rotation=float(y_rotation)
        angular_speed=float(angular_speed)

        return x_start, y_start, x_end, y_end, x_rotation, y_rotation, angular_speed