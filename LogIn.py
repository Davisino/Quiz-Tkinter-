import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import messagebox
from uHome import UserHomePage
from aHome import AdminHomePage


class LogInPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # --------------------------LOGIN---------------------------------
        fontBG = tkFont.Font(
                                family="Arial",
                                size=16,
                                weight='bold',
        )


        border = tk.LabelFrame(self, text="Log In",bg='#02203c',fg="white", bd=1, font=fontBG)
        border.pack(fill='both', expand='yes', padx=20, pady=150)

        username = tk.Label(border, text="username", font=fontBG,fg="white",bg='#02203c')
        username.place(x=50, y=20)

        userInput = tk.Entry(border, width=30, bd=5)
        userInput.place(x=180, y=20)

        password = tk.Label(border, text="password", font=fontBG,fg="white",bg='#02203c')
        password.place(x=50, y=80)

        passInput = tk.Entry(border,show="*", width=30, bd=5)
        passInput.place(x=180, y=80)
        # -------------------------------SUBMIT LOGIN--------------------------
        def verify():
            # OPTION 1 ->
            # username and password match
            # in the database File for normal users
            # Should take them to the UI of normal users
            with open("credential.txt", "r") as f:
                # ["username, password", "username,password"]
                info = f.readlines()
                for user in info:

                    # u -> username, p -> password
                    # split them such that u -> "username" and p -> "password"
                    u, p = user.split(",")
                    # strip -> removes spaces at the end and begining
                    # if u match our username input and p match our password input take user to next page
                    if u.strip() == userInput.get() and p.strip() == passInput.get():
                        controller.change_frame(UserHomePage)
                        return
            # OPTION 2 ->
            # username and password match
            # in the database file for ADMINS users
            # Should take them to the UI for Admin Users
            with open("AdminCredential.txt", "r") as f:
                # ["username, password", "username,password"]
                info = f.readlines()
                for user in info:
                    # u -> username, p -> password
                    # split them such that u -> "username" and p -> "password"
                    u, p = user.split(",")
                    # strip -> removes spaces at the end and begining
                    # if u match our username input and p match our password input take user to next page
                    if u.strip() == userInput.get() and p.strip() == passInput.get():

                        controller.change_frame(AdminHomePage)
                        return
            messagebox.showinfo("Error", "Please provide a correct username and password")



        # ---------------------REGISTRATION-----------------------------
        submitBtn = tk.Button(border, text="Submit", command=verify, font=fontBG)
        submitBtn.place(x=275, y=120)
        def registerUser():
            window = tk.Tk()

            # make the window not resizable
            window.resizable(0,0)

            window.title("Register")
            l1 = tk.Label(window, text="Username: ", font=fontBG)
            l1.place(x=10, y=10)

            e1 = tk.Entry(window,width=30, bd=5)
            e1.insert(tk.END, "username")
            e1.place(x=200, y=10)

            l2 = tk.Label(window, text="Password: ", font=fontBG)
            l2.place(x=10, y=80)

            e2 = tk.Entry(window, show="*", width=30, bd=5)
            e2.insert(tk.END, "password")
            e2.place(x=200, y=80)

            l3 = tk.Label(window, text="Confirm Password: ", font=fontBG)
            l3.place(x=10, y=150)
            e3 = tk.Entry(window, show="*", width=30, bd=5)
            e3.place(x=200, y=150)

            # This function open the database and
            # check whether the username of the user
            # is already in use returns True if it is,
            # otherwise False
            def isNameUsed(name):
                with open("credential.txt", 'r') as f:
                    info = f.readlines()
                    for user in info:
                        # u -> username, p -> password
                        # split them such that u -> "username" and p -> "password"
                        u, p = user.split(",")
                        # strip -> removes spaces at the end and beginning
                        # if u match our username input
                        # and p match our password input take user to next page
                        if u.strip() == name:
                            return True
                return False

            # ----------------------------submit registration --------------------------
            def check():
                isUsed = isNameUsed(e1.get())
                if e1.get() != 'username' and e2.get() != "password" and isUsed is False:
                    if e2.get() == e3.get():
                        with open("credential.txt", "a") as f:
                            f.write(e1.get() + ',' + e2.get() + "\n")

                            messagebox.showinfo("Welcome", "You are now a fully registered")
                    else:
                        messagebox.showinfo("Error", "Your password didn't get match!")
                else:
                    if isUsed:
                        messagebox.showinfo("Error", "This username is already in use")
                        return
                    messagebox.showinfo("Error", "Some field is missing, Please fill of all of them")


            e4 = tk.Button(window, text="Sign In", command=check, font=fontBG)
            e4.place(x=330, y=180)
            window.geometry("480x250")

        registerBtn = tk.Button(self, text="Register", bg='#02203c', font=fontBG,fg="white",
                                command=registerUser)
        registerBtn.place(x=550, y=170)
