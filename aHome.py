import tkinter as tk
from Third import ThirdPage
import tkinter.font as tkFont
import sqlite3

# Today 13/12/2021
# Implemented fetch data from sqlite3 database and display modules into the app.
# Corrected minor errors, on some functions logic.
# add new update button to update the current list of modules every time a module is created

# What next?
#     every time add module should also add questions and feedback to quest table.
#


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

        def fetchModules():
            # This function will return all the modules from the Modules table in a list of tuples
            modules = ''
            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "SELECT mod_name from Modules"
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                modules = count.fetchall()
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to fetch data", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")
            return modules
        def deleteAndUpdate():
            if self.isActive:
                row = 2
                col = 0
                while row < 7 and col < 2:
                    a = head.grid_slaves(row, col)
                    if len(a) > 0:
                        a[0].destroy()
                        row += 1
                        if row == 7:
                            row = 2
                            col += 1

            row = 2
            col = 0
            # We get all the modules and store them in the getModules
            # Then we put them in columns of 5 rows while
            # popping modules names from it so that no modules are repeated
            getModules = fetchModules()
            # 20,178
            # 20, 178 + 122
            x,y = 20, 178

            while row < 7 and col < 3 and len(getModules) > 0:
                mod_txt = getModules[-1][0]
                mod_btn = tk.Button(head, text=mod_txt, font=fontFrame, width=15, height=1)
                mod_btn.grid(row=row, column=col, padx=20, pady=40)

                delete_mod = tk.Button(head, text="edit", width=15, height=1)
                delete_mod.place(x=x, y=y)

                edit_mod = tk.Button(head, text="delete module", width=13, height=1)
                edit_mod.place(x=x+104, y=y)
                y = y + 122

                row += 1
                if row == 7:
                    row = 2
                    col += 1
                    x += 245
                    y = 178
                getModules.pop()
            self.isActive = True
        deleteAndUpdate()
        # This button 'update' is necessary because if I try to run the
        # delete and update function to erase all widgets and put them again
        # tkinter app crashes. Therefore, the user needs to update it manually.

        update = tk.Button(head, text="update", command=deleteAndUpdate)
        update.grid(row=1, column=1)
        # Check If possible answers are in the correct formar
        def addNewModule():
            window = tk.Tk()
            #
            # window.grid_rowconfigure(0, minsize=600)
            # window.grid_columnconfigure(0, minsize=700)
            # make the window not resizable
            window.resizable(0, 0)
            window.geometry("320x350")

            window.title("New Module")
            l1 = tk.Label(window, text="Module Name: ")
            l1.place(x=10, y=10)

            e1 = tk.Entry(window, width=30)
            e1.place(x=110, y=10)

            l2 = tk.Label(window, text="Starting Question: ")
            l2.place(x=10, y=80)

            e2 = tk.Entry(window, width=30)
            e2.place(x=110, y=80)

            l3 = tk.Label(window, text="Possible Answers: ")
            l3.place(x=10, y=150)

            e3 = tk.Entry(window, width=30)
            e3.insert(0, "ans1,ans2,ans3...")
            e3.place(x=110, y=150)

            l4 = tk.Label(window, text="Feedback: ")
            l4.place(x=10, y=220)

            e4 = tk.Entry(window, width=30)
            e4.place(x=110, y=220)

            # Register Module
            def add_mod(mod_name):

                try:
                    sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                    cursor = sqliteConnection.cursor()
                    print("Succesfully connected to SQLite")

                    sqlite_insert_query = "INSERT INTO Modules (mod_name) Values " + "('" + mod_name + "')"
                    print(sqlite_insert_query)
                    count = cursor.execute(sqlite_insert_query)
                    sqliteConnection.commit()
                    print("record saved")
                    cursor.close()
                except sqlite3.Error as error:
                    print("Failed to insert data into sqlite table", error)
                finally:
                    if sqliteConnection:
                        sqliteConnection.close()
                        print("The SQLite connection is closed")

            # Register Questions from Module
            def add_quest(quest_name, quest_feed, quest_mod_id, possible_answers):
                try:
                    sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                    cursor = sqliteConnection.cursor()
                    print("Succesfully connected to SQLite")

                    sqlite_insert_query = "INSERT INTO Questions (quest_name, quest_feedback," \
                                          " mod_id, times, possible_answers)" \
                                          " Values " + "('" + quest_name + "')" + ",('" + quest_feed + "')" + ",('" + quest_mod_id +\
                                          "')" + ",('" + str(0) + "')" + ",('" + possible_answers + "');"
                    print(sqlite_insert_query)
                    count = cursor.execute(sqlite_insert_query)
                    sqliteConnection.commit()
                    print("record saved")
                    cursor.close()
                except sqlite3.Error as error:
                    print("Failed to insert data into sqlite ", error)
                finally:
                    if sqliteConnection:
                        sqliteConnection.close()
                        print("The SQLite connection is closed")


            def findModId(module_name):
                conn = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = conn.execute("SELECT mod_id FROM Modules where mod_name = '" + module_name + "'")
                row = cursor.fetchall()

                return str(row[0][0])

            def register_mod():

                # 1. We add the module to database so it has a Key
                add_mod(e1.get())
                # 2. We find that key
                e6 = findModId(e1.get())
                # 3. We can now add questions to its own table having access to the specific foreign key (mod_id)
                add_quest(e2.get(), e4.get(), e6, e3.get())

            submit_mod = tk.Button(window, text="add Module", command=register_mod)
            submit_mod.place(x=130, y=290)


        add_mod_btn = tk.Button(head, text="new module", font=fontFrame, command=addNewModule)
        add_mod_btn.grid(row=0, column=1, padx=(100, 0))










# ---------------------DELETE MODULE -------------------------
 #  step1. Delete All feedback from db
 #  step2. delete all questions from db
 #  step3. delete module

# ----------------------Add Module ----------------------------
#   step1. Add module and 1 questions and 1 feeback recommend user to add more questions
#   step2. add more questions through box kwowing this module is created already
#   step3. submit and add to the db.