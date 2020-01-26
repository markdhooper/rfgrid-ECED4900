import sys
import subprocess
import os
import platform



#Determine host OS

current_os = platform.system()


def windows():
    print( "\U000025B6"+"You are running on Windows!" + "\U0001F4BB")

def macos():
    print( "\U000025B6 "+"You are running on MacOS.." + "\U0001F4BB" )
    print("\U000025B6 "+"Verying pip module exists.. " + "\U0001F504")
    cmd_output = (subprocess.check_output(["pip", "--version"]))
    result = (cmd_output.decode("utf-8")).find("command not found")
    if(result == -1):
        print("\U000025B6 "+"pip is already installed.. " + "\U00002705")
    else:

        print("Installing pip..")

    print("\U000025B6 "+ "Installing serial module.." + "\U000023F3")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "serial"])
    print("\U000025B6 "+"Installing numpy module.." + "\U000023F3")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"])
    print("\U000025B6 "+ "Installing pygame module.." + "\U000023F3")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])

    print("\U000025B6 "+ "Installed all the required python modules.."+ "\U00002705")


def linux():
    print("You are running on linux" + "\U0001F4BB")

available_os = {
    "Windows": windows,
    "Darwin" : macos,
    "linux" : linux
}

available_os[current_os]()

