import glob
import os

images = open("images.txt", "w+")

for imgFile in glob.glob("*.png"):
	images.write("%s\n" % imgFile)
	print("%s\n" % imgFile)
	
images.close()