import sys
import datetime
import time
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import tkinter.ttk as ttk


class Application(Tk):
    def __init__(self):
        print("Starting application....")
        super(Application, self).__init__()
        self.title("Alarm Clock application")
        self.minsize(500, 400)
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self).grid(column=0, row=0, sticky=(N, W, E, S))
        label_hours = ttk.Label(main_frame, text="Hours").grid(column=1, row=0, sticky=S)
        label_minutes = ttk.Label(main_frame, text="Minutes").grid(column=2, row=0, sticky=S)
        label_seconds = ttk.Label(main_frame, text="Seconds").grid(column=3, row=0, sticky=S)
        entry_hours = ttk.Entry(main_frame).grid(column=1, row=1)
        entry_minutes = ttk.Entry(main_frame).grid(column=2, row=1)
        entry_seconds = ttk.Entry(main_frame).grid(column=3, row=1)

    def say_hi(self):
        print("Hello")


root = Application()
root.mainloop()

# def say_hi():
#     print("Hello...")
#
#
# root = Tk()
# root.title("Alarm Clock App")
# root.minsize(500, 450)
#
# main_frame = ttk.Frame(root)
# main_frame.grid(column=0, row=0)
#
# button1 = ttk.Button(main_frame, text="press me", command=say_hi).grid(column=0, row=0)
#
# root.mainloop()
