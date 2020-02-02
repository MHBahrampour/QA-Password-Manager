# import libraries and module
import functions

# the main script
def main():
    the_username = ""

    # show the help page
    print( functions.help_page() )

    # Check entry method
    user_verify = functions.login_page(the_username)
    
    if user_verify == 1:
        # while loop for getting user commands
        while True:
            user_input = input( "\n?? " )
            functions.user_command(user_input)
    
    if user_verify == 0:
        print(":: App closed.")
        exit()

if __name__ == "__main__":
    main()