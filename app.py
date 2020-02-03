# import libraries and module
import functions

def user_verify():
    the_username = ""
    # get the verification code
    user_verify = functions.login_page(the_username)
    # enter to the app
    if user_verify == 1:
        # while loop for getting user commands
        while True:
            user_input = input( "\n?? " )
            functions.user_command(user_input)
    # close the app
    if user_verify == 0:
        print(":: App closed.")
        exit()


# the main script
def main():
    
    # show the help page
    print( functions.help_page() )

    user_verify()

if __name__ == "__main__":
    main()