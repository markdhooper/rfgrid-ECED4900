import sys
import subprocess
import os
import platform
import time

succesfull = 0


#Determine host OS

current_os = platform.system()

def windows():
	cmd_output = (subprocess.check_call(["pip", "--version"]))
	if(cmd_output == succesfull):
		print("> pip is already installed..")
		if((subprocess.check_call([sys.executable, "-m", "pip", "install", "serial"]) != succesfull)):
			print("> Could not install serial module..")	
	
		elif((subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy"]) != succesfull)):
			print("> Could not install numpy module..")
		elif((subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"]) != succesfull)):
			print("> Could not install pygame module..")
		print("> Installed all the required python modules..")
	else:
		print("> pip module is missing")

        


	
	time.sleep(5)

def macos():
	print("gonna merge later")



def linux():
    print("OS: Linux " + "\U0001F4BB")

available_os = {
    "Windows": windows,
    "Darwin" : macos,
    "linux" : linux
}

available_os[current_os]()

