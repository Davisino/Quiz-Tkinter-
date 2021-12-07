import tkinter as tk
from Third import ThirdPage
import tkinter.font as tkFont
import sqlite3


# MODULE
# c.execute("""CREATE TABLE Modules (
#                         mod_id INTEGER PRIMARY KEY,
#                         mod_name TEXT NOT NULL
#             )""")
#
# c.execute("""CREATE TABLE Questions (
#                                              quest_id INTEGER PRIMARY KEY,
#                                              quest_name TEXT NOT NULL,
#                                              quest_feedback TEXT NOT NULL,
#                                              mod_id INTEGER NOT NULL,
#                                              FOREIGN KEY (mod_id)
#                                                  REFERENCES Modules (mod_id)
#                                  )""")


class AdminHomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.isActive = False

        fontFrame = tkFont.Font(
            family="Arial",
            size=16,
            weight='bold')
        head = tk.LabelFrame(self, text="Admin Page", bg='#FBFDF4', font=fontFrame, bd=1)
        head.pack(fill='both', expand='yes', padx=20, pady=10)

        # def createDB():
        #     mod_storage = sqlite3.connect('./Databases/quiz_storage.db')
        #     c = mod_storage.cursor()
        #
        #     c.execute("""CREATE TABLE Questions (
        #                                      quest_id INTEGER PRIMARY KEY,
        #                                      quest_name TEXT NOT NULL,
        #                                      quest_feedback TEXT NOT NULL,
        #                                      mod_id INTEGER NOT NULL,
        #                                      FOREIGN KEY (mod_id)
        #                                          REFERENCES Modules (mod_id)
        #                          )""")
        #     print('Questions table created and connected to modules table')
        # btn = tk.Button(self, text="ClickToCreateDatabase", font=fontFrame, command=createDB)
        # btn.pack()

        titleLabel = tk.Label(head, text="Current Modules", font=fontFrame)
        titleLabel.grid(row=0, column=0, pady=20)


        def deleteAndUpdate():
            if self.isActive:
                row = 2
                col = 0
                while row < 7 and col < 2:
                    a = head.grid_slaves(row, col)
                    a[0].destroy()
                    row += 1
                    if row == 7:
                        row = 2
                        col += 1
            row = 2
            col = 0
            while row < 7 and col < 2:
                mod_btn = tk.Button(head, text="Science", font=fontFrame)
                mod_btn.grid(row=row, column=col, padx=20, pady=20)
                row += 1
                if row == 7:
                    row = 2
                    col += 1
            self.isActive = True

        def addNewModule():
            window = tk.Tk()

            # make the window not resizable
            window.resizable(0, 0)

            window.title("New Module")
            l1 = tk.Label(window, text="Module Name: ")
            l2 = tk.Label(window, text="Question: ")


        add_mod_btn = tk.Button(head, text="new module", font=fontFrame, command=addNewModule)
        add_mod_btn.grid(row=0, column=1, padx=(100, 0))

        deleteAndUpdate()








# ---------------------DELETE MODULE -------------------------
 #  step1. Delete All feedback from db
 #  step2. delete all questions from db
 #  step3. delete module

# ----------------------Add Module ----------------------------
#   step1. Add module and 1 questions and 1 feeback recommend user to add more questions
#   step2. add more questions through box kwowing this module is created already
#   step3. submit and add to the db.