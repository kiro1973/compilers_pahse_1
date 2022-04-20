import tkinter as tk
from tkinter import ttk
from tkinter import*

from screen2 import screen2
class screen3(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.button1 = ttk.Button(self, text ="screen2",
        command = lambda:controller.show_frame(screen2))
        self.button1.place(x=10,y=600)