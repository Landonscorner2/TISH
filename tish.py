from cmd import Cmd
import os

# Function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the version.
def version():
    print("Version 0.1") # This is the version of the shell.

class MyCmd(Cmd): # Here we define the class that will handle the shell commands.
    clear()
    prompt = ':'
    intro = "Welcome to The Intimidation Shell! \nType help or ? to list commands.\n"
    
    def do_x(self, arg): # This exits the shell, similar to Ctrl+D or Ctrl+C. 
        try:
            print("Exiting...")
            return True
        except (KeyboardInterrupt, EOFError): # This handles the Ctrl+C and Ctrl+D exceptions.
            print("\nExiting...")
            return True

    def do_help(self, arg): # PLEASE FUCKING HELP ME !
        if arg:
            print(f"Help on command '{arg}':")
        else:
            print("""
            Available commands:
            x       - Exit the shell
            c       - Clear the screen
            help    - Show this help message
            f       - List files in the current directory
            d       - Change directory
            w       - Print the current working directory
            abt     - About the shell
            m       - Make a directory
            r       - Remove a directory      
            """)

    def do_c(self, arg): # Again, hides the evidence of the body.
        clear()

    def do_EOF(self, arg): # Same as 'X' or Ctrl+C. Prevents a unholy error mess.
        print("\nExiting...")
        return True
    
    def do_f(self, arg): # Gotta list 'em all.
        try:
            if not arg:
                for f in os.listdir(): # List all files in the current directory.
                    print(f)
            else:
                for f in os.listdir(arg): # List all files in the specified directory.
                    print(f) 
        except (FileNotFoundError, ValueError) as fer:
            print(f"Error: {fer}")  

    def do_d(self, arg): # This is the command to change directories. It will take an argument and change the current working directory to that argument.

        if not arg:
            print("Error: No directory specified.") # If no argument is provided, print an error message.
            return
        
        try:
            if os.path.isdir(arg): # Check if the argument is a valid directory.
                os.chdir(arg)
                print(f"Changed directory to {arg}")
            else:
                print(f"Error: '{arg}' is not a valid directory.") # If the argument is not a valid directory, print an error message.
        except (FileNotFoundError, PermissionError) as er:
            print(f"Error: {er}")

    def do_w(self, arg): # This is the command to print the current working directory.
        print(f"Current directory: {os.getcwd()}")

    def do_abt(self, arg): 
        print("TISH is under the GNU GPL v3 license.") # This is the command to print the license information.
        print("It is free software: you can redistribute it and comes with no warranty.\n")
        print("The Intimidation Shell is a simple shell written in Python.")
        print("Created with passion by Landon Brooks <3")

    def do_m(self, arg): # Makes a directory.
        try:
            if not arg:
                print("Error: No argument provided.")
            else:
                os.mkdir(arg)
                print(f"Directory '{arg}' created.")
        except (FileNotFoundError, PermissionError, FileExistsError, OSError) as mer:
            print(f"Error: {mer}")

    def do_r(self, arg): # Removes a directory.
        try:
            if not arg:
                print("Error: No argument provided.")
            else:
                os.rmdir(arg)
                print(f"Directory '{arg}' removed.")
        except (FileNotFoundError, PermissionError, OSError) as rer:
            print(f"Error: {rer}")

    def emptyline(self):
        print("Error: Nothing was inputted.") # This is the method that will be called if an empty line is entered.


    def default(self, line): # This is the default command handler. It will be called if no other command matches.
        print(f"Command not found: {line}")
        

if __name__ == '__main__': # This is the main function. It will be called when the script is run.
    try:
        MyCmd().cmdloop()
    except KeyboardInterrupt:
        print("\nExiting...")