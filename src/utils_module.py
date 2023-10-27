import tkinter as  tk
from tkinter import messagebox
import requests

def about():
    """
    Открывает окно "О приложении" и отображает его описание.
    Функция создает окно, отображающее информацию о приложении.
    Информация о приложении содержится в файле about.txt, находящемся по адресу: utils/about.txt.

    """
    about_wind=tk.Toplevel()
    about_wind.title("О приложении")
    about_txt=tk.Text(about_wind, height=40, width=70)
    about_txt.pack()
    with open("utils/about.txt","r", encoding="utf-8") as fin:
        about_txt.insert(tk.END, fin.read())


