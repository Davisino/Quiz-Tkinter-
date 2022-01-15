import tkinter as tk
import tkinter.font as tkFont
import sqlite3

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

        titleLabel = tk.Label(head, text="Current Modules", font=fontTitle)
        titleLabel.grid(row=0, column=0, pady=20)

    # ----------- USEFEUL FUNCTIONS ---------
    # From here, you will see some functions
    # that I consider very useful to do the job on the quiz app.
    # It saved me a lot of time, because I had not to code manually sqlite commands anymore.
    # I would just call the function and pass the desired arguments/parameters.

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
        def change_mod_name(curr_mod_name):
            window = tk.Tk()
            window.resizable(0, 0)
            window.geometry("320x150")

            window.title("New Module Name")
            new_name_entry = tk.Entry(window, font=fontBtn, borderwidth=5, width=22)
            new_name_entry.place(x=20, y=20)

            def update_mod_name_in_db(curr_name, desired_name):
                print(curr_name, desired_name, 'sss')
                try:
                    sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                    cursor = sqliteConnection.cursor()
                    print("Succesfully connected to SQLite")

                    sqlite_insert_query = "Update Modules set mod_name = " +\
                                          "'" + desired_name + "'" +\
                                          " where mod_name = " + "'" +\
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

            new_name_sub = tk.Button(window, text="submit", font=fontBtn,  width=7, command= lambda: execute_mod_change(curr_mod_name, new_name_entry.get()))
            new_name_sub.place(x=240, y=16)

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
                mod_btn = tk.Button(head, text=mod_txt, font=fontBtn, width=15, height=1, command=lambda i=mod_txt: change_mod_name(i))
                mod_btn.grid(row=row, column=col, padx=15, pady=20)

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
        def chooseTypeOfQuestion():
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
            def TypeQuest(type):
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

                e1 = tk.Entry(head, width=30)
                e1.place(x=350, y=10)

                l2 = tk.Label(head, text="Question: ", font=ques_title)
                l2.place(x=10, y=110)

                e2 = tk.Entry(head, width=30)
                e2.place(x=350, y=110)

                ans_l = tk.Label(head, text="Correct Answer: ", font=ques_title)
                ans_l.place(x=10, y=150)

                ans_e = tk.Entry(head, width=30)
                ans_e.place(x=350, y=150)

                if type == 'mcq' or type == 'bm':
                    inc_ans = tk.Label(head, text="Other Possible Answer:", font=ques_title)
                    inc_ans.place(x=10, y=200)

                    inc_one = tk.Entry(head, width=30)
                    inc_two = tk.Entry(head, width=30)
                    inc_three = tk.Entry(head, width=30)
                    inc_four = tk.Entry(head, width=30)

                    inc_one.place(x=350, y=200)
                    inc_two.place(x=350, y=230)
                    inc_three.place(x=350, y=260)
                    inc_four.place(x=350, y=290)

                max_score = tk.Label(head, text="Score the user should get if  answered correctly: ", font=ques_title)
                max_score.place(x=10, y=60)

                e_score = tk.Entry(head, width=5)
                e_score.place(x=350, y=60)
                def all_inc_ans(*args):
                    list_of_inc_ans = []
                    for t in args:
                        if t == '':
                            continue
                        list_of_inc_ans.append(t)
                    return list_of_inc_ans



                # register_mod_DB(mod_name, start_quest, ans, feed):
                submit_mod = tk.Button(head, text="add Module",\
                                       command=lambda: register_mod_DB(e1.get(),\
                                                                       e2.get(),\
                                                                       ans_e.get().lower(),\
                                                                       all_inc_ans(inc_one.get(), inc_two.get(), inc_three.get(), inc_four.get()),\
                                                                       tf_form,\
                                                                       type,
                                                                       e_score.get()))
                submit_mod.place(x=130, y=320)



            options = tk.LabelFrame(head, text="Options: ", font=opt_title)
            options.pack(fill='both', expand='yes', padx=20, pady=100)
            op1 = tk.Button(options, text="TF", font=opts, width=20, height=7, command=lambda: TypeQuest('tf'))
            op1.pack(side=tk.LEFT)
            op2 = tk.Button(options, text="MCQ", font=opts, width=20, height=7, command=lambda: TypeQuest('mcq'))
            op2.pack(side=tk.LEFT)
            op3 = tk.Button(options, text="BM", font=opts, width=20, height=7, command=lambda: TypeQuest('bm'))
            op3.pack(side=tk.LEFT)


        # SQLITE COMMANDS
        def add_feed_to_DB(q_id, name, text, m_id):
            try:
                sqliteConnection = sqlite3.connect('./Databases/quiz_storage.db')
                cursor = sqliteConnection.cursor()
                print("Succesfully connected to SQLite")

                sqlite_insert_query = "INSERT INTO Feedback (quest_id, feed_ans_name, feed_text, mod_id)\
                                                        Values " + "(" + q_id + ", '" + name + "' , '" \
                                      + text + "'," + m_id + ");"
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
                                      " Values " + "('" + quest_name + "'" + ",'" + quest_mod_id + "'" +\
                                      ", '" + str(0) + "'" + ",'" + answer + "'" + ",'" + possible_answers +\
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
        def add_feed_frame(quest_id, answers, prevForm, m_id):

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

            if l == 2:
                ans1 = tk.Label(f_head, text=answers[0], font=ques_title)
                ans1.place(x=c_x, y=c_y)
                e_ans1 = tk.Entry(f_head, width=40)
                e_ans1.place(x=c_x * 3, y=c_y)

                ans2 = tk.Label(f_head, text=answers[1], font=ques_title)
                ans2.place(x=c_x, y=c_y * 2)
                e_ans2 = tk.Entry(f_head, width=40)
                e_ans2.place(x=c_x * 3, y=c_y * 2)
            if l == 3:
                ans1 = tk.Label(f_head, text=answers[0], font=ques_title)
                ans1.place(x=c_x, y=c_y)
                e_ans1 = tk.Entry(f_head, width=40)
                e_ans1.place(x=c_x * 3, y=c_y)

                ans2 = tk.Label(f_head, text=answers[1], font=ques_title)
                ans2.place(x=c_x, y=c_y * 2)
                e_ans2 = tk.Entry(f_head, width=40)
                e_ans2.place(x=c_x * 3, y=c_y * 2)

                ans3 = tk.Label(f_head, text=answers[2], font=ques_title)
                ans3.place(x=c_x, y=c_y * 3)
                e_ans3 = tk.Entry(f_head, width=40)
                e_ans3.place(x=c_x * 3, y=c_y * 3)


            if l == 4:
                ans1 = tk.Label(f_head, text=answers[0], font=ques_title)
                ans1.place(x=c_x, y=c_y)
                e_ans1 = tk.Entry(f_head, width=40)
                e_ans1.place(x=c_x * 3, y=c_y)

                ans2 = tk.Label(f_head, text=answers[1], font=ques_title)
                ans2.place(x=c_x, y=c_y * 2)
                e_ans2 = tk.Entry(f_head, width=40)
                e_ans2.place(x=c_x * 3, y=c_y * 2)

                ans3 = tk.Label(f_head, text=answers[2], font=ques_title)
                ans3.place(x=c_x, y=c_y * 3)
                e_ans3 = tk.Entry(f_head, width=40)
                e_ans3.place(x=c_x * 3, y=c_y * 3)

                ans4 = tk.Label(f_head, text=answers[3], font=ques_title)
                ans4.place(x=c_x, y=c_y * 4)
                e_ans4 = tk.Entry(f_head, width=40)
                e_ans4.place(x=c_x * 3, y=c_y * 4)
            if l == 5:
                ans1 = tk.Label(f_head, text=answers[0], font=ques_title)
                ans1.place(x=c_x, y=c_y)
                e_ans1 = tk.Entry(f_head, width=40)
                e_ans1.place(x=c_x * 3, y=c_y)

                ans2 = tk.Label(f_head, text=answers[1], font=ques_title)
                ans2.place(x=c_x, y=c_y * 2)
                e_ans2 = tk.Entry(f_head, width=40)
                e_ans2.place(x=c_x * 3, y=c_y * 2)

                ans3 = tk.Label(f_head, text=answers[2], font=ques_title)
                ans3.place(x=c_x, y=c_y * 3)
                e_ans3 = tk.Entry(f_head, width=40)
                e_ans3.place(x=c_x * 3, y=c_y * 3)

                ans4 = tk.Label(f_head, text=answers[3], font=ques_title)
                ans4.place(x=c_x, y=c_y * 4)
                e_ans4 = tk.Entry(f_head, width=40)
                e_ans4.place(x=c_x * 3, y=c_y * 4)

                ans5 = tk.Label(f_head, text=answers[4], font=ques_title)
                ans5.place(x=c_x, y=c_y * 5)
                e_ans5 = tk.Entry(f_head, width=40)
                e_ans5.place(x=c_x * 3, y=c_y * 5)

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

        def register_mod_DB(mod_name, start_quest, ans, inc_ans, currForm, typeOfQuestion, mark):
            #
            # 1. We add the module to database so it has a Key
            # 2. We find that key
            # 3. We can now add questions to its own table having access to the specific foreign key (mod_id)
            #
            # Add otherAnswer and times attribute when adding to DB
            if typeOfQuestion == 'tf':
                true_false = 'true' if ans == 'false' else 'false'
                # ADD MODULE TO DB
                onlyDeleteBtnModules()
                add_mod(mod_name)
                e6 = findModId(mod_name)
                # ADD QUESTIONS TO DB
                add_quest(start_quest, e6, true_false, ans, mark, typeOfQuestion)
                delBtnModsAndUpdate()
                # ADD FEEDBACK TO DB
                all_ans = [ans, true_false]
                # hacky way of inserting question id to the feedback
                add_feed_frame(e6, all_ans, currForm, e6)
            elif typeOfQuestion == 'mcq':
                all_ans = inc_ans
                all_ans.append(ans)
                onlyDeleteBtnModules()
                add_mod(mod_name)
                e6 = findModId(mod_name)
                add_quest(start_quest, e6, ",".join(inc_ans), ans, mark, typeOfQuestion)
                delBtnModsAndUpdate()
                add_feed_frame(e6, all_ans, currForm, e6)
            elif typeOfQuestion == 'mb':
                # NEED TO CONSIDER TWO THINGS
                # The Admind can add some options
                # Each of these options can have some answers
                # the app should store these answers and options
                # How can we link these options and answer to determine which belongs to which?
                # IDEA1: Create a new Answers Table that will hold the answers and its option.
                        # This way we can just fetch this entities and compare them with what the user matched in the app.
                # Idea 2: ADD an  "A" To the beginning of each option and Answer so we know they are connected.
                        # We would just need to check the first letter to determine the correctness of the user match.
                return

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
                mod_to_delete= toText(currModule.get())
                get_mod_id = findModId(mod_to_delete)
                delAllFeedbackFromDB(get_mod_id)
                delAllQuestionsFromDB(get_mod_id)
                delModFromDB(mod_to_delete)
                delBtnModsAndUpdate()
                window.destroy()

            sub_del = tk.Button(window, text="erase", font= ('Arial', 14, 'bold'), command=deleteModule)
            sub_del.place(x=230, y=20)

            alert_txt = tk.Label(window, text="Careful! All questions & feedback will also be erased", font=('Arial', 8, 'bold'))
            alert_txt.place(x=20, y=120)

        del_mod_btn = tk.Button(head, text="Del Module", font=fontBtn, command=delModuleFrame)
        del_mod_btn.grid(row=0, column=2, padx=(10, 0))


