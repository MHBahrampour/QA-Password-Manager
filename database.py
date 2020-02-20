import sqlite3

# create connection for datsabase
connection = sqlite3.connect('database.db')

# create cursor to datsabase
cursor = connection.cursor()

# create QAs table for user
def add_user_table(username):

    # create the name of table
    table_name = username

    # create user table
    cursor.execute('''CREATE TABLE IF NOT EXISTS {0} (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        question TEXT NOT NULL, 
        answer TEXT NOT NULL)'''.format(table_name))

    print(":: Your account created seccessfuly.")

def insert_QA(username, question, answer):
    # insert the QA to database
    cursor.execute("INSERT INTO {0} (question, answer) VALUES ('{1}', '{2}')".format(username, question, answer))

def add_pass_table(username):

    # create the name of table
    table_name = (username + "_Pass")

    # create user pass table
    cursor.execute('''CREATE TABLE IF NOT EXISTS {0} (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        title TEXT NOT NULL, 
        description TEXT,
        password TEXT NOT NULL)'''.format(table_name))

    print(":: Your pass table created seccessfuly.")

def insert_password(username, pass_title, description, password):
    
    # create the name of table
    table_name = (username + "_Pass")

    # insert a new password
    cursor.execute("INSERT INTO {0} (title, description, password) VALUES ('{1}', '{2}', '{3}')".format(table_name, pass_title, description, password))

    print(":: Your password added seccessfuly.")

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

# show all password titles of the user
def show_pass_titles(username):

    # create the name of table
    table_name = username + "_Pass"

    # select id and title column
    cursor.execute("SELECT id, title, description FROM {0}".format(table_name))

    # fetchall these data
    pass_title = cursor.fetchall()

    # ptint headers
    print("   ID\tTitle\tDescription")

    # print these data
    for rows in pass_title:
        print("   {0}\t{1}\t{2}".format(rows[0], rows[1], rows[2]))

# show password
def show_password(username, row_number):

    # create the name of table
    table_name = (username + "_Pass")

    # select title and password column of the row
    cursor.execute("SELECT title, password FROM {0} WHERE id = {1}".format(table_name, row_number))

    # fetchall these data
    password = cursor.fetchall()

    # ptint headers
    print("\n   Title\tPassword")

    # print these data
    print("   {0}\t{1}".format(rows[0], rows[1]))

# remove password
def delete_password(username, row_number):

    # create the name of table
    table_name = (username + "_Pass")

    # select row to delete
    cursor.execute("DELETE FROM {0} WHERE id = {1}".format(table_name, row_number))

    print("\n:: Password deleted.")

# edit password
def edit_password(username, row_number, new_title, new_description, new_password):

    # create the name of table
    table_name = (username + "_Pass")

    # get current field context
    cursor.execute("SELECT title, description, password FROM {0} WHERE id = {1}".format(table_name, row_number))

    # fetchall these data
    row = cursor.fetchall()

    # save current field context
    current_title = row[0]
    current_description = row[1]
    current_password = row[2]

    # don't change these if user want
    if new_title == "":
        new_title = current_title
    if new_description == "":
        new_description = current_description
    if new_password == "":
        new_password = current_password

    # change fields with new contexts
    

# Save (commit) the changes
def commit_changes():
    connection.commit()

# Close the connection
#connection.close()