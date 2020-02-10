import sys
import subprocess
import os
import platform
import time


def main():
	succesfull = 0

	print("> OS: Windows ")
	print("> Verying pip module exists..")
	cmd_output = (subprocess.check_output(["pip", "--version"]))
	if(cmd_output == succesfull):
		print("> pip is already installed..")
	else:
		print("> Installing pip..")
		
	print("> Installing serial module.." )
	subprocess.check_output([sys.executable, "-m", "pip", "install", "serial"])
	print("> Installing numpy module..")
	subprocess.check_output([sys.executable, "-m", "pip", "install", "numpy"])
	print("> Installing pygame module..")
	subprocess.check_output([sys.executable, "-m", "pip", "install", "pygame"])
	print("> Installed all the required python modules..")
		
	time.sleep(5)


if __name__ == "__main__": main()