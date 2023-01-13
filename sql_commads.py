
import sqlite3

def findModId(module_name):
    conn = sqlite3.connect('./question_bank.db')
    cursor = conn.execute("SELECT mod_id FROM Modules where mod_name = '" + module_name + "';")
    row = cursor.fetchall()

    return str(row[0][0]) if row != [] else False

def get_quest_id(question):
  
    modules = ''
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
        cursor = sqliteConnection.cursor()
        print("Succesfully connected to SQLite")

        sqlite_insert_query = "SELECT quest_id from Questions " \
                              "where quest_name = '" + question + "' "
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        modules = count.fetchall()
        modules = [x[0] for x in modules]

        cursor.close()
    except sqlite3.Error as error:
        print("Failed to fetch data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return modules[0]

def fetchFeedbackFromQuestion(question, user_answer):
    
    quest_id = get_quest_id(question)
    modules = ''
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
        cursor = sqliteConnection.cursor()
        print("Succesfully connected to SQLite")

        sqlite_insert_query = "SELECT feed_text from Feedback " \
                              "where quest_id = '" + str(quest_id) + "' "\
                            " and feed_ans_name = '" + user_answer + "'" 
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        modules = count.fetchall()
        modules = [x[0] for x in modules]

        cursor.close()
    except sqlite3.Error as error:
        print("Failed to fetch data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return modules[0]

def fetchPointsFromQuestion(question):
    
    modules = ''
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
        cursor = sqliteConnection.cursor()
        print("Succesfully connected to SQLite")

        sqlite_insert_query = "SELECT quest_mark from Questions " \
                              "where quest_name = '" + question + "'"
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        modules = count.fetchall()
        modules = [x[0] for x in modules]

        cursor.close()
    except sqlite3.Error as error:
        print("Failed to fetch data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return int(modules[0])

def fetchModules():
    modules = ''
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
print(fetchModules(), 'sss')
def fetchAnswer(question):
    modules = ''
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
        cursor = sqliteConnection.cursor()
        print("Succesfully connected to SQLite")

        sqlite_insert_query = "SELECT answer from Questions " \
                              "where quest_name = '" + question + "'"
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        modules = count.fetchall()
        modules = [x[0] for x in modules]

        cursor.close()
    except sqlite3.Error as error:
        print("Failed to fetch data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return modules

def fetchPossibleAnswers(question, isMCQ= False):
    modules = ''
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
        cursor = sqliteConnection.cursor()
        print("Succesfully connected to SQLite")

        sqlite_insert_query = "SELECT possible_answers from Questions " \
                              "where quest_name = '" + str(question) + "'"
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        modules = count.fetchall()
        modules = [x[0] for x in modules]

        cursor.close()
    except sqlite3.Error as error:
        print("Failed to fetch data", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
 
    return modules[0].split(',') if isMCQ else modules 
def fetch_all_quest(curr_mod_name):
    m_id = findModId(curr_mod_name)
    questions = []
    modules = ''
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
        cursor = sqliteConnection.cursor()
        print("Succesfully connected to SQLite")

        sqlite_insert_query = "SELECT quest_name from Questions " \
                              "where mod_id = " + str(m_id)
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

    return modules


def get_fathers_from_children(answers):
    fathers = []

    for i in range(len(answers)):
        try:
            sqliteConnection = sqlite3.connect('./question_bank.db')
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
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
        sqliteConnection = sqlite3.connect('./question_bank.db')
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


def get_father_from_child(child):
    c = ''
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
        cursor = sqliteConnection.cursor()
        print("Succesfully connected to SQLite")

        sqlite_insert_query = "SELECT bma_father from BestMatchAns " \
                              "where bma_child = " + "'" + child + "'"
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        result = count.fetchone()[0]
        c = result
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to select father from child ", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return c


def find_quest_mark(quest_id):
    result = ''
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
        sqliteConnection = sqlite3.connect('./question_bank.db')
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


def add_ans_to_bma(q_id, father, child, m_id):
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
        cursor = sqliteConnection.cursor()
        print("Succesfully connected to SQLite")

        sqlite_insert_query = "INSERT INTO BestMatchAns (" \
                              "quest_id, bma_father, bma_child, mod_id) " \
                              "Values ('" + str(q_id) + "', '" + father + \
                              "', '" + child + "', '" + str(m_id) + "')"

        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed add ans to bma ", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return


def del_bma_rows(q_id):
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
        cursor = sqliteConnection.cursor()
        print("Succesfully connected to SQLite")

        sqlite_insert_query = "Delete from BestMatchAns where " \
                              "quest_id = " + str(q_id)
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to fetch all answers from question ", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return


def update_quest(quest_id, column, new_answer):
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
        cursor = sqliteConnection.cursor()
        print("Succesfully connected to SQLite")

        sqlite_insert_query = "Update Questions " \
                              "Set " + column + " = '" + new_answer + "' " \
                                                                      "Where quest_id = '" + str(quest_id) + "'"
        count = cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        cursor.close()
    except sqlite3.Error as error:
        print("Failed to update answers in question ", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
    return


def del_feed_quest_from_db(q_id):
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
    return


def del_bma_quest_from_db(q_id):
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
    return


def del_quest_execute(q_id):
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
    return


def find_quest_type(quest_name):
    result = ''
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
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


def update_mod_name_in_db(curr_name, desired_name):
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
    return


def add_feed_to_DB(q_id, name, text, m_id):
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
    return


def add_mod(mod_name):
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
    return


def add_quest(quest_name, quest_mod_id, possible_answers, answer, mark, quest_type):
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
    return


def add_bma_ans(quest_id, father, child, mod_id):
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
    return


def update_bms_db_poss_ans(children, q_id):
    c = ",".join(children)

    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
    return


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
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
    return


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
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
    return


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
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
    return


def delModFromDB(moduleName):
    try:
        sqliteConnection = sqlite3.connect('./question_bank.db')
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
    return
