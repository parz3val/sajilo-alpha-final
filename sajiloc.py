import sajilo
import sys
import os.path

if len(sys.argv) == 1:
    #ask for the file if no file is provided
    print("Usage: %s filename" % __file__)
else:
    #get the file extension if file is provided.
    ext = str(os.path.splitext(sys.argv[1])[1])
    if ext == ".sajilo":
        #execute the file if extension matches
        with open(sys.argv[1]) as f:
            sajilo.execute(f.read())
    else:
        print("Sajilo Compiler only supports .sajilo files!")

