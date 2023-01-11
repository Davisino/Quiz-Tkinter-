import tkinter as tk
from sql_commads import *
import tkinter.font as tkFont
from userPageWidgets.launchQuiz import *
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
        fontFrame = tkFont.Font(
            family="Arial",
            size=26,
            weight='bold')
        lable_title = tk.Label(self, text="Select a module you would like to take the test on", font=fontFrame)
        lable_title.pack()

        current_modules = fetchModules()
        array_modules = [x[0] for x in current_modules]


        variable = tk.StringVar(self)

        variable.set(array_modules[0])  # default value

        w = tk.OptionMenu(self, variable, *array_modules)
        w.pack()

        launch_module = tk.Button(self, text="Take Assesment", command=lambda: launchQuiz(variable.get()))
        launch_module.pack()








