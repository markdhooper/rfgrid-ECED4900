from rfgrid import *
from rfgridCommunication import *
from time import sleep
import numpy

rfgrid = rfgridInit()
rfgrid.updateMenu("Initializing Grid:\nPlease Wait...",40,(0,0,0),(255,255,255))
rfgridSerial = rfgridCommInit(rfgrid.grid_x_tiles, rfgrid.grid_y_tiles)
done = False

while not done:
	if (rfgridSerial.inWaiting() > 0):
		# there is data in the serial buffer
		# extract the command byte, and the arguments from the buffer
		cmdIdx, args = rx_rfgrid(rfgridSerial)
		RX_LUT[RX_LUT_KEYS[cmdIdx]](args,rfgrid)
		rfgrid.updateMenu("rfgrid - chess",60,(0,0,0),(255,255,255))

	for event in pygame.event.get():
		# IF USER CLOSES THE WINDOW
		if event.type == pygame.QUIT:
			done=True
		
		# ESCAPE KEYPRESS
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			done=True

		# ARROW KEYPRESSES
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			rfgrid.scrollBackground(-1,0,smooth = False)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			rfgrid.scrollBackground(+1,0,smooth = False)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			rfgrid.scrollBackground(0,+1,smooth = False)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			rfgrid.scrollBackground(0,-1, smooth = False)

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
				if(rfgrid.tags[index][0]):
					rfgrid.draw()
				rfgrid.playTagSound(index)
				if rfgrid.tags[index][1]:
					if(x == 0):
						# object detected on left Edge
						rfgrid.scrollBackground(+2,0,smooth = True)
					if(x == 7):
						# object detected on right edge
						rfgrid.scrollBackground(-2,0,smooth = True)
					if(y == 0):
						# object detected on top edge
						rfgrid.scrollBackground(0,+2,smooth = True)
					if(y == 7):
						# object detected on bottom edge
						rfgrid.scrollBackground(0,-2,smooth = True)
	
	clock.tick(20)
pygame.quit()