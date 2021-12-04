import tkinter as tk

from Third import ThirdPage

import sqlite3
class UserHomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button = tk.Button(self, text="UserHomePAge", command=lambda: controller.change_frame(ThirdPage))
        button.grid(row=3, column=1)
        button = tk.Button(self, text="click", command=lambda: controller.getNumModules())
        button.grid(row=4, column=1)