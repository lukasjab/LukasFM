# LukasFM, a simple yet uniquely terrible file manager written in python.

import os

workingDirectory = r"/home/" + os.getlogin()

print("Welcome to LukasFM, a simple yet uniquely terrible file manager written in python.")
while True:
    print("Current working directory: " + workingDirectory)
    print("Type 'help' for a list of commands.")
    command = input("Enter a command: ")
    if command == "help":
        print("cd <directory> - Change the current working directory.")
        print("ls - List the contents of the current working directory.")
        print("mkdir <directory> - Create a new directory in the current working directory.")
        print("rmdir <directory> - Remove a directory from the current working directory.")
        print("touch <file> - Create a new file in the current working directory.")
        print("rm <file> - Remove a file from the current working directory.")
        print("exit - Exit LukasFM.")
    elif command == "ls":
        print("Contents of " + workingDirectory + ":")
        for item in os.listdir(workingDirectory):
            print(item)
    elif command[0:3] == "cd ":
        if os.path.isdir(workingDirectory + "/" + command[3:]):
            workingDirectory = workingDirectory + "/" + command[3:]
        else:
            print("Directory not found.")
    elif command[0:6] == "mkdir ":
        os.mkdir(workingDirectory + "/" + command[6:])
    elif command[0:6] == "rmdir ":
        os.rmdir(workingDirectory + "/" + command[6:])
    elif command[0:6] == "touch ":
        open(workingDirectory + "/" + command[6:], "w").close()
    elif command[0:3] == "rm ":
        os.remove(workingDirectory + "/" + command[3:])
    elif command == "exit":
        break
    else:
        print("Invalid command.")