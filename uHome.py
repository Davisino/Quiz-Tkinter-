import tkinter as tk

import sqlite3

# TO-DO List
# Retrieve Modules from DB and Render them into the screen
# Each Module should be clickable so that user can select which module to take the quiz on.
# Make design of how the quiz should look like

# When user clicks on a module to take the quiz
# DO: Generate 5 random questions from the DB and store those 5 questions on the quest_chosen
#      How: fetch all the questions of 'module selected' from DB of questions and select 5 of them randomly.
#           Add those 5 questions to the quest_chosen for later use

# DO: Create a submit/finish quiz button
#     i.This button should display the feedback from the DB and display the total score.
#     ii. At the same time the APP should store in results the test taken.
#     iii. Reset user score to 0 and take user to home user page

# IMPORTANT!
# Do: Keep track of the most 2 most questions repeated in the quiz.
#    How?: Additional table "quest_chosen" to store all questions selected
#          From each the questions DB.

class UserHomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # def score():
        #     return controller.getScore()
        #
        # def addScore():
        #     controller.currScore += 1
        # button = tk.Button(self, text="click", command=score)
        # button.grid(row=4, column=1)
        #
        # button = tk.Button(self, text="clickToAddScore", command=addScore)
        # button.grid(row=5, column=1)
        for i in range(3):
            self.columnconfigure(i, weight=1, minsize=75)
            self.rowconfigure(i, weight=1, minsize=50)

            for j in range(0, 3):
                frame = tk.Frame(
                    master=self,
                    relief=tk.RAISED,
                    borderwidth=1
                )
                frame.grid(row=i, column=j, padx=5, pady=5)

                label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
                label.pack(padx=5, pady=5)

