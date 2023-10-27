from tkinter_module import Tkinter_module
from input import Input
from draw_module import Draw_module
from controller_module import Controller_module

tkinter_module=Tkinter_module()
input=Input()
draw_module=Draw_module(tkinter_module.canvas)
controller=Controller_module(input,draw_module,tkinter_module)
tkinter_module.run()