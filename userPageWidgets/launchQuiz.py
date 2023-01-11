import tkinter as tk
from sql_commads import *
import tkinter.font as tkFont
import numpy as np

# TODO: Develop fetchPointsFromQuestion and fetchFeedbackFromQuestion


def launchQuiz(quizName):
    # window = tk.Tk()
    # window.resizable(0, 0)
    # window.geometry("700x600")
    #
    # fontFrame = tkFont.Font(
    #     family="Arial",
    #     size=26,
    #     weight='bold')
    # m_quest_features = tk.LabelFrame(window, text=f"{quizName} questionnaire", bg='#FBFDF4', font=fontFrame,
    #                                  bd=1)
    # m_quest_features.pack(fill='both', expand='yes', padx=20, pady=10)

    # Put all the questions with the possible answers

    questions = fetch_all_quest(quizName)
    questions = [x[0] for x in questions]

    answers_from_user = []

    for question in questions:
        a = fetchAnswer(question)
        b = fetchPossibleAnswers(question)
        answers = a + b
        newQuestionFrame(question, answers, answers_from_user, questions)




def newQuestionFrame(question_name, answers, storage_answers, questions):
    window = tk.Tk()
    window.resizable(0, 0)
    window.geometry("700x600")

    fontFrame = tkFont.Font(
        family="Arial",
        size=40,
        weight='bold')
    m_quest_features = tk.LabelFrame(window, text=f"questionnaire", bg='#FBFDF4', font=fontFrame,
                                     bd=1)
    m_quest_features.pack(fill='both', expand='yes', padx=20, pady=10)

    title = tk.Label(m_quest_features, text=question_name, font=fontFrame)
    title.pack()

    variable = tk.StringVar(m_quest_features)

    variable.set(answers[0])  # default value
    print(answers)
    w = tk.OptionMenu(m_quest_features, variable, *answers)
    w.pack()

    submit = tk.Button(m_quest_features, text="Submit", command=lambda: submitQuestion(window,variable.get(), storage_answers, questions))
    submit.pack()

def submitQuestion(currentWindow,value, storage, questions):
    storage.append(value)
    if len(storage) == len(questions):
        displayResults(questions, storage)
    currentWindow.destroy()

def displayResults(questions, answers):
    window = tk.Tk()
    window.resizable(0, 0)
    window.geometry("700x600")

    correctAnswered = 0
    totalPoints = 0
    for i in range(len(questions)):
        question = questions[i]
        user_answer = answers[i]
        correct_answer = fetchAnswer(question)
        if user_answer == correct_answer:
            correctAnswered +=1
            totalPoints = int(fetchPointsFromQuestion(question))

            lquestion = tk.Label(window, text=question)
            lquestion.pack()
            feeb = fetchFeedbackFromQuestion(question, user_answer)
            lfeedback = tk.Label(window, text=feeb)
            lfeedback.pack()

    message = "WELL DONE! You have answered" + str(correct_answer) + " questions correctly" if \
        correctAnswered >= 3 else "You have answered " + correctAnswered + " questions correctly, Keep working on it"
    title = tk.Label(window, text=message)
    title.pack()

