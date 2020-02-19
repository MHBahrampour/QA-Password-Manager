import sqlite3

# create connection for datsabase
connection = sqlite3.connect('database.db')

# create cursor to datsabase
cursor = connection.cursor()

# create QAs table for user
def add_user_table(username):

    # create the name of table
    table_name = username
    cursor.execute('''CREATE TABLE IF NOT EXISTS {0} (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        question TEXT NOT NULL, 
        answer TEXT NOT NULL)'''.format(table_name))
    print(":: Your account created seccessfuly.")

# create password table for user
def add_pass_table(username):

    # create the name of table
    table_name = (username + "_Pass")
    cursor.execute('''CREATE TABLE IF NOT EXISTS {0} (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT NOT NULL, 
        password TEXT NOT NULL)'''.format(table_name))

    print(":: Your pass table created seccessfuly.")

# insert QAs to user QAs table
def insert_QA(username, question, answer):
    # insert the QA to database
    cursor.execute("INSERT INTO {0} (question, answer) VALUES ('{1}', '{2}')".format(username, question, answer))

# verify user access
def user_verification(username):

    # select all QAs of user
    cursor.execute("SELECT question, answer FROM {0}".format(username))

    # fetch data
    # this will be something like this:
    # [ ('Question_1', 'Answer_1'), ('Question_2', 'Answer_2'), ... ]
    user_QAs = cursor.fetchall()

    print(":: Answer these questions to verification yourself: ")
    
    # these variables check nubmer of all Questions and all correct Answers to verify user
    number_of_all_Questions = 0
    number_of_correct_Answers = 0

    # a for loop to show and ask the answer of questions
    for rows in user_QAs:

        # increase number_of_all_Questions
        number_of_all_Questions = number_of_all_Questions + 1

        # show the Question
        print("\n  :: Question #{0}".format(number_of_all_Questions) + ' : ' + rows[0])

        # get the Answer
        the_answer = input("  :: Tell me the answer: ")

        # check the input answer with the TRUE answer (if it was correct)
        if the_answer == rows[1]:

            # increase number_of_correct_Answers
            number_of_correct_Answers = number_of_correct_Answers + 1

            print("  :: Answer is correct")

        # if input answer was not TRUE
        else:
            print("  :: Answer is not correct")
            break
        
    # return 1 if user verification was seccsessful
    if number_of_all_Questions == number_of_correct_Answers:
        print("\n:: User verification was seccsessful.")
        return 1

    # return 0 if user verification was NOT seccsessful
    else:
        print("\n:: User verification was not seccsessful.")
        return 0

# insert passwords to user pass table
def add_password(username, pass_title, password):
    
    # create the name of table
    table_name = (username + "_Pass")

    # insert a new password
    cursor.execute("INSERT INTO {0} (title, password) VALUES ('{1}', '{2}')".format(table_name, pass_title, password))

    print(":: Your password added seccessfuly.")

# Save (commit) the changes
def commit_changes():
    connection.commit()

# Close the connection
#connection.close()