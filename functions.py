import database

# these content give some important options to use this app
def help_page():
    help_page = """
    ---------------------------------
    Wellcome to QA Password Manager !

    You are using VERSION 1.0
    To see the user manual type 'man'
    To get out of the app type 'exit'

    Introduce some sign:
    :: -> App questions or message.
    !! -> Warning message.
    ?? -> You can type what you want.
    ---------------------------------
    """
    return help_page

# exit door for app
def exit_door():

    # warning message
    print("!! Make sure you saved changes,")
    print("   otherwise the changes will be ignored.")

    while True:
        # asking user decision
        exit_confirmation = input(":: Do you really want EXIT? [Y/n] ")

        # exit operation (exit)
        if exit_confirmation == "Y" or exit_confirmation == 'y' or exit_confirmation == '':
            print(":: App closed.")
            exit()

        # exit operation (stay)
        if exit_confirmation == "n":
            print(":: Exit operation stopped.")
            break

        else:
            print(":: ERROR: You entered wrong option!")

def login_page(the_username):
    
    print(":: You had two option to using app: ")
    log = input(":: 1. Sign-up and 2. Log-in ? [1/2] ")

    # sign-up in app
    if log == '1':
        # create username (table) account
        the_username = add_user(the_username)
        # ask about questions and answers for log-in
        add_question_answer(the_username)
        print(":: Congratulation, you signed-up seccessfuly.\n")

        # log-in to app
        print(":: Answer these Questions to log-in: ")
        # ask username
        the_username = input(":: Enter username: ")
        # ask the user questions and return verification
        return database.user_verification(the_username)

    # log-in to app
    if log == '2':
        # ask username
        the_username = input(":: Enter username: ")
        return database.user_verification(the_username)

# add table for the user
def add_user(the_username):
    # ask username
    the_username = input(":: Enter username: ")

    # send username to make a table 
    database.add_user_table(the_username)

    return the_username

def commit_confirmation():

    commit_confirmation = input(":: Do you want to save changes? [Y/n]")

    if commit_confirmation == 'Y' or commit_confirmation == 'y' or commit_confirmation == '':
        database.commit_changes()
        print(":: Changes seccessfuly saved.")
    
    if commit_confirmation == 'n' or commit_confirmation == 'N':
        print(":: Changes not saved.")

def add_question_answer(the_username):
    
    while True:
        # ask the question
        question = input(":: Enter the qustion: ")
        answer = input(":: Enter the answer: ")

        database.insert_question_answer(the_username, question, answer)

        continue_confirmation = input(":: Do you want to add another Qusetion and answer? [y/N] ")

        if continue_confirmation == 'N' or continue_confirmation == 'n' or continue_confirmation == '':
            print(":: Congratulate, you added some Question and Answer.")
            commit_confirmation()
            break

        if continue_confirmation == 'y':
            continue

# do what the user want
def user_command(user_input):

    if user_input == "exit":
        return exit_door()

    if user_input == "addu":
        add_user()

    if user_input == "addqa":
        add_question_answer(the_username)

    
    # if user command wasn't exist
    else:
        print(":: Command not found!")
        print(":: To see commands type 'man' and read the manual.")





