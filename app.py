# import libraries and module
import functions

# the main script
def main():
    
    # show the help page
    print( functions.help_page() )

    # while loop for getting user commands
    while True:
        user_input = input( "\n?? " )
        functions.user_command( user_input )

if __name__ == "__main__":
    main()