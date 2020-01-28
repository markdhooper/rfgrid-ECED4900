from rfgrid import *
import numpy

rfgrid = rfgridInit()
rfgrid.updateMenu("Added tag state management Jan 28, 2020",30,(0,0,0),(100,100,100))
done = False

import serial

# set up serial port and variables for communication
CMD_UPDATE = b'\x00'
#serPort = serial.Serial(port = "COM3", baudrate = 9600, timeout = 1)
#serPort.flushOutput() 
#serPort.flushInput() 
ID = 0
x = 0
y = 0


while not done:
	# if (serPort.inWaiting() > 0):
	# 	if serPort.read(1) == CMD_UPDATE:
	# 		ID = int.from_bytes(serPort.read(4), byteorder = 'big', signed = 0)
	# 		x  = int.from_bytes(serPort.read(1), byteorder = 'big', signed = 0)
	# 		y  = int.from_bytes(serPort.read(1), byteorder = 'big', signed = 0)
	# 		if ID != 0:
	# 			image = pygame.transform.smoothscale(pygame.image.load(tags[str(ID)]),(rfgrid.grid_x_step,rfgrid.grid_y_step))
	# 			rfgrid.drawGrid(x,y,image)
	# 		else:
	# 			blankRect = pygame.Surface((rfgrid.grid_x_step,rfgrid.grid_y_step))
	# 			blankRect.blit(rfgrid.bg_surf, (rfgrid.bg_ofs_x + x*rfgrid.grid_x_step,rfgrid.bg_ofs_y+ y*rfgrid.grid_y_step))
	# 			print(rfgrid.grid_x_step*x + rfgrid.bg_ofs_x)
	# 			print(rfgrid.grid_y_step*y - rfgrid.bg_ofs_y)
	# 			print(rfgrid.grid_x_step + rfgrid.grid_x_step*x + rfgrid.bg_ofs_x)
	# 			print(rfgrid.grid_y_step + rfgrid.grid_y_step*y - rfgrid.bg_ofs_y)
	# 			rfgrid.drawGrid(x,y,blankRect)


	for event in pygame.event.get():
		# IF USER CLOSES THE WINDOW
		if event.type == pygame.QUIT:
			done=True
		
		# ESCAPE KEYPRESS
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			done=True

		# ARROW KEYPRESSES
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			rfgrid.scrollBackground(-1,0)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			rfgrid.scrollBackground(+1,0)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			rfgrid.scrollBackground(0,+1)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			rfgrid.scrollBackground(0,-1)

		# Pressing a will simulate a random tag event, at a random x,y coordinate
		if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
			x = int(numpy.random.randint(0,8))
			y = int(numpy.random.randint(0,8))
			id = rfgrid.tags[numpy.random.randint(0,rfgrid.tag_count)][0]
			# tag search will return a valid index if the ID sent is
			# within the tags.rfgridtag file
			index = tagSearch(rfgrid.tags,id)
			if index != -1:
				rfgrid.updateGridTiles(x,y,index)
				rfgrid.draw()
	
	clock.tick(30)
pygame.quit()