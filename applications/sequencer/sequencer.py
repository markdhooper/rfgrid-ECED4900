from rfgrid import *
from rfgridCommunication import *
from time import sleep
import numpy

rfgrid = rfgridInit()
rfgrid.updateMenu("Initializing Grid:\nPlease Wait...",40,(0,0,0),(255,255,255))
rfgridSerial = rfgridCommInit(rfgrid.grid_x_tiles, rfgrid.grid_y_tiles)
done = False

# sequencer parameters
bpm_idx = 2
bpm_clk = 0
bpm_alarm = [500,187,150,125]#for 60,80,100,120 bpm, how many miliseconds need to elapse.
beat = 0
vol_index = 3
master_vol = float((vol_index+1)/8)
channel = 0

id = 0
x = 0
y = 0
update_flag = False

# S - Sample Tile (beat 1)
# s - Sample Tile (beat 2,3, or 4)
# g - green
# y - yellow
# r - red
# 6 - 60bpm
# 8 - 80bpm
# 0 - 100bpm
# 2 - 120bpm
# l - load
# p - play
# u - pause
# e - record

seq_zone_map = [
['S','s','s','s','S','s','s','s'],
['S','s','s','s','S','s','s','s'],
['S','s','s','s','S','s','s','s'],
['S','s','s','s','S','s','s','s'],
['S','s','s','s','S','s','s','s'],
['S','s','s','s','S','s','s','s'],
['g','g','g','g','g','y','y','r'],
['6','8','0','2','l','p','u','e']
]

seq_zone_dict = {
	'S':'./images/objects/b1.png',
	's':'./images/objects/b2.png',
	'g':'./images/objects/v1.png',
	'y':'./images/objects/v2.png',
	'r':'./images/objects/v3.png',
	'6':'./images/objects/bpm60.png',
	'8':'./images/objects/bpm80.png',
	'0':'./images/objects/bpm100.png',
	'2':'./images/objects/bpm120.png',
	'l':'./images/objects/load.png',
	'p':'./images/objects/play.png',
	'u':'./images/objects/pause.png',
	'e':'./images/objects/rec.png'
}

seq_state = [
	[True,	False,	False,	False,	False,	False,	False,	False],
	[True,	False,	False,	False,	False,	False,	False,	False],
	[True,	False,	False,	False,	False,	False,	False,	False],
	[True,	False,	False,	False,	False,	False,	False,	False],
	[True,	False,	False,	False,	False,	False,	False,	False],
	[True,	False,	False,	False,	False,	False,	False,	False],
	[True,	True,	True,	True,	False,	False,	False,	False],
	[False,	False,	True,	False,	False,	False,	True,	False]
]

seq_surface = [
	[None,	None,	None,	None,	None,	None,	None,	None],
	[None,	None,	None,	None,	None,	None,	None,	None],
	[None,	None,	None,	None,	None,	None,	None,	None],
	[None,	None,	None,	None,	None,	None,	None,	None],
	[None,	None,	None,	None,	None,	None,	None,	None],
	[None,	None,	None,	None,	None,	None,	None,	None],
	[None,	None,	None,	None,	None,	None,	None,	None],
	[None,	None,	None,	None,	None,	None,	None,	None]
]
for col in range(0,8):
	for row in range(0,8):
			surf = pygame.image.load(seq_zone_dict[seq_zone_map[col][row]])
			surf = pygame.transform.smoothscale(surf,(rfgrid.grid_x_step,rfgrid.grid_y_step))
			seq_surface[col][row] = surf

