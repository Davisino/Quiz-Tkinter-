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
        fontBtn = tkFont.Font(
            family="Arial",
            size=14,
            )
        fontTitle = tkFont.Font(
            family="Arial",
            size=22,
        )
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

        titleLabel = tk.Label(head, text="Current Modules", font=fontTitle)
        titleLabel.grid(row=0, column=0, pady=20)



        # ----------- USEFEUL FUNCTIONS ---------
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
        def onlyDeleteBtnModules():
            row = 2
            col = 0
            count = len(fetchModules())
            print(count,'sss')
            while row < 7 and col < 2 and count > 0:
                a = head.grid_slaves(row, col)
                if len(a) > 0:
                    a[0].destroy()
                    count -= 1
                    row += 1
                    if row == 7:
                        row = 2
                        col += 1
            self.isActive = False
            return
        def delBtnModsAndUpdate():
            if self.isActive is True:
                row = 2
                col = 0
                count = len(fetchModules())
                print(count, 'sss')
                while row < 7 and col < 2 and count > 0:
                    a = head.grid_slaves(row, col)

                    if len(a) > 0:
                        a[0].destroy()
                        count -= 1
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

            while row < 7 and col < 3 and len(getModules) > 0:
                mod_txt = getModules[-1][0]
                mod_btn = tk.Button(head, text=mod_txt, font=fontBtn, width=15, height=1)
                mod_btn.grid(row=row, column=col, padx=15, pady=20)
                # delete_mod = tk.Button(head, text="edit", width=15, height=1)
                # delete_mod.place(x=x, y=y)
                #
                # edit_mod = tk.Button(head, text="delete module", width=13, height=1)
                # edit_mod.place(x=x+104, y=y)
                row += 1
                if row == 7:
                    row = 2
                    col += 1
                getModules.pop()

            self.isActive = True
        delBtnModsAndUpdate()

        def findModId(module_name):

            conn = sqlite3.connect('./Databases/quiz_storage.db')
            cursor = conn.execute("SELECT mod_id FROM Modules where mod_name = '" + module_name + "';")
            row = cursor.fetchall()
            print(str(row[0][0]))
            return str(row[0][0])
        # ---------------END OF USEFUL FUNCTIONS ---------------
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
                                          " Values " + "('" + quest_name + "'" + ",'" + quest_feed + "'" + ", '" + quest_mod_id +\
                                          "'" + ",'" + str(0) + "'" + ",'" + possible_answers + "');"
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


            def register_mod_DB():
                #
                # 1. We add the module to database so it has a Key
                # 2. We find that key
                # 3. We can now add questions to its own table having access to the specific foreign key (mod_id)
                #
                onlyDeleteBtnModules()
                add_mod(e1.get())
                e6 = findModId(e1.get())
                add_quest(e2.get(), e4.get(), e6, e3.get())
                delBtnModsAndUpdate()


            submit_mod = tk.Button(window, text="add Module", command=register_mod_DB)
            submit_mod.place(x=130, y=290)


        add_mod_btn = tk.Button(head, text="New Module", font=fontBtn, command=addNewModule)
        add_mod_btn.grid(row=0, column=1, padx=(100, 0))

        def delModuleFrame():
            window = tk.Tk()

            # window.grid_rowconfigure(0, minsize=600)
            # window.grid_columnconfigure(0, minsize=700)
            # make the window not resizable
            window.resizable(0, 0)
            window.geometry("320x200")
            window.title("Delete Module")
            currModule = tk.StringVar(window)
            currModule.set("--Select Module--")  # default value



            chooseTest = tk.OptionMenu(window, currModule, *fetchModules())
            chooseTest.config(font=('Arial', 15, 'bold'))
            menu = window.nametowidget(chooseTest.menuname)
            menu.config(font=('Arial', 10, 'bold'))
            chooseTest.place(x=20, y=20)


            # ORDER TO DELETE A MODULE
            #     1. Delete All questions from Databases
            #     2. Delete Module From database
            #     3. Close window frame and DeleteAndUpdate
            #

            # DEL QUESTIONS
            def toText(module):
                i = 0
                z = len(module)-1
                az = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                while module[i] not in az:
                    i+=1
                while module[z] not in az:
                    z -=1

                return module[i:z+1]


            def delAllQuestionsFromDB(moduleId):
                try:
                    sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                    cursor = sqliteConnection.cursor()
                    print("Succesfully connected to SQLite")

                    sqlite_insert_query = "DELETE FROM Questions WHERE mod_id = " + moduleId + ";"
                    print(sqlite_insert_query)
                    count = cursor.execute(sqlite_insert_query)
                    sqliteConnection.commit()
                    print("Questions Deleted")
                    cursor.close()
                except sqlite3.Error as error:
                    print("Failed to Delete questions into Sqlite ", error)
                finally:
                    if sqliteConnection:
                        sqliteConnection.close()
                        print("The SQLite connection is closed")
            def delModFromDB(moduleName):
                try:
                    sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                    cursor = sqliteConnection.cursor()
                    print("Succesfully connected to SQLite")

                    sqlite_insert_query = "DELETE FROM Modules WHERE mod_name = '" + moduleName + "';"
                    print(sqlite_insert_query)
                    count = cursor.execute(sqlite_insert_query)
                    sqliteConnection.commit()
                    print("Module Deleted")
                    cursor.close()
                except sqlite3.Error as error:
                    print("Failed to Delete questions into Sqlite ", error)
                finally:
                    if sqliteConnection:
                        sqliteConnection.close()
                        print("The SQLite connection is closed")

            def deleteModule():
                # 1. Delete all buttons first
                # 2. delete module from DB
                # 3. Display buttons again
                onlyDeleteBtnModules()
                modToDelete = toText(currModule.get())
                getModId = findModId(modToDelete)
                delAllQuestionsFromDB(getModId)
                delModFromDB(modToDelete)
                delBtnModsAndUpdate()
                window.destroy()


            sub_del = tk.Button(window, text="erase", font= ('Arial', 14, 'bold'), command=deleteModule)
            sub_del.place(x=230, y=20)

            alert_txt = tk.Label(window, text="Careful! All questions will also be erased", font=('Arial', 8, 'bold'))
            alert_txt.place(x=20, y=120)

        del_mod_btn = tk.Button(head, text="Del Module", font=fontBtn, command=delModuleFrame)
        del_mod_btn.grid(row=0, column=2, padx=(10, 0))










# ---------------------DELETE MODULE -------------------------
 #  step1. Delete All feedback from db
 #  step2. delete all questions from db
 #  step3. delete module

# ----------------------Add Module ----------------------------
#   step1. Add module and 1 questions and 1 feeback recommend user to add more questions
#   step2. add more questions through box kwowing this module is created already
#   step3. submit and add to the db.