import tkinter as tk
from LogIn import LogInPage
from uHome import UserHomePage
from aHome import AdminHomePage
from Third import ThirdPage
import sys
import os

# HOW TO HANDLE THE ADMIN UI VS NORMAL USER UI?
# Idea 1: create a database to store all
# the modules with their respective questions
# Then by default there will be 5 modules and 5 questions for each module.
# Admin user have the power to MODIFY the database.
# Example:
    # Admin user can delete/add questions
        # i. Delete:
            # admin will just need to click on a little button to the right of each question which will delete the question SOMEHOW
        # ii. ADD:
            # admin will click on the + sign and immediately a new window will pop up for the user to add the new question

    # admin user can delete/add modules
        # i. Delete:
            # admin will just click on the little button to the right of each module on the -Modules Frame- which will delete the module and its questions SOMEHOW.
        # ii. ADD:
            # admin will click on the + sign button and immediately a new window will pop up for the user to add the new module and 5 default questions.

    # Normal user select module


# *args store all arguments in tuple
# **kwargs store key value pairs.
class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.currScore = 0
        #Create the window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=600)
        window.grid_columnconfigure(0, minsize=700)

        self.frames = {}
        for f in (LogInPage, UserHomePage, AdminHomePage, ThirdPage):
            frame = f(window, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.change_frame(LogInPage)

    def change_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
    def getScore(self):
        print(self.currScore)
    def restart_program(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

app = App()
app.mainloop()