while not done:
	if (rfgridSerial.inWaiting() > 0):
		# there is data in the serial buffer
		# extract the command byte, and the arguments from the buffer
		cmdIdx, args = rx_rfgrid(rfgridSerial)
		if(cmdIdx == 0):
			# Update Message, special case for the sequencer
			id,x,y = RX_LUT[RX_LUT_KEYS[cmdIdx]](args,rfgrid)
			update_flag = True
		else:
			RX_LUT[RX_LUT_KEYS[cmdIdx]](args,rfgrid)
		rfgrid.updateMenu("rfgrid - sequencer",60,(0,0,0),(255,255,255))
	
	if update_flag:
		#we need to check to see at which x and y the update occurred
		# INSTRUMENT
		if(y < 6 and x < 8):
			#update occurred within the play area
			if(id == 0):
				#tag was removed, make sure that 
				#the image isn't drawn there anymore
				rfgrid.game_tiles[x,y] = -1
				channel -= 1
			else:
				#tag detected at (x,y)
				index = tagSearch(rfgrid.tags,id)
				if index != -1:
					rfgrid.updateGridTiles(x,y,index)
					channel += 1
					if seq_state[7][6]:
						#play the tag sound only if we are paused.
						rfgrid.playTagSound(index,master_vol,channel)
		
		# VOLUME
		elif (y == 6 and id != 0):
			#tag detected on volume slider
			vol_index = x
			master_vol = float((vol_index+1)/8)
			for i in range(0,8):
				# illuminate all volume icons <= the x coordinate
				if i <= x:
					seq_state[6][i]=True
				else:
					seq_state[6][i]=False
					
		# BPM
		elif (y == 7 and x < 4 and id != 0):
			#tag detected at the BPM section
			bpm_idx = x
			for i in range(0,4):
				#illuminate the corresponding BPM control
				if i == x:
					seq_state[7][i]=True
				else:
					seq_state[7][i]=False
		# LOAD
		elif (y == 7 and x == 4):
			if(id != 0):
				seq_state[7][4]=True
			else:
				seq_state[7][4]=False
		
		# PLAY
		elif (y == 7 and x == 5 and id != 0):
				seq_state[7][5]=True
				seq_state[7][6]=False
		
		# PAUSE
		elif (y == 7 and x == 6 and id != 0):
				seq_state[7][5]=False
				seq_state[7][6]=True
				
		# RECORD
		elif (y == 7 and x == 7):
			#tag detected at the BPM section
			if(id != 0):
				seq_state[7][7]=True
			else:
				seq_state[7][7]=False
		
		# draw the sequencer area and clear the update flag
		rfgrid.draw(True,seq_surface,seq_state)
		update_flag = False
	
	bpm_clk += clock.get_time()
	if(bpm_clk >= bpm_alarm[bpm_idx]):
		rfgrid.draw(True,seq_surface,seq_state)
		for row in range(0,6):
			if seq_state[7][5] and (rfgrid.game_tiles[beat,row] != -1):
				rfgrid.playTagSound(rfgrid.game_tiles[beat,row],master_vol,row+6*beat)
		if seq_state[7][5]:
			#Play is enabled
			for col in range(0,6):
				seq_state[col][beat]=False
				seq_state[col][(beat+1)%8]=True
			beat = (beat + 1)%8
		bpm_clk = 0
		
	for event in pygame.event.get():
		#b keypress to change the bpm
		if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
			seq_state[7][bpm_idx]=False
			bpm_idx = (bpm_idx + 1)%4
			seq_state[7][bpm_idx]=True
		
		#v keypress to change the volume
		if event.type == pygame.KEYDOWN and event.key == pygame.K_v:
			vol_index = (vol_index + 1)%8
			master_vol = float((vol_index+1)/8)
			for i in range(0,8):
				if i <= vol_index:
					seq_state[6][i]=True
				else:
					seq_state[6][i]=False
					
		#p will tolggle play or pause
		if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
			if seq_state[7][5]:
				#play is enabled
				seq_state[7][5]=False
				seq_state[7][6]=True
			else:
				seq_state[7][5]=True
				seq_state[7][6]=False
		
		# IF USER CLOSES THE WINDOW
		if event.type == pygame.QUIT:
			done=True
		
		# ESCAPE KEYPRESS
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			done=True
			
		# Pressing a will simulate a random tag event, at a random x,y coordinate
		if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
			x = int(numpy.random.randint(0,8))
			y = int(numpy.random.randint(0,6))
			id = rfgrid.tags[numpy.random.randint(0,rfgrid.tag_count)][0]
			# tag search will return a valid index if the ID sent is
			# within the tags.rfgridtag file
			index = tagSearch(rfgrid.tags,id)
			if index != -1:
				rfgrid.updateGridTiles(x,y,index)
				if(rfgrid.tags[index][0]):
					rfgrid.draw(True,seq_surface,seq_state)
				rfgrid.playTagSound(index,master_vol,10)
	
	clock.tick(30)
pygame.quit()