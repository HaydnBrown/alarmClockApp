import sys
import datetime
import time
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import tkinter.ttk as ttk
from functools import partial


class Application(Tk):
    def __init__(self):
        print("Starting application....")
        print("the time is.....", datetime.datetime.now().strftime("%H:%M:%S"))
        super(Application, self).__init__()
        self.title("Alarm Clock application")
        self.minsize(500, 400)
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self).grid(column=0, row=0, sticky=(N, W, E, S))
        label_hours = ttk.Label(main_frame, text="Hours")
        label_hours.grid(column=1, row=0, sticky=S)
        label_minutes = ttk.Label(main_frame, text="Minutes")
        label_minutes.grid(column=2, row=0, sticky=S)
        label_seconds = ttk.Label(main_frame, text="Seconds")
        label_seconds.grid(column=3, row=0, sticky=S)

        entry_hours = ttk.Entry(main_frame)
        entry_hours.grid(column=1, row=1)
        entry_minutes = ttk.Entry(main_frame)
        entry_minutes.grid(column=2, row=1)
        entry_seconds = ttk.Entry(main_frame)
        entry_seconds.grid(column=3, row=1)

        submit_button = ttk.Button(main_frame, text="Set Alarm",
                                   command=partial(self.start_timer, entry_hours, entry_minutes, entry_seconds))
        submit_button.grid(column=2, row=3)

    def start_timer(self, h, m, s):
        print("starting timer...")
        alarm_time = f"{int(h.get()):02d}:{int(m.get()):02d}:{int(s.get()):02d}"
        print("alarm time: ", alarm_time)
        while True:
            time.sleep(1)
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("the current time is: ", current_time)
            if current_time == alarm_time:
                self.popup_win()
                break

    def popup_win(self):
        popup = tk.Tk()
        popup.wm_title("!")
        popup.minsize(300, 250)
        label = ttk.Label(popup, text="Your alarm has gone off!")
        label.pack(side="top", fill="x", pady=10)
        b1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        b1.pack()
        popup.mainloop()


root = Application()
root.mainloop()
