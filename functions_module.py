import database

# these content give some important options to use this app
def help_page():
    help_page = """
    ---------------------------------
    Wellcome to QA Password Manager !

    You are using VERSION 1.0
    To see the user manual type 'man'
    To close the app type '0'

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

def login_page():
    
    print(":: You had two option to using app: ")
    input_method = input(":: 1. Sign-up or 2. Sign-in ? [1/2] ")
    return input_method

# create user table
def sign_up():

    # get username
    username = input("\n:: Enter your username: ")

    # create username (table)
    database.add_user(username)

    return username

# sign-in to app
def sign_in():

    # get username
    username = input("\n:: Enter your username: ")
    verification = database.user_verification(username)
    return verification

# add Questions and Answers
def add_QA(username):
    
    # get QAs
    while True:
        # ask QAs
        question = input("\n:: Enter the Qustion: ")
        answer = input(":: Enter the Answer: ")

        # send the QA to database
        database.insert_QA(username, question, answer)
        
        # stay or leave?
        continue_confirmation = input("\n:: Do you want to add another pattern? [y/N] ")

        # if user want to leave
        if continue_confirmation == 'N' or continue_confirmation == 'n' or continue_confirmation == '':
            print("\n:: Congratulate, you added some pattern.")
            commit_confirmation()
            break

        # if user want to stay
        if continue_confirmation == 'y':
            continue

def commit_confirmation():

    commit_confirmation = input(":: Do you want to save changes? [Y/n]")

    if commit_confirmation == 'Y' or commit_confirmation == 'y' or commit_confirmation == '':
        database.commit_changes()
        print(":: Changes seccessfuly saved.")
    
    elif commit_confirmation == 'n' or commit_confirmation == 'N':
        print(":: Changes not saved.")

    else:
        print(":: Your option is unvalid, Enter 'y' or 'n'. ")
        commit_confirmation() 

# do what the user want
def user_command(user_input):

    # close the app
    if user_input == "0":
        return exit_door()

    # add new password
    if user_input == "1":
        new_password(username)

    #if user_input == "":

    
    # if user command wasn't exist
    else:
        print(":: Command not found!")
        print(":: To see commands type 'man' and read the manual.")