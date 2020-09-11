import sajilo
import sys
import os.path


# Infinite loop console func
def console():
    while True:
        text = input(""
                     "Sajilo Shell>> \n$")
        if text == "exit();" or text == "anta();":
            print("\n")
            print("\nUsage with file sajilo filename\nSajilo Compiler prayog garda 'sajiloc filname' use garnu hola")
            exit()
        # If the command is not exit()
        sajilo.shell(text)


# If no file is provided switch to the REPL mode.
if len(sys.argv) == 1:
    console()
else:
    # Get the file extension if file is provided.
    ext = str(os.path.splitext(sys.argv[1])[1])
    if ext == ".sajilo":
        # Execute the file if extension matches
        with open(sys.argv[1]) as f:
            sajilo.execute(f.read())
    else:
        print("Sajilo Compiler only supports .sajilo files!")

