import tkinter as tk


class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button = tk.Button(self, text="Home")
        button.grid(row=3, column=1)