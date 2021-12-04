import tkinter as tk
from Third import ThirdPage
import tkinter.font as tkFont
import sqlite3
# TO-DO LIST:
# Create FEEDBACK TABLE AND try to add modules to database and delete them.

# MODULE
# c.execute("""CREATE TABLE Modules (
#                         mod_id INTEGER PRIMARY KEY,
#                         mod_name TEXT NOT NULL
#             )""")

# QUESTIONS
# c.execute("""CREATE TABLE Feedback (
#                                  fee_id INTEGER PRIMARY KEY,
#                                  fee_name TEXT NOT NULL,
#                                  _id INTEGER NOT NULL,
#                                  FOREIGN KEY (mod_id)
#                                      REFERENCES Modules (mod_id)
#                      )""")

# FEEDBACK

class AdminHomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # $ add fontsize
        fontFrame = tkFont.Font(
            family="Arial",
            size=16,
            weight='bold')
        head = tk.LabelFrame(self, text="Log In", bg='#FBFDF4', font=fontFrame, bd=1)
        head.pack(fill='both', expand='yes', padx=20, pady=10)

        # def createDB():
        #     mod_storage = sqlite3.connect('./Databases/quiz_storage.db')
        #     c = mod_storage.cursor()
        #     c.execute("""CREATE TABLE Feedback (
        #                             fee_id INTEGER PRIMARY KEY,
        #                             fee_text TEXT NOT NULL,
        #
        #                 )""")
        #     print('create question db and linking foreign key ')
        # btn = tk.Button(self, text="ClickToCreateDatabase", font=fontFrame, command=createDB)
        # btn.pack()





 # ---------------------DELETE MODULE -------------------------
 #  step1. Delete All feedback from db
 #  step2. delete all questions from db
 #  step3. delete module

# ----------------------Add Module ----------------------------
#   step1. Add module and 1 questions and 1 feeback recommend user to add more questions
#   step2. add more questions through box kwowing this module is created already
#   step3. submit and add to the db.