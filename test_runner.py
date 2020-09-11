import os
import platform


def get_test_files():
    test_file_names = []
    for file in os.listdir("tests"):
        if file.endswith('.sajilo'):
            if platform.system() == "Windows":
                test_file_names.append("tests\\"+str(file))
            else:
                test_file_names.append("tests/" + str(file))

    return test_file_names


def mac_commands(python_version):
    commands = []
    for test_file_name in get_test_files():
        command = python_version + " sajiloc.py " + test_file_name
        commands.append(command)
    return commands


# Assuming that only I have two versions of python
if platform.system() == "Darwin:":
    py = "python3"
else:
    py = "python"


for term_c in mac_commands(py):
    os.system(term_c)
