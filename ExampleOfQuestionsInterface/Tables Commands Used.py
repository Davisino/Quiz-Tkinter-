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
