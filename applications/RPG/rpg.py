from rfgrid import *
from rfgridCommunication import *
from time import sleep

rfgrid = rfgridInit()
rfgrid.updateMenu("Initializing Grid:\nPlease Wait...",40,(0,0,0),(255,255,255))
rfgridSerial = rfgridCommInit(rfgrid.grid_x_tiles, rfgrid.grid_y_tiles)
done = False
numPlayers = 4
currentPlayer = 0
playerNames = ["Verrona","Udoghast","Lud","Rugren"]
id = 0
x = 0
y = 0

# THESE ARE SPECIFIC TO rpg.py
MUTE = 2302950640
END_TURN = 695941360
EXPLORE = 2311927792
SCROLL_OFF = 963853040 
SCROLL_ON = 2307276272
MENU_COLOR = (200,200,200)


while not done:
	if (rfgridSerial.inWaiting() > 0):
		# there is data in the serial buffer
		# extract the command byte, and the arguments from the buffer
		cmdIdx, args = rx_rfgrid(rfgridSerial)
		if cmdIdx == 7:
			rfgrid.updateMenu("rfgrid - rpg",60,(0,0,0),MENU_COLOR)
		if cmdIdx == 0:
			id, x, y = RX_LUT[RX_LUT_KEYS[cmdIdx]](args,rfgrid)
			
			# Mute all audio 
			if id == MUTE:
				pygame.mixer.fadeout(5000)
				
			# End the current turn and locate 
			elif id == END_TURN:
				if currentPlayer == numPlayers:
					rfgrid.updateMenu("Dungeon Master's Turn",40,(0,0,0),MENU_COLOR)
					currentPlayer = 0
				else:
					# inform the player that it's their turn
					msg = ("%s's Turn:" % (playerNames[currentPlayer]))
					rfgrid.updateMenu(msg,40,(0,0,0),MENU_COLOR)
					# attempt to pan the map to display that character
					rfgrid.moveCameraToTag(currentPlayer)
					currentPlayer += 1
					
			# Enable background scrolling for tags with renderable images
			elif id == SCROLL_ON:
				rfgrid.scroll_enabled = True
				MENU_COLOR = (200,200,200)
				msg = "\n Character Scrolling ENABLED"
				rfgrid.updateMenu(msg,30,(0,0,0),MENU_COLOR)
			
			# Disable background scrolling for tags with renderable images
			elif id == SCROLL_OFF:
				rfgrid.scroll_enabled = False
				MENU_COLOR = (200,100,100)
				msg = "\n Character Scrolling DISABLED"
				rfgrid.updateMenu(msg,30,(255,0,0),MENU_COLOR)
			
			elif id == EXPLORE:
				step_size = 0
				x_dir = 0
				y_dir = 0
				
				# x cases
				if(x == 0):
					step_size = 7
					x_dir = 1
				elif(x == 1):
					step_size = 2
					x_dir = 1
				elif(x == 7):
					step_size = 7
					x_dir = -1
				elif(x == 6):
					step_size = 2
					x_dir = -1
				
				# y cases
				if(y == 0):
					step_size = 7
					y_dir = 1
				elif(y == 1):
					step_size = 2
					y_dir = 1
				elif(y == 7):
					step_size = 7
					y_dir = -1
				elif(y == 6):
					step_size = 2
					y_dir = -1
						
				for i in range(0,step_size):
					rfgrid.scrollBackground(x_dir,y_dir,smooth = True, speed = 20)
		else:
			RX_LUT[RX_LUT_KEYS[cmdIdx]](args,rfgrid)

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
	
	clock.tick(20)
pygame.quit()