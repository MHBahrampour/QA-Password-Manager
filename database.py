import sqlite3

# create connection and cursor to the database
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# make a table for the user
def add_user_table(the_username):

    cursor.execute('''CREATE TABLE {0} (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        question TEXT NOT NULL, 
        answer TEXT NOT NULL)'''.format(the_username))
    print(":: Your account created seccessfuly.")

def insert_question_answer(the_username, question, answer):
    cursor.execute("INSERT INTO {0} (question, answer) VALUES ('{1}', '{2}')".format(the_username, question, answer))

def user_verification(the_username):
    cursor.execute("SELECT question, answer FROM {0}".format(the_username))
    user_qa_database = cursor.fetchall()
    print(":: Answer these questions to verification your username: ")
    
    i = 0
    j = 0
    for rows in user_qa_database:
        i = i + 1
        print(":: Question #{0}".format(i) + '\t' + rows[0])
        the_answer = input(":: Tell me the answer: ")
        if the_answer == rows[1]:
            j = j + 1
            print(":: Answer is correct")
        else:
            print(":: Answer is not correct")
            break
        
    if i == j:
        print(":: User verification was seccsessful.")
        return 1
    else:
        print(":: User verification was not seccsessful.")
        return 0
    

        

        

# Save (commit) the changes
def commit_changes():
    connection.commit()


# Close the connection
#connection.close()