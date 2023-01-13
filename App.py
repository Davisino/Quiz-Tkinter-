import tkinter as tk
from adminPageWidgetts.LogIn import LogInPage
from userPageWidgets.uHome import UserHomePage  
from adminPageWidgetts.aHome import AdminHomePage

class QuizzApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.currScore = 0
        # Create the window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=700)
        window.grid_columnconfigure(0, minsize=700)

        """
        This idea of maintaining the frames in a constant for loop came from this video.
        https://www.youtube.com/watch?v=tpGjHRDEjCE&t=1153s&ab_channel=IGTechTeam

        Basically, it cre∏ates a dictionary to store all the classes of the questionnaire.
        Then with the "change_frame" function it changes to which class you want to visit. 
        """
        self.containerOfFrames = {}
        for f in (LogInPage, UserHomePage, AdminHomePage):
            frame = f(window, self)
            self.containerOfFrames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.change_frame(LogInPage)
    def exitSystem(self):
        self.destroy()
        self.containerOfFrames[LogInPage].destroy()
        self.containerOfFrames[AdminHomePage].destroy()
        self.containerOfFrames[UserHomePage].destroy()
    def change_frame(self, page):
        frame = self.containerOfFrames[page]
        frame.tkraise()

    """
    This function can be used to get the score of the user at any point in time whenever a
    quiz has been initialized.
    There is gotta be another function to update the score to 0.

    """

    def getScore(self):
        print(self.currScore)


app = QuizzApp()
app.mainloop()
