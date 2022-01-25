import tkinter as tk
import tkinter.font as tkFont
import sqlite3


class AdminHomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.isActive = False
        fontFrame = tkFont.Font(
            family="Arial",
            size=26,
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

        titleLabel = tk.Label(head, text="Current Modules", font=fontTitle)
        titleLabel.grid(row=0, column=0, pady=20)

        # ----------- USEFEUL FUNCTIONS ---------
        # From here, you will see some functions
        # that I consider very useful to do the job on the quiz app.
        # It saved me a lot of time, because I had not to code manually sqlite commands anymore.
        # I would just call the function and pass the desired arguments/parameters.
        def findModId(module_name):
            conn = sqlite3.connect('./Databases/quiz_storage.db')
            cursor = conn.execute("SELECT mod_id FROM Modules where mod_name = '" + module_name + "';")
            row = cursor.fetchall()
            print(str(row[0][0]))
            return str(row[0][0])

        def fetchModules():
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

        def fetch_all_quest(curr_mod_name):
            m_id = findModId(curr_mod_name)
            print(m_id, 'module id')
            questions = []
            modules = ''
            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "SELECT quest_name from Questions " \
                                      "where mod_id = " + m_id
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                modules = count.fetchall()

                cursor.close()
            except sqlite3.Error as error:
                print("Failed to fetch questions", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

            for i in range(len(modules)):
                questions.append(modules[i][0])
            return questions

        def get_fathers_from_children(answers):
            fathers = []

            for i in range(len(answers)):
                try:
                    sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                    cursor = sqliteConnection.cursor()
                    print("Succesfully connected to SQLite")

                    sqlite_insert_query = "SELECT bma_father from BestMatchAns " \
                                          "where bma_child = " + "'" + answers[i] + "'"
                    count = cursor.execute(sqlite_insert_query)
                    sqliteConnection.commit()
                    result = count.fetchone()[0]
                    fathers.append(result)
                    cursor.close()
                except sqlite3.Error as error:
                    print("Failed to select father from child ", error)
                finally:
                    if sqliteConnection:
                        sqliteConnection.close()
                        print("The SQLite connection is closed")

            return fathers

        def find_mod_quest_id(quest_name):
            result = []
            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "SELECT quest_id, mod_id from Questions " \
                                      "where quest_name = " + "'" + quest_name + "'"
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                result = count.fetchall()
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to select quest and mod id ", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

            return [int(result[0][0]), int(result[0][1])]

        def find_quest_id(quest_name):

            result = ''
            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "SELECT quest_id from Questions " \
                                      "where quest_name = " + "'" + quest_name + "'"
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                result = count.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to select quest id ", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

            return result[0]

        def find_inc_ans_from_quest(quest_id):
            result = ''
            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "Select possible_answers from Questions " \
                                      "where quest_id = '" + str(quest_id) + "'"
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                result = count.fetchall()
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to fetch all answers from question ", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")
            ans = result[0][0]
            return ans.split(',')

        def find_quest_mark(quest_id):
            result = ''
            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "SELECT quest_mark from Questions " \
                                      "where quest_id = " + "'" + str(quest_id) + "'"
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                result = count.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to select quest id ", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

            return result[0]

        def find_ans_from_quest(quest_id):
            result = ''
            ans = []
            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "Select answer from Questions " \
                                      "where quest_id = '" + str(quest_id) + "'"
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                result = count.fetchall()
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to fetch all answers from question ", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")
            for x in result:
                ans.append(x[0])
            return ans

        def update_quest(quest_id, column, new_answer):
            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "Update Questions " \
                                      "Set " + column + " = '" + new_answer + "' " \
                                                                              "Where quest_id = '" + str(quest_id) + "'"
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to fetch all answers from question ", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

        def del_feed_quest_from_db(q_id):

            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "Delete from Feedback " \
                                      "Where quest_id = " + str(q_id)
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                result = count.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to delete feedback from db", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

        def del_bma_quest_from_db(q_id):

            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "Delete from BestMatchAns " \
                                      "Where quest_id = " + str(q_id)
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                result = count.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to delete bms answers from db ", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

        def del_quest_execute(q_id):

            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "Delete from Questions " \
                                      "where quest_id = " + str(q_id)
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                result = count.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to delete question from db ", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

        def update_option_menu(m_quest_to_del, curr_mod_name, quest_to_del):
            m = m_quest_to_del['menu']
            m.delete(0, 'end')
            list_of_quest = fetch_all_quest(curr_mod_name)
            for string in list_of_quest:
                m.add_command(label=string, command=lambda value=string: quest_to_del.set(value))

        def find_quest_type(quest_name):
            result = ''
            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "Select quest_type from Questions " \
                                      "where quest_name = '" + quest_name + "'"
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                result = count.fetchone()
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to fetch type of quest ", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")
            return result[0]

        def onlyDeleteBtnModules():
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
            self.isActive = False
            return

        # EDIT QUESTIONS MODE NAME
        def edit_quest_frame(mod_name, quest_name):

            window = tk.Tk()
            window.resizable(0, 0)
            window.geometry("700x600")
            m_quest_features = tk.LabelFrame(window, text="Admin Page - Edit Question", bg='#FBFDF4', font=fontFrame,
                                             bd=1)
            m_quest_features.pack(fill='both', expand='yes', padx=20, pady=10)

            # Find type of quest and id:
            type_of_q = find_quest_type(quest_name)
            quest_id = find_quest_id(quest_name)

            quest_module = tk.Label(m_quest_features, text="Module: ", font=fontTitle)
            quest_module.place(x=10, y=10)

            quest_module_title = tk.Label(m_quest_features, text=mod_name, font=fontTitle)
            quest_module_title.place(x=180, y=10)

            quest_title = tk.Label(m_quest_features, text="Question Name: ", font=fontTitle)
            quest_title.place(x=10, y=60)

            e_quest_title = tk.Entry(m_quest_features, width=30)
            e_quest_title.place(x=180, y=60)
            e_quest_title.insert(tk.END, quest_name)

            if type_of_q == 'tf':
                l_ans = tk.Label(m_quest_features, text="Answer: ", font=fontTitle)
                l_ans.place(x=10, y=100)
                get_ans_tf = find_ans_from_quest(quest_id)
                e_ans_tf = tk.Entry(m_quest_features, width=20)
                e_ans_tf.place(x=10, y=130)
                e_ans_tf.insert(tk.END, get_ans_tf)
                # Update answer column
                ans_tf_btn = tk.Button(m_quest_features, text="Apply", width=10,
                                       command=lambda: update_quest(quest_id, 'answer', e_ans_tf.get()))
                ans_tf_btn.place(x=10, y=160)

                get_inc_ans_tf = find_inc_ans_from_quest(quest_id)
                l_inc_ans = tk.Label(m_quest_features, text="Incorrect Answer: ", font=fontTitle)
                l_inc_ans.place(x=10, y=200)

                e_inc_ans = tk.Entry(m_quest_features, width=20)
                e_inc_ans.place(x=10, y=230)
                e_inc_ans.insert(tk.END, get_inc_ans_tf)
                # Update possible answer column

                ans_tf_btn = tk.Button(m_quest_features, text="Apply", width=10,
                                       command=lambda: update_quest(quest_id, 'possible_answer', e_inc_ans.get()))
                ans_tf_btn.place(x=10, y=260)

                # Update question Mark
                get_quest_mark = find_quest_mark(quest_id)
                l_quest_mark = tk.Label(m_quest_features, text="Question Mark: ", font=fontTitle)
                l_quest_mark.place(x=10, y=290)
                e_quest_mark = tk.Entry(m_quest_features, width=8)
                e_quest_mark.place(x=10, y=320)
                e_quest_mark.insert(tk.END, get_quest_mark)

                q_m_btn = tk.Button(m_quest_features, text="Apply", width=10,
                                    command=lambda: update_quest(quest_id, 'quest_mark', e_quest_mark.get()))
                q_m_btn.place(x=10, y=350)
            if type_of_q == 'mcq':
                l_ans = tk.Label(m_quest_features, text="Answer: ", font=fontTitle)
                l_ans.place(x=10, y=100)
                get_ans = find_ans_from_quest(quest_id)
                len_of_ans = len(get_ans)
                if len_of_ans == 1:
                    e_ans_1 = tk.Entry(m_quest_features, width=20)
                    e_ans_1.place(x=10, y=130)
                    e_ans_1.insert(tk.END, get_ans[0])
                elif len_of_ans == 2:
                    e_ans_1 = tk.Entry(m_quest_features, width=20)
                    e_ans_1.place(x=10, y=130)
                    e_ans_1.insert(tk.END, get_ans[0])

                    e_ans_2 = tk.Entry(m_quest_features, width=20)
                    e_ans_2.place(x=10, y=160)
                    e_ans_2.insert(tk.END, get_ans[1])
                elif len_of_ans == 3:
                    e_ans_1 = tk.Entry(m_quest_features, width=20)
                    e_ans_1.place(x=10, y=130)
                    e_ans_1.insert(tk.END, get_ans[0])

                    e_ans_2 = tk.Entry(m_quest_features, width=20)
                    e_ans_2.place(x=10, y=160)
                    e_ans_2.insert(tk.END, get_ans[1])

                    e_ans_3 = tk.Entry(m_quest_features, width=20)
                    e_ans_3.place(x=10, y=190)
                    e_ans_3.insert(tk.END, get_ans[2])

                get_inc_ans = find_inc_ans_from_quest(quest_id)
                l_inc_ans = tk.Label(m_quest_features, text="Incorrect Answers: ", font=fontTitle)
                l_inc_ans.place(x=10, y=250)
                len_of_inc_ans = len(get_inc_ans)

                if len_of_inc_ans == 1:
                    e_inc_ans_1 = tk.Entry(m_quest_features, width=20)
                    e_inc_ans_1.place(x=10, y=280)
                    e_inc_ans_1.insert(tk.END, get_inc_ans[0])
                if len_of_inc_ans == 2:
                    e_inc_ans_1 = tk.Entry(m_quest_features, width=20)
                    e_inc_ans_1.place(x=10, y=280)
                    e_inc_ans_1.insert(tk.END, get_inc_ans[0])

                    e_inc_ans_2 = tk.Entry(m_quest_features, width=20)
                    e_inc_ans_2.place(x=10, y=310)
                    e_inc_ans_2.insert(tk.END, get_inc_ans[1])

                if len_of_inc_ans == 3:
                    e_inc_ans_1 = tk.Entry(m_quest_features, width=20)
                    e_inc_ans_1.place(x=10, y=280)
                    e_inc_ans_1.insert(tk.END, get_inc_ans_tf[0])

                    e_inc_ans_2 = tk.Entry(m_quest_features, width=20)
                    e_inc_ans_2.place(x=10, y=310)
                    e_inc_ans_2.insert(tk.END, get_inc_ans_tf[1])

                    e_inc_ans_3 = tk.Entry(m_quest_features, width=20)
                    e_inc_ans_3.place(x=10, y=340)
                    e_inc_ans_3.insert(tk.END, get_inc_ans_tf[2])
                def gather_inc_ans():
                    if len_of_inc_ans == 1:
                        return ",".join([e_inc_ans_1.get()])
                    if len_of_inc_ans == 2:
                        print('ss')
                        return ",".join([e_inc_ans_1.get(), e_inc_ans_2.get()])
                    if len_of_inc_ans == 3:
                        return ",".join([e_inc_ans_1.get(), e_inc_ans_2.get(), e_inc_ans_3.get()])

                def gather_ans():
                    if len_of_ans == 1:
                        return ",".join([e_ans_1.get()])
                    if len_of_ans == 2:
                        return ",".join([e_ans_1.get(), e_ans_2.get()])
                    if len_of_ans == 3:
                        return ",".join([e_ans_1.get(), e_ans_2.get(), e_ans_3.get()])

                ans_btn = tk.Button(m_quest_features, text="Apply", width=10,
                                    command=lambda: update_quest(quest_id, 'answer', gather_ans()))
                ans_btn.place(x=10, y=220)

                inc_ans_btn = tk.Button(m_quest_features, text="Apply", width=10,
                                        command=lambda: update_quest(
                                            quest_id,
                                            'possible_answers',
                                            gather_inc_ans()))
                inc_ans_btn.place(x=10, y=370)

                get_quest_mark = find_quest_mark(quest_id)
                l_quest_mark = tk.Label(m_quest_features, text="Question Mark: ", font=fontTitle)
                l_quest_mark.place(x=10, y=410)
                e_quest_mark = tk.Entry(m_quest_features, width=8)
                e_quest_mark.place(x=150, y=410)
                e_quest_mark.insert(tk.END, get_quest_mark)

                q_m_btn = tk.Button(m_quest_features, text="Apply", width=10,
                                    command=lambda: update_quest(quest_id, 'quest_mark', e_quest_mark.get()))
                q_m_btn.place(x=220, y=410)

        # Change mod name frame
        def change_mod_name(curr_mod_name):
            window = tk.Tk()
            window.resizable(0, 0)
            window.geometry("700x600")
            mod_features = tk.LabelFrame(window, text="Admin Page - Edit Module", bg='#FBFDF4', font=fontFrame, bd=1)
            mod_features.pack(fill='both', expand='yes', padx=20, pady=10)

            t_new_name = tk.Label(mod_features, text="New Module Name: ", font=fontTitle)
            t_new_name.place(x=10, y=10)
            new_name_entry = tk.Entry(mod_features, font=fontBtn, borderwidth=5, width=22)
            new_name_entry.place(x=10, y=50)
            refresh_btn = tk.Button(mod_features, text="Refresh", width=10,
                                    command=lambda:
                                    update_option_menu(curr_quest_to_del_m,
                                                       curr_mod_name,
                                                       curr_quest_to_del))
            refresh_btn.place(x=580, y=10)

            def update_mod_name_in_db(curr_name, desired_name):
                try:
                    sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                    cursor = sqliteConnection.cursor()
                    print("Succesfully connected to SQLite")

                    sqlite_insert_query = "Update Modules set mod_name = " + \
                                          "'" + desired_name + "'" + \
                                          " where mod_name = " + "'" + \
                                          curr_name + "';"
                    print(sqlite_insert_query)
                    count = cursor.execute(sqlite_insert_query)
                    sqliteConnection.commit()
                    print("record Updated")
                    cursor.close()
                except sqlite3.Error as error:
                    print("Failed to Update Data Into Sqlite3", error)
                finally:
                    if sqliteConnection:
                        sqliteConnection.close()
                        print("The SQLite connection is closed")

            def execute_mod_change(curr_name, desired_name):

                update_mod_name_in_db(curr_name, desired_name)
                delBtnModsAndUpdate()
                window.destroy()

            new_name_sub = tk.Button(mod_features, text="submit", font=fontBtn, width=7,
                                     command=lambda: execute_mod_change(curr_mod_name, new_name_entry.get()))
            new_name_sub.place(x=240, y=50)

            # Add Question:

            mod_add_quest_l = tk.Label(mod_features, text="Add new question to this module: ", font=fontTitle)
            mod_add_quest_l.place(x=10, y=125)

            add_quest_e = tk.Button(mod_features, text="Add", font=fontBtn,
                                    command=lambda: chooseTypeOfQuestion(curr_mod_name))

            add_quest_e.place(x=270, y=120)

            mod_del_quest_l = tk.Label(mod_features, text="Delete / Edit a question from the list below: ",
                                       font=fontTitle)
            mod_del_quest_l.place(x=10, y=195)

            curr_quest_to_del = tk.StringVar(mod_features)
            curr_quest_to_del.set("Choose a Question")  # default value

            def del_quest_from_db(quest_name):
                # Delete Feedback and BMA answers from db
                q_id = find_quest_id(quest_name)
                del_feed_quest_from_db(q_id)
                del_bma_quest_from_db(q_id)
                del_quest_execute(q_id)
                # Reset the List of Questions.
                update_option_menu(curr_quest_to_del_m, curr_mod_name, curr_quest_to_del)

            curr_quest_to_del_m = tk.OptionMenu(mod_features, curr_quest_to_del, *fetch_all_quest(curr_mod_name))
            curr_quest_to_del_m.config(font=fontBtn)
            m_q_c = mod_features.nametowidget(curr_quest_to_del_m.menuname)
            m_q_c.config(font=fontBtn)
            curr_quest_to_del_m.place(x=10, y=235)

            mod_del_quest_btn = tk.Button(mod_features, text="Erase", font=fontBtn,
                                          command=lambda: del_quest_from_db(curr_quest_to_del.get()))
            mod_del_quest_btn.place(x=10, y=285)

            mod_edit_quest_btn = tk.Button(mod_features, text="Edit", font=fontBtn,
                                           command=lambda: edit_quest_frame(curr_mod_name, curr_quest_to_del.get())
                                           )
            mod_edit_quest_btn.place(x=90, y=285)

            # --------------- Change Module Name ----------------

        def delBtnModsAndUpdate():
            if self.isActive is True:
                row = 2
                col = 0
                count = len(fetchModules())
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
                mod_btn = tk.Button(head, text=mod_txt, font=fontBtn, width=15, height=1,
                                    command=lambda i=mod_txt: change_mod_name(i))
                mod_btn.grid(row=row, column=col, padx=15, pady=20)

                row += 1
                if row == 7:
                    row = 2
                    col += 1
                getModules.pop()

            self.isActive = True

        delBtnModsAndUpdate()

        def toText(module):
            # This additional function is used
            # to separate the string module
            # name from other non alphabet characters
            i = 0
            z = len(module) - 1
            az = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
            while module[i] not in az:
                i += 1
            while module[z] not in az:
                z -= 1

            return module[i:z + 1]

        # ---------------END OF USEFUL FUNCTIONS ---------------

        # ---------------ADD MODULE---------------
        def chooseTypeOfQuestion(curr_mod_name=False):
            window = tk.Tk()
            window.resizable(0, 0)
            window.geometry("700x600")
            head = tk.LabelFrame(window, text="Admin Page", bg='#FBFDF4', font=fontFrame, bd=1)
            head.pack(fill='both', expand='yes', padx=10, pady=10)
            title = tkFont.Font(
                family="Arial",
                size=25,
            )
            opt_title = tkFont.Font(
                family="Arial",
                size=20
            )
            opts = tkFont.Font(
                family="Arial",
                size=60
            )
            l1 = tk.Label(head, text="Select a type of questions for the module", font=title)
            l1.place(x=20, y=50)

            def TypeQuest(type, mod_name=False):
                # TRUE OR FALSE FORM

                # 1.This frame collects all the information
                # necessary to create the module and a
                # first TF question in the database
                #
                # 2.It then add it to the database through
                # a click an erase the window and update
                # the buttons so the changes can me seen instantly.
                #
                # 3.In order to accomplish this,
                #  different type of sqlite
                #  commands are used, each with a different purpose

                window.destroy()
                tf_form = tk.Tk()
                fontFrame = tkFont.Font(
                    family="Arial",
                    size=16,
                    weight='bold')
                ques_title = tkFont.Font(
                    family="Arial",
                    size=14
                )
                tf_form.resizable(0, 0)
                tf_form.geometry("700x600")

                head = tk.LabelFrame(tf_form, text="Admin Page", bg='#FBFDF4', font=fontFrame, bd=1)
                head.pack(fill='both', expand='yes', padx=20, pady=10)

                l1 = tk.Label(head, text="Module Name: ", font=ques_title)
                l1.place(x=10, y=10)

                max_score = tk.Label(head, text="Score the user should get if  answered correctly: ", font=ques_title)
                max_score.place(x=10, y=60)

                e_score = tk.Entry(head, width=5)
                e_score.place(x=350, y=60)

                if mod_name:
                    mod_name_title = tk.Label(head, text=curr_mod_name, font=fontTitle)
                    mod_name_title.place(x=350, y=10)
                else:
                    e1 = tk.Entry(head, width=30)
                    e1.place(x=350, y=10)

                l2 = tk.Label(head, text="Question: ", font=ques_title)
                l2.place(x=10, y=110)

                e2 = tk.Entry(head, width=30)
                e2.place(x=350, y=110)
                max_score = tk.Label(head, text="Score the user should get if  answered correctly: ", font=ques_title)
                max_score.place(x=10, y=60)

                exist_mod = True if mod_name else False

                def is_mod_name():
                    if mod_name:
                        return mod_name
                    return e1.get()

                if type == 'tf':
                    ans_l = tk.Label(head, text="Correct Answer: ", font=ques_title)
                    ans_l.place(x=10, y=150)

                    ans_e = tk.Entry(head, width=30)
                    ans_e.place(x=350, y=150)

                    inc_ans = 'true' if ans_e.get() == 'false' else 'false'

                    submit_mod = tk.Button(head, text="add Module",
                                           command=lambda: register_mod_DB(is_mod_name(),
                                                                           e2.get(),
                                                                           ans_e.get().lower(),
                                                                           inc_ans,
                                                                           tf_form,
                                                                           type,
                                                                           e_score.get(),
                                                                           exist_mod
                                                                           ))
                    submit_mod.place(x=130, y=320)

                if type == 'mcq':
                    # The user needs to able to choose how many answers/inc answers want to have
                    # therefore the approach I'm going to take is as follows
                    # 1. Let the user choose amount of answers
                    # 2. Let the user choose amount of inc_ans
                    # 3. Base on that display entries for the user type on them.
                    # 4. Store ans and inc ans in DB
                    # 5. Prompt Feedback Frame
                    choices = [1, 2, 3]
                    l_ans = tk.Label(head,
                                     text="Now Select the amount of answers and incorrect answers you want your question to have. Max = 5")
                    l_ans.place(x=10, y=150)

                    # Number of answers of the question
                    l_num_ans = tk.Label(head, text="N. Answers: ")
                    l_num_ans.place(x=10, y=180)

                    l_num_ans = tk.Label(head, text="N. Inc. Answers: ")
                    l_num_ans.place(x=300, y=180)

                    ans_1 = tk.Entry(head, width=30)
                    ans_1.place(x=100, y=220)

                    ans_1 = tk.Entry(head, width=30)
                    ans_1.place(x=100, y=220)
                    ans_2 = tk.Entry(head, width=30)
                    ans_2.place(x=100, y=250)

                    ans_1 = tk.Entry(head, width=30)
                    ans_1.place(x=100, y=220)
                    ans_2 = tk.Entry(head, width=30)
                    ans_2.place(x=100, y=250)
                    ans_3 = tk.Entry(head, width=30)
                    ans_3.place(x=100, y=280)

                    inc_ans_1 = tk.Entry(head, width=30)
                    inc_ans_1.place(x=300, y=220)

                    inc_ans_1 = tk.Entry(head, width=30)
                    inc_ans_1.place(x=300, y=220)
                    inc_ans_2 = tk.Entry(head, width=30)
                    inc_ans_2.place(x=300, y=250)

                    inc_ans_1 = tk.Entry(head, width=30)
                    inc_ans_1.place(x=300, y=220)
                    inc_ans_2 = tk.Entry(head, width=30)
                    inc_ans_2.place(x=300, y=250)
                    inc_ans_3 = tk.Entry(head, width=30)
                    inc_ans_3.place(x=300, y=280)

                    def store_inc_and_corr_answers_in_db():
                        is_to_much = [ans_1.get(), ans_2.get(), ans_3.get(), inc_ans_3.get(), inc_ans_1.get(),
                                      inc_ans_2.get()]
                        q = 0
                        for x in is_to_much:
                            if x != '':
                                q += 1
                        if q >= 6:
                            tk.messagebox.showerror("showerror", "You can only add 5 answers/incorrect answers at most")
                            tf_form.destroy()
                            return

                        def grab_only_ans(*args):
                            l = []
                            for x in args:
                                if x != '':
                                    l.append(x)
                            return ",".join(l)

                        list_of_inc_ans = grab_only_ans(inc_ans_1.get(), inc_ans_2.get(), inc_ans_3.get())
                        list_of_ans = grab_only_ans(ans_1.get(), ans_2.get(), ans_3.get())

                        register_mod_DB(is_mod_name(),
                                        e2.get(),
                                        list_of_ans.lower(),
                                        list_of_inc_ans,
                                        tf_form,
                                        type,
                                        e_score.get(),
                                        exist_mod)

                    submit_mod = tk.Button(head, text="add Module", command=lambda: store_inc_and_corr_answers_in_db())
                    submit_mod.place(x=130, y=320)

                if type == 'bm':
                    # Enter 3-5 answers that others possible answers will be matched to

                    t_ans = tk.Label(head,
                                     text="Enter 1-5 answers. This will answers will be used as the match for other possible answers",
                                     font=fontTitle)
                    t_ans.place(x=10, y=150)

                    p_ans_1 = tk.Entry(head, width=30)
                    p_ans_2 = tk.Entry(head, width=30)
                    p_ans_3 = tk.Entry(head, width=30)
                    p_ans_4 = tk.Entry(head, width=30)
                    p_ans_5 = tk.Entry(head, width=30)

                    p_ans_1.place(x=10, y=180)
                    p_ans_2.place(x=10, y=220)
                    p_ans_3.place(x=10, y=260)
                    p_ans_4.place(x=10, y=300)
                    p_ans_5.place(x=10, y=340)

                    def phase_1_of_bma():
                        def grab_only_ans(*args):
                            l = []
                            for x in args:
                                if x != '':
                                    l.append(x)
                            return ",".join(l)

                        list_of_ans = grab_only_ans(p_ans_1.get(), p_ans_2.get(), p_ans_3.get(), p_ans_4.get(),
                                                    p_ans_5.get())
                        register_mod_DB(
                            is_mod_name(),
                            e2.get(),
                            list_of_ans.lower(),
                            '',
                            tf_form,
                            type,
                            e_score.get(),
                            exist_mod
                        )

                    submit_mod_bm = tk.Button(head, text="Continue", command=lambda: phase_1_of_bma())
                    submit_mod_bm.place(x=200, y=370)

            options = tk.LabelFrame(head, text="Options: ", font=opt_title)
            options.pack(fill='both', expand='yes', padx=20, pady=100)
            op1 = tk.Button(options, text="TF", font=opts, width=20, height=7,
                            command=lambda: TypeQuest('tf', curr_mod_name))
            op1.pack(side=tk.LEFT)
            op2 = tk.Button(options, text="MCQ", font=opts, width=20, height=7,
                            command=lambda: TypeQuest('mcq', curr_mod_name))
            op2.pack(side=tk.LEFT)
            op3 = tk.Button(options, text="BM", font=opts, width=20, height=7,
                            command=lambda: TypeQuest('bm', curr_mod_name))
            op3.pack(side=tk.LEFT)

        # SQLITE COMMANDS
        def add_feed_to_DB(q_id, name, text, m_id):
            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "INSERT INTO Feedback (quest_id, feed_ans_name, feed_text, mod_id)\
                                                        Values " + "(" + str(q_id) + ", '" + name + "' , '" \
                                      + text + "'," + str(m_id) + ");"
                print(sqlite_insert_query)
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                print("Feedback of Answer Succesfully Inserted")
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to insert feedback of answer into Sqlite ", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

        def add_mod(mod_name):
            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "INSERT INTO Modules (mod_name) Values " + "('" + mod_name + "')"
                print(sqlite_insert_query)
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                print("Moduled added succesfully")
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to insert Module into sqlite table", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

            # Register Questions from Module

        def add_quest(quest_name, quest_mod_id, possible_answers, answer, mark, quest_type):

            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")
                sqlite_insert_query = "INSERT INTO Questions (quest_name," \
                                      " mod_id, quest_times, answer, possible_answers, quest_mark, quest_type)" \
                                      " Values " + "('" + quest_name + "'" + ",'" + quest_mod_id + "'" + \
                                      ", '" + str(0) + "'" + ",'" + answer + "'" + ",'" + possible_answers + \
                                      "', '" + mark + "', '" + quest_type + "');"
                print(sqlite_insert_query)
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                print("Question added succesfully")
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to insert question into sqlite ", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

        def add_bma_ans(quest_id, father, child, mod_id):
            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")
                sqlite_insert_query = "INSERT INTO BestMatchAns (quest_id," \
                                      " bma_father, bma_child, mod_id)" \
                                      " Values " + "('" + str(quest_id) + "'" + ",'" + father + "'" + \
                                      ", '" + child + "'" + ",'" + str(mod_id) + "');"
                print(sqlite_insert_query)
                count = cursor.execute(sqlite_insert_query)
                sqliteConnection.commit()
                print("bma answer added succesfully")
                cursor.close()
            except sqlite3.Error as error:
                print("Failed to insert bma answer into sqlite ", error)
            finally:
                if sqliteConnection:
                    sqliteConnection.close()
                    print("The SQLite connection is closed")

        # BMA FRAME TO GET ALL POSSIBLE ANSWERS
        def get_inc_ans_from_bma_frame(quest, typeofQuest, ans, currForm):
            currForm.destroy()
            bma_phase_2 = tk.Tk()
            bma_phase_2.resizable(0, 0)
            bma_phase_2.geometry("700x600")

            admin_phase_2 = tk.LabelFrame(bma_phase_2, text="Admin Page", bg='#FBFDF4', font=fontFrame, bd=1)
            admin_phase_2.pack(fill='both', expand='yes', padx=20, pady=10)

            t_phase_2 = tk.Label(admin_phase_2,
                                 text="Now, Type 1-5 possible answers and match them to their corresponding answer.",
                                 font=fontTitle)
            t_phase_2.place(x=10, y=10)

            bma_p2_ans_1 = tk.Entry(admin_phase_2, width=30)
            bma_p2_ans_2 = tk.Entry(admin_phase_2, width=30)
            bma_p2_ans_3 = tk.Entry(admin_phase_2, width=30)
            bma_p2_ans_4 = tk.Entry(admin_phase_2, width=30)
            bma_p2_ans_5 = tk.Entry(admin_phase_2, width=30)

            bma_p2_ans_1.place(x=10, y=50)
            bma_p2_ans_2.place(x=10, y=100)
            bma_p2_ans_3.place(x=10, y=150)
            bma_p2_ans_4.place(x=10, y=200)
            bma_p2_ans_5.place(x=10, y=250)

            # First Answer DropDown Menu list
            curr_bma_ans_1 = tk.StringVar(admin_phase_2)
            curr_bma_ans_1.set("Choose Match")  # default value

            curr_bma_ans_1_c = tk.OptionMenu(admin_phase_2, curr_bma_ans_1, *ans.split(','))
            curr_bma_ans_1_c.config(font=fontBtn)
            menu_1 = admin_phase_2.nametowidget(curr_bma_ans_1_c.menuname)
            menu_1.config(font=fontBtn)
            curr_bma_ans_1_c.place(x=200, y=45)

            # Second Answer DropDown Menu List

            curr_bma_ans_2 = tk.StringVar(admin_phase_2)
            curr_bma_ans_2.set("Choose Match")  # default value

            curr_bma_ans_2_c = tk.OptionMenu(admin_phase_2, curr_bma_ans_2, *ans.split(','))
            curr_bma_ans_2_c.config(font=fontBtn)
            menu_2 = admin_phase_2.nametowidget(curr_bma_ans_2_c.menuname)
            menu_2.config(font=fontBtn)
            curr_bma_ans_2_c.place(x=200, y=95)

            # Third Answer Drop Down Menu List

            curr_bma_ans_3 = tk.StringVar(admin_phase_2)
            curr_bma_ans_3.set("Choose Match")  # default value

            curr_bma_ans_3_c = tk.OptionMenu(admin_phase_2, curr_bma_ans_3, *ans.split(','))
            curr_bma_ans_3_c.config(font=fontBtn)
            menu_3 = admin_phase_2.nametowidget(curr_bma_ans_3_c.menuname)
            menu_3.config(font=fontBtn)
            curr_bma_ans_3_c.place(x=200, y=145)

            # Fourth Answer Drop Down Menu List

            curr_bma_ans_4 = tk.StringVar(admin_phase_2)
            curr_bma_ans_4.set("Choose Match")  # default value

            curr_bma_ans_4_c = tk.OptionMenu(admin_phase_2, curr_bma_ans_4, *ans.split(','))
            curr_bma_ans_4_c.config(font=fontBtn)
            menu_4 = admin_phase_2.nametowidget(curr_bma_ans_4_c.menuname)
            menu_4.config(font=fontBtn)
            curr_bma_ans_4_c.place(x=200, y=195)

            # Fifth Answer Drop Down Menu list

            curr_bma_ans_5 = tk.StringVar(admin_phase_2)
            curr_bma_ans_5.set("Choose Match")  # default value

            curr_bma_ans_5_c = tk.OptionMenu(admin_phase_2, curr_bma_ans_5, *ans.split(','))
            curr_bma_ans_5_c.config(font=fontBtn)
            menu_5 = admin_phase_2.nametowidget(curr_bma_ans_5_c.menuname)
            menu_5.config(font=fontBtn)
            curr_bma_ans_5_c.place(x=200, y=245)

            def update_bms_db_poss_ans(children, q_id):
                c = ",".join(children)

                try:
                    sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                    cursor = sqliteConnection.cursor()
                    print("Succesfully connected to SQLite")
                    sqlite_insert_query = "UPDATE QUESTIONS " \
                                          "SET possible_answers = " + "'" + c + "'" + " where quest_id = " + str(q_id)

                    print(sqlite_insert_query)
                    count = cursor.execute(sqlite_insert_query)
                    sqliteConnection.commit()
                    print("bma possible answer updated succesfully")
                    cursor.close()
                except sqlite3.Error as error:
                    print("Failed to insert bma possible answer child into sqlite ", error)
                finally:
                    if sqliteConnection:
                        sqliteConnection.close()
                        print("The SQLite connection is closed")

            def execute_bma_add():
                q_id, m_id = find_mod_quest_id(quest)
                answers = []
                if bma_p2_ans_1.get() != '':
                    add_bma_ans(q_id, curr_bma_ans_1.get(), bma_p2_ans_1.get(), m_id)
                    answers.append(bma_p2_ans_1.get())
                if bma_p2_ans_2.get() != '':
                    add_bma_ans(q_id, curr_bma_ans_2.get(), bma_p2_ans_2.get(), m_id)
                    answers.append(bma_p2_ans_2.get())
                if bma_p2_ans_3.get() != '':
                    add_bma_ans(q_id, curr_bma_ans_3.get(), bma_p2_ans_3.get(), m_id)
                    answers.append(bma_p2_ans_3.get())
                if bma_p2_ans_4.get() != '':
                    add_bma_ans(q_id, curr_bma_ans_4.get(), bma_p2_ans_4.get(), m_id)
                    answers.append(bma_p2_ans_4.get())
                if bma_p2_ans_5.get() != '':
                    add_bma_ans(q_id, curr_bma_ans_5.get(), bma_p2_ans_5.get(), m_id)
                    answers.append(bma_p2_ans_5.get())
                update_bms_db_poss_ans(answers, q_id)

                add_feed_frame(q_id, answers, bma_phase_2, m_id, True)

            bma_btn = tk.Button(admin_phase_2, text="Continue", command=lambda: execute_bma_add())
            bma_btn.place(x=200, y=320)

        def add_feed_frame(quest_id, answers, prevForm, m_id, bma=False):
            prevForm.destroy()
            feed_form = tk.Tk()

            fontFrame = tkFont.Font(
                family="Arial",
                size=16,
                weight='bold')
            ques_title = tkFont.Font(
                family="Arial",
                size=14
            )
            feed_form.resizable(0, 0)
            feed_form.geometry("700x600")

            f_head = tk.LabelFrame(feed_form, text="Admin Page", bg='#FBFDF4', font=fontFrame, bd=1)
            f_head.pack(fill='both', expand='yes', padx=20, pady=10)

            if bma:
                t1 = tk.Label(f_head, text="Now write why do they match to each other", font=fontFrame)
                t1.place(x=10, y=10)
            else:
                t1 = tk.Label(f_head, text="Now write why each answer is correct/incorrect:", font=fontFrame)
                t1.place(x=10, y=10)

            l = len(answers)
            c_x, c_y = 40, 50
            # Hacky Way of displaying entries.
            # Target: Display all answers with entries
            # for the user to write feedback why it is wrong/right
            # Since we cannot id entries and access them manually,
            # Im going to first:
            # 1. Find the length of answers
            # 2. display As many entries as answers are.
            # 3. base on length again insert feedback
            t_1 = tk.Label(f_head, text="match to ", font=ques_title)
            t_2 = tk.Label(f_head, text="match to ", font=ques_title)
            t_3 = tk.Label(f_head, text="match to ", font=ques_title)
            t_4 = tk.Label(f_head, text="match to ", font=ques_title)
            t_5 = tk.Label(f_head, text="match to ", font=ques_title)

            if bma:
                fathers = get_fathers_from_children(answers)
                if l == 2:
                    t_1.place(x=c_x * 5, y=c_y)
                    t_2.place(x=c_x * 5, y=c_y * 2)

                    f_1 = tk.Label(f_head, text=fathers[0], font=ques_title)
                    f_2 = tk.Label(f_head, text=fathers[1], font=ques_title)

                    f_1.place(x=c_x * 8, y=c_y)
                    f_2.place(x=c_x * 8, y=c_y * 2)
                if l == 3:
                    t_1.place(x=c_x * 5, y=c_y)
                    t_2.place(x=c_x * 5, y=c_y * 2)
                    t_3.place(x=c_x * 5, y=c_y * 3)

                    f_1 = tk.Label(f_head, text=fathers[0], font=ques_title)
                    f_2 = tk.Label(f_head, text=fathers[1], font=ques_title)
                    f_3 = tk.Label(f_head, text=fathers[2], font=ques_title)

                    f_1.place(x=c_x * 8, y=c_y)
                    f_2.place(x=c_x * 8, y=c_y * 2)
                    f_3.place(x=c_x * 8, y=c_y * 3)

                if l == 4:
                    t_1.place(x=c_x * 5, y=c_y)
                    t_2.place(x=c_x * 5, y=c_y * 2)
                    t_3.place(x=c_x * 5, y=c_y * 3)
                    t_4.place(x=c_x * 5, y=c_y * 4)

                    f_1 = tk.Label(f_head, text=fathers[0], font=ques_title)
                    f_2 = tk.Label(f_head, text=fathers[1], font=ques_title)
                    f_3 = tk.Label(f_head, text=fathers[2], font=ques_title)
                    f_4 = tk.Label(f_head, text=fathers[3], font=ques_title)

                    f_1.place(x=c_x * 8, y=c_y)
                    f_2.place(x=c_x * 8, y=c_y * 2)
                    f_3.place(x=c_x * 8, y=c_y * 3)
                    f_4.place(x=c_x * 8, y=c_y * 4)
                if l == 5:
                    t_1.place(x=c_x * 5, y=c_y)
                    t_2.place(x=c_x * 5, y=c_y * 2)
                    t_3.place(x=c_x * 5, y=c_y * 3)
                    t_4.place(x=c_x * 5, y=c_y * 4)
                    t_5.place(x=c_x * 5, y=c_y * 5)

                    f_1 = tk.Label(f_head, text=fathers[0], font=ques_title)
                    f_2 = tk.Label(f_head, text=fathers[1], font=ques_title)
                    f_3 = tk.Label(f_head, text=fathers[2], font=ques_title)
                    f_4 = tk.Label(f_head, text=fathers[3], font=ques_title)
                    f_5 = tk.Label(f_head, text=fathers[4], font=ques_title)

                    f_1.place(x=c_x * 8, y=c_y)
                    f_2.place(x=c_x * 8, y=c_y * 2)
                    f_3.place(x=c_x * 8, y=c_y * 3)
                    f_4.place(x=c_x * 8, y=c_y * 4)
                    f_5.place(x=c_x * 8, y=c_y * 5)

            if l == 2:
                ans1 = tk.Label(f_head, text=answers[0], font=ques_title)
                ans1.place(x=c_x, y=c_y)
                e_ans1 = tk.Entry(f_head, width=40)
                e_ans1.place(x=c_x * 11, y=c_y)

                ans2 = tk.Label(f_head, text=answers[1], font=ques_title)
                ans2.place(x=c_x, y=c_y * 2)
                e_ans2 = tk.Entry(f_head, width=40)
                e_ans2.place(x=c_x * 11, y=c_y * 2)
            if l == 3:
                ans1 = tk.Label(f_head, text=answers[0], font=ques_title)
                ans1.place(x=c_x, y=c_y)
                e_ans1 = tk.Entry(f_head, width=40)
                e_ans1.place(x=c_x * 11, y=c_y)

                ans2 = tk.Label(f_head, text=answers[1], font=ques_title)
                ans2.place(x=c_x, y=c_y * 2)
                e_ans2 = tk.Entry(f_head, width=40)
                e_ans2.place(x=c_x * 11, y=c_y * 2)

                ans3 = tk.Label(f_head, text=answers[2], font=ques_title)
                ans3.place(x=c_x, y=c_y * 3)
                e_ans3 = tk.Entry(f_head, width=40)
                e_ans3.place(x=c_x * 11, y=c_y * 3)

            if l == 4:
                ans1 = tk.Label(f_head, text=answers[0], font=ques_title)
                ans1.place(x=c_x, y=c_y)
                e_ans1 = tk.Entry(f_head, width=40)
                e_ans1.place(x=c_x * 11, y=c_y)

                ans2 = tk.Label(f_head, text=answers[1], font=ques_title)
                ans2.place(x=c_x, y=c_y * 2)
                e_ans2 = tk.Entry(f_head, width=40)
                e_ans2.place(x=c_x * 11, y=c_y * 2)

                ans3 = tk.Label(f_head, text=answers[2], font=ques_title)
                ans3.place(x=c_x, y=c_y * 3)
                e_ans3 = tk.Entry(f_head, width=40)
                e_ans3.place(x=c_x * 11, y=c_y * 3)

                ans4 = tk.Label(f_head, text=answers[3], font=ques_title)
                ans4.place(x=c_x, y=c_y * 4)
                e_ans4 = tk.Entry(f_head, width=40)
                e_ans4.place(x=c_x * 11, y=c_y * 4)
            if l == 5:
                ans1 = tk.Label(f_head, text=answers[0], font=ques_title)
                ans1.place(x=c_x, y=c_y)
                e_ans1 = tk.Entry(f_head, width=40)
                e_ans1.place(x=c_x * 11, y=c_y)

                ans2 = tk.Label(f_head, text=answers[1], font=ques_title)
                ans2.place(x=c_x, y=c_y * 2)
                e_ans2 = tk.Entry(f_head, width=40)
                e_ans2.place(x=c_x * 11, y=c_y * 2)

                ans3 = tk.Label(f_head, text=answers[2], font=ques_title)
                ans3.place(x=c_x, y=c_y * 3)
                e_ans3 = tk.Entry(f_head, width=40)
                e_ans3.place(x=c_x * 11, y=c_y * 3)

                ans4 = tk.Label(f_head, text=answers[3], font=ques_title)
                ans4.place(x=c_x, y=c_y * 4)
                e_ans4 = tk.Entry(f_head, width=40)
                e_ans4.place(x=c_x * 11, y=c_y * 4)

                ans5 = tk.Label(f_head, text=answers[4], font=ques_title)
                ans5.place(x=c_x, y=c_y * 5)
                e_ans5 = tk.Entry(f_head, width=40)
                e_ans5.place(x=c_x * 11, y=c_y * 5)

            def insert_all_feed():
                if l == 2:
                    add_feed_to_DB(quest_id, answers[0], e_ans1.get(), m_id)
                    add_feed_to_DB(quest_id, answers[1], e_ans2.get(), m_id)
                if l == 3:
                    add_feed_to_DB(quest_id, answers[0], e_ans1.get(), m_id)
                    add_feed_to_DB(quest_id, answers[1], e_ans2.get(), m_id)
                    add_feed_to_DB(quest_id, answers[2], e_ans3.get(), m_id)
                if l == 4:
                    add_feed_to_DB(quest_id, answers[0], e_ans1.get(), m_id)
                    add_feed_to_DB(quest_id, answers[1], e_ans2.get(), m_id)
                    add_feed_to_DB(quest_id, answers[2], e_ans3.get(), m_id)
                    add_feed_to_DB(quest_id, answers[3], e_ans4.get(), m_id)
                if l == 5:
                    add_feed_to_DB(quest_id, answers[0], e_ans1.get(), m_id)
                    add_feed_to_DB(quest_id, answers[1], e_ans2.get(), m_id)
                    add_feed_to_DB(quest_id, answers[2], e_ans3.get(), m_id)
                    add_feed_to_DB(quest_id, answers[3], e_ans4.get(), m_id)
                    add_feed_to_DB(quest_id, answers[4], e_ans5.get(), m_id)

                feed_form.destroy()

            feed_form_sub = tk.Button(f_head, text="Submit", font=ques_title, command=insert_all_feed)
            feed_form_sub.place(x=500, y=500)

        def register_mod_DB(mod_name, start_quest, ans, inc_ans, currForm, typeOfQuestion, mark, mod_exist=False):
            #
            # 1. We add the module to database so it has a Key
            # 2. We find that key
            # 3. We can now add questions to its own table having access to the specific foreign key (mod_id)
            #
            # Add otherAnswer and times attribute when adding to DB

            if typeOfQuestion == 'tf':
                # ADD MODULE TO DB
                onlyDeleteBtnModules()
                if mod_exist is False:
                    add_mod(mod_name)

                e6 = findModId(mod_name)
                # ADD QUESTIONS TO DB
                add_quest(start_quest, e6, inc_ans, ans, mark, typeOfQuestion)

                q_id = find_quest_id(start_quest)
                delBtnModsAndUpdate()
                # ADD FEEDBACK TO DB
                all_ans = [ans, inc_ans]
                # hacky way of inserting question id to the feedback
                add_feed_frame(q_id, all_ans, currForm, e6)
            elif typeOfQuestion == 'mcq':
                all_ans = inc_ans.split(',') + ans.split(',')
                onlyDeleteBtnModules()
                if mod_exist is False:
                    add_mod(mod_name)
                e6 = findModId(mod_name)
                add_quest(start_quest, e6, inc_ans, ans, mark, typeOfQuestion)
                q_id = find_quest_id(start_quest)
                delBtnModsAndUpdate()
                add_feed_frame(q_id, all_ans, currForm, e6)
            elif typeOfQuestion == 'bm':
                # NEED TO CONSIDER TWO THINGS
                # The Admin can add some options
                # Each of these options can have some answers
                # the app should store these answers and options
                # How can we link these options and answer to determine which belongs to which?
                # IDEA1: Create a new Answers Table that will hold the answers and its option.
                # This way we can just fetch this entities and compare them with what the user matched in the app.
                # Idea 2: ADD an  "A" To the beginning of each option and Answer so we know they are connected.
                # We would just need to check the first letter to determine the correctness of the user match.
                onlyDeleteBtnModules()
                if mod_exist is False:
                    add_mod(mod_name)
                e6 = findModId(mod_name)
                add_quest(start_quest, e6, inc_ans, ans, mark, typeOfQuestion)
                delBtnModsAndUpdate()
                get_inc_ans_from_bma_frame(start_quest, typeOfQuestion, ans, currForm)

        add_mod_btn = tk.Button(head, text="New Module", font=fontBtn, command=chooseTypeOfQuestion)
        add_mod_btn.grid(row=0, column=1, padx=(100, 0))

        # -----------------ORDER TO DELETE A MODULE----------------
        #     1. Delete All questions from Databases
        #     2. Delete Module From database
        #     3. Close window frame and DeleteAndUpdate
        #
        def delModuleFrame():
            window = tk.Tk()
            window.resizable(0, 0)
            window.geometry("320x200")
            window.title("Delete Module")
            currModule = tk.StringVar(window)
            currModule.set("--Select Module--")  # default value

            # Here the dropdown menu is created
            # using the 'data' modules
            # from the database.
            chooseTest = tk.OptionMenu(window, currModule, *fetchModules())
            chooseTest.config(font=('Arial', 15, 'bold'))
            menu = window.nametowidget(chooseTest.menuname)
            menu.config(font=('Arial', 10, 'bold'))
            chooseTest.place(x=20, y=20)

            def delAllFeedbackFromDB(moduleId):
                # In order to delete a module,
                # we first need to delete all
                # the feedback & questions from that
                # module because they are
                # connected throught a
                # foreign key and thus
                # cannot be deleted without
                # first all questions are removed.
                try:
                    sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                    cursor = sqliteConnection.cursor()
                    print("Succesfully connected to SQLite")

                    sqlite_insert_query = "DELETE FROM Feedback WHERE mod_id = " + moduleId + ";"
                    print(sqlite_insert_query)
                    count = cursor.execute(sqlite_insert_query)
                    sqliteConnection.commit()
                    print("Feedback Succesfully Deleted")
                    cursor.close()
                except sqlite3.Error as error:
                    print("Failed to Delete Feedback into Sqlite ", error)
                finally:
                    if sqliteConnection:
                        sqliteConnection.close()
                        print("The SQLite connection is closed")

            def delAllBmaFromDB(moduleId):
                # In order to delete a module,
                # we first need to delete all
                # the quesions & feedback & bma if it has from that
                # module because they are
                # connected throught a
                # foreign key and thus
                # cannot be deleted without
                # first all questions are removed.
                try:
                    sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                    cursor = sqliteConnection.cursor()
                    print("Succesfully connected to SQLite")

                    sqlite_insert_query = "DELETE FROM BestMatchAns WHERE mod_id = " + moduleId + ";"
                    print(sqlite_insert_query)
                    count = cursor.execute(sqlite_insert_query)
                    sqliteConnection.commit()
                    print("bma answers Succesfully Deleted")
                    cursor.close()
                except sqlite3.Error as error:
                    print("Failed to Delete bma answers ", error)
                finally:
                    if sqliteConnection:
                        sqliteConnection.close()
                        print("The SQLite connection is closed")

            def delAllQuestionsFromDB(moduleId):
                # In order to delete a module,
                # we first need to delete all
                # the quesions & feedback from that
                # module because they are
                # connected throught a
                # foreign key and thus
                # cannot be deleted without
                # first all questions are removed.
                try:
                    sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                    cursor = sqliteConnection.cursor()
                    print("Succesfully connected to SQLite")

                    sqlite_insert_query = "DELETE FROM Questions WHERE mod_id = " + moduleId + ";"
                    print(sqlite_insert_query)
                    count = cursor.execute(sqlite_insert_query)
                    sqliteConnection.commit()
                    print("Questions Succesfully Deleted")
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
                    print("Successfully connected to SQLite")

                    sqlite_insert_query = "DELETE FROM Modules WHERE mod_name = '" + moduleName + "';"
                    print(sqlite_insert_query)
                    count = cursor.execute(sqlite_insert_query)
                    sqliteConnection.commit()
                    print("Module Successfully Deleted")
                    cursor.close()
                except sqlite3.Error as error:
                    print("Failed to Delete questions into Sqlite ", error)
                finally:
                    if sqliteConnection:
                        sqliteConnection.close()
                        print("The SQLite connection is closed")

            def deleteModule():
                # ----------------MAIN DELETE MODULE FUNCTION--------------

                # In order to make the app more dynamic.
                # 1. Remove all widget buttons from the frame
                # 2. Delete all feedback from the db of feedback from module chosen id
                # 2. Delete all questions from the db of questions from module chosen
                # 3. Delete Module from DB
                # 4. Display all buttons widgets again
                # 5. Delete frame window itself
                onlyDeleteBtnModules()
                mod_to_delete = toText(currModule.get())
                get_mod_id = findModId(mod_to_delete)
                delAllFeedbackFromDB(get_mod_id)
                delAllBmaFromDB(get_mod_id)
                delAllQuestionsFromDB(get_mod_id)
                delModFromDB(mod_to_delete)
                delBtnModsAndUpdate()
                window.destroy()

            sub_del = tk.Button(window, text="erase", font=('Arial', 14, 'bold'), command=deleteModule)
            sub_del.place(x=230, y=20)

            alert_txt = tk.Label(window, text="Careful! All questions & feedback will also be erased",
                                 font=('Arial', 8, 'bold'))
            alert_txt.place(x=20, y=120)

        del_mod_btn = tk.Button(head, text="Del Module", font=fontBtn, command=delModuleFrame)
        del_mod_btn.grid(row=0, column=2, padx=(10, 0))
