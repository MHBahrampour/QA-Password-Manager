import sqlite3

# create connection and cursor to the database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# make a table for the user
def add_user_table(username):

    cursor.execute('''CREATE TABLE {0} (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        question TEXT NOT NULL, 
        answer TEXT NOT NULL)'''.format(username))
    print(":: Your account created seccessfuly.")

def insert_question_answer(question, answer):
    curent_user = "bpmmd"
    cursor.execute("INSERT INTO {0} (question, answer) VALUES ('{1}', '{2}')".format(curent_user, question, answer))

# Save (commit) the changes
def commit_changes():
    connection.commit()
    connection.close()


# Close the connection
#connection.close()