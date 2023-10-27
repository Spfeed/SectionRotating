import tkinter as tk
from utils_module import about

class Tkinter_module:

    def __init__(self):
        self.root=tk.Tk()
        self.root.title("Вращение отрезка с выбранной угловой скоростью вокруг заданной точки")
        self.width=800
        self.height=800
        width_screen=self.root.winfo_screenwidth()
        height_screen=self.root.winfo_screenheight()
        x_pack=(width_screen-self.width)//2
        y_pack=(height_screen-self.height)//2
        self.root.geometry(f"{self.width}x{self.width}+{x_pack}+{y_pack}")
        self.canvas=tk.Canvas(self.root, width=self.width, height=self.height-300, bg="white")
        self.canvas.pack(side="top")
        self.input_area=tk.Frame(self.root)
        self.input_area.pack()

        self.label_x_start = tk.Label(self.input_area, text="x_start:")
        self.entry_x_start = tk.Entry(self.input_area)
        self.label_y_start = tk.Label(self.input_area, text="y_start:")
        self.entry_y_start = tk.Entry(self.input_area)

        self.label_x_end = tk.Label(self.input_area, text="x_end:")
        self.entry_x_end = tk.Entry(self.input_area)
        self.label_y_end = tk.Label(self.input_area, text="y_end:")
        self.entry_y_end = tk.Entry(self.input_area)

        self.label_x_rotation = tk.Label(self.input_area, text="x_rotation:")
        self.entry_x_rotation = tk.Entry(self.input_area)
        self.label_y_rotation = tk.Label(self.input_area, text="y_rotation:")
        self.entry_y_rotation = tk.Entry(self.input_area)

        self.label_angular_speed = tk.Label(self.input_area, text="angular_speed:")
        self.entry_angular_speed = tk.Entry(self.input_area)

        self.label_x_start.grid(row=0, column=0)
        self.entry_x_start.grid(row=0, column=1)
        self.label_y_start.grid(row=0, column=2)
        self.entry_y_start.grid(row=0, column=3)

        self.label_x_end.grid(row=1, column=0)
        self.entry_x_end.grid(row=1, column=1)
        self.label_y_end.grid(row=1, column=2)
        self.entry_y_end.grid(row=1, column=3)

        self.label_x_rotation.grid(row=2, column=0)
        self.entry_x_rotation.grid(row=2, column=1)
        self.label_y_rotation.grid(row=2, column=2)
        self.entry_y_rotation.grid(row=2, column=3)

        self.label_angular_speed.grid(row=3, column=0, columnspan=2)
        self.entry_angular_speed.grid(row=3, column=2, columnspan=2)

        self.menu_bar=tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.main_menu=tk.Menu(self.menu_bar)
        self.menu_bar.add_command(label="О программе", command=about)
        #self.file_menu.add_command(label="Версия", command=version)

        self.root.bind('<Escape>', self.close_window)

    def get_inputed_values(self):
        return self.entry_x_start.get(), self.entry_y_start.get(), self.entry_x_end.get(), self.entry_y_end.get(), self.entry_x_rotation.get(), self.entry_y_rotation.get(), self.entry_angular_speed.get()

    def close_window(self):
        self.root.destroy()

    def create_button(self,txt,function):
        button=tk.Button(self.input_area, text=txt, command=function)
        button.grid(row=4, column=0, columnspan=4)

    def run(self):
        self.root.mainloop()



