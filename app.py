# import libraries and module
import functions

# the main script
def main():
    
    # show the help page
    print( functions.help_page() )

    # login_page
    input_method = functions.login_page()

    verification = 'Null'
    
    # sign-up
    if input_method == '1':

        # get the username, create table, return username
        username = functions.sign_up()

        # add Questuions and Answers
        functions.add_QA(username)

        # get the username, pass to user_verification function
        verification = functions.sign_in()

    # sign-in
    elif input_method == '2':

        # get the username, pass to user_verification function
        verification = functions.sign_in()

    else:
        print(":: There is not such method !")

    # seccsessful verification
    if verification == 1:

        # a loop of user commands
        while True:
            user_input = input( "\n?? " )
            functions.user_command(user_input)

    # unseccsessful verification
    if verification == 0:

        # get out
        print(":: App closed.")
        exit()

# run the main function
if __name__ == "__main__":
    main()