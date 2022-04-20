from tkinter.tix import IMAGETEXT
from DFA import Dfa
import tkinter as tk
from tkinter import ttk
from tkinter import*
from PIL import Image,ImageTk
import sys,re
print(sys.executable)
class screen2(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        from screen3 import screen3
        self.button1 = ttk.Button(self, text ="test",
        command = self.m)
        self.button1.place(x=10,y=300)
        self.name = StringVar()
        self.textEntry=Entry(self,textvariable=self.name,width=40,font=('Georgia 12'))
        self.textEntry.place(x=13,y=250,height=28)
        self.image = Image.open("D:\python codes\compilers\dfa.jpeg")
        self.python_image = ImageTk.PhotoImage(self.image.resize((800,450)))

        imagelabel =ttk.Label(self, image=self.python_image)
        imagelabel.place (x=550,y=100)
        self.resultLabel=ttk.Label(self,text="",font=('Helvetica 10 bold'))
        self.resultLabel.place(x=10,y=700)
    def m (self):
        String=self.textEntry.get()  
        x = re.findall(r"([(]|[)]|<=|=>|&&|[|]{2}|[<>=!]|[\w]+)", String)
        print(x)
        routes = []
        for i in range(len(x)):
            routes.append(x[i])
        dfa=Dfa()
        Token=dfa.Tokens(routes) 

        self.resultLabel.config(text=Token)
        


    