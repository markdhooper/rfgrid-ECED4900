import pygame
import sys
import os
#os.chdir(f'./applications/{sys.argv[1]}')
import ptext
scriptDir = os.path.dirname('__file__')

bg_filename = ""
bg_config = ""
configDir = ""
X_DIM = 0
Y_DIM = 0

deviceDim = {
	"4x4": (4,4),
	"8x8": (8,8),
	"12x12": (12,12),
	"16x16": (16,16)
}



# get command line arguments
if len(sys.argv) < 2:
	print(
		"error: rfgrid device dimensions not provided.\n" +
		"\tplease specify dimensions in command line arguments eg. 4x4, 8x8, 12x12, or 16x16."
		) 
	exit()
	
elif(	(sys.argv[1] == "4x4")   or (sys.argv[1] == "8x8")   or
		(sys.argv[1] == "12x12") or (sys.argv[1] == "16x16")
	):
	X_DIM, Y_DIM = deviceDim[sys.argv[1]]
	bg_filename = "./images/backgrounds/" + sys.argv[1] + ".png"
	bg_filename = os.path.join(scriptDir, bg_filename)
	if os.path.isfile(bg_filename):
		configDir = os.path.join(scriptDir,"./configs/")
		if not os.path.isdir(configDir):
			os.mkdir("configs")
		grid_config = open(configDir + "grid.rfgrid","w+")
	else:
		print("error: cannot find file " + bg_filename)
		exit()
else:
	print("error: invalid argument:" + sys.argv[1])
	exit()

pygame.init()
clock = pygame.time.Clock()

def rfgridInit(
	bg_img, scr_w = 1024, scr_h = 768, 
	fullScreen = False, x_tiles = 8, y_tiles = 8, 
	x0 = 256, y0 = 191, x1 = 768, y1 = 573
	):
	
	#declare globals
	global SCR	#screen - which is the pygame.display()
	global GRID #a grid object
	
	#create pygame window
	if fullScreen:
		SCR = pygame.display.set_mode((scr_w,scr_h), pygame.FULLSCREEN)
	else:
		SCR = pygame.display.set_mode((scr_w,scr_h), pygame.RESIZABLE)
		
	#set up the grid
	GRID = Grid(x0,y0,x1,y1,x_tiles,y_tiles, bg_img)
	GRID.drawGrid()

class Grid():
	def __init__(self, x0, y0, x1, y1, x_tiles, y_tiles, bg_img):
		self.surface = pygame.Surface((int(x1-x0),int(y1-y0)))

		self.x0 = x0					# left x coordinate
		self.x1 = x1					# right x coordinate
		self.y0 = y0					# top y coordinate
		self.y1 = y1					# bottom y coordinate
		self.x_step = (x1-x0)//x_tiles	# horizontal distance between tiles 
		self.y_step = (y1-y0)//y_tiles	# vertical distance between tiles
		self.x_tiles = x_tiles			# 
		self.y_tiles = y_tiles

		#used to resize the grid by draging the left mouse from top-left, to bottom-right
		self.gridRect = pygame.rect.Rect(x0,y0,x1,y1)	
		self.gridRect_draging = False					#flags used when resizing
		self.gridRect_dragged = True	
		
		self.bg_original = pygame.image.load(bg_img)
		self.bg = pygame.transform.scale(pygame.image.load(bg_img),((self.x1 - self.x0),(self.y1 - self.y0)))
		
		self.menu = pygame.Surface(((self.x1-self.x0),(2*self.y_step)))
		self.menuColor = (200,200,200)
		self.menu.fill(self.menuColor)
		self.menuStr = 'rfgrid Display Calibration Tool:\nPress \'Enter\' to begin calibration'
		self.menuFontColor = (0,0,0)
	
	def updateMenu(self, str):
		self.menuStr = str
		
	def resizeStart(self,x,y):
		if self.gridRect_draging == False:
			self.gridRect.width = 1
			self.gridRect.height = 1
			self.gridRect.x = x
			self.gridRect.y = y
		self.x0 = x
		self.y0 = y
		self.gridRect_draging = True
		
	def resizeEnd(self):
		self.gridRect_draging = False
		if self.gridRect_dragged == True:
			self.gridRect_dragged = False
			self.x1 = self.gridRect.width + self.gridRect.x
			self.y1 = self.gridRect.height + self.gridRect.y
			self.surface = pygame.Surface(((self.x1-self.x0),(self.y1-self.y0)))
			self.x_step = (self.x1-self.x0)//self.x_tiles
			self.y_step = (self.y1-self.y0)//self.y_tiles
			self.menu = pygame.Surface(((self.x1-self.x0),(2*self.y_step)))
			self.drawGrid()
	
	def updateGridRect(self,x,y):
		if(x > self.gridRect.x and y > self.gridRect.y):
			self.gridRect_dragged = True
			self.gridRect.width = x - self.gridRect.x
			self.gridRect.height = y - self.gridRect.y
			self.x1 = self.gridRect.width + self.gridRect.x
			self.y1 = self.gridRect.height + self.gridRect.y
			self.x_step = (self.x1-self.x0)//self.x_tiles
			self.y_step = (self.y1-self.y0)//self.y_tiles
			self.surface = pygame.Surface(((self.x1-self.x0),(self.y1-self.y0)))
			self.menu = pygame.Surface(((self.x1-self.x0),(2*self.y_step)))
			self.drawGrid()
			pygame.draw.rect(SCR, (255,255,255), self.gridRect, 1)
			pygame.display.flip()

	def drawGrid(self):
		self.bg = pygame.transform.scale(self.bg_original,(self.x1-self.x0,self.y1-self.y0))
		self.surface.blit(self.bg,(0,0))
		self.menu.fill(self.menuColor)
		tsurf, tpos = ptext.draw(self.menuStr,midleft=(self.x_step,self.y_step),fontname="./fonts/UbuntuMono-Regular.ttf",color=self.menuFontColor, shadow=(1,1),scolor=(128,128,128),fontsize=15, width=(self.menu.get_width() - self.x_step*2))
		self.menu.blit(tsurf,tpos)
		SCR.fill((0,0,0))
		SCR.blit(self.surface,(self.x0, self.y0))
		SCR.blit(self.menu,(self.x0, self.y0 - 2*self.y_step))
		pygame.display.flip()
		
#######################################################################
# Beginning of Calibration Loop
#######################################################################
rfgridInit(bg_filename,1024,768,True,X_DIM,Y_DIM,450,350,950,800)
done = False
CALIBRATION_STEP = 0

while not done:
	for event in pygame.event.get():
		
		if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			# User has closed the pygame window or pressed 'ESC'
			done=True
		
		if CALIBRATION_STEP == 0:
			# Welcome Screen
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				# Enter Keypress
				GRID.updateMenu("Left-Click and drag from the top-left to bottom-right of the projection surface")
				GRID.drawGrid()
				CALIBRATION_STEP = 1
				
		elif CALIBRATION_STEP == 1:
			# Aligmnment with projection surface
			if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
				# User has clicked the top left corner of their device's projection surface
				x, y = event.pos
				GRID.resizeStart(x,y)
				GRID.drawGrid()
			elif (event.type == pygame.MOUSEMOTION) and GRID.gridRect_draging:
				# User is dragging the mouse toward the bottom right corner
				# of their device's projection surface
				x, y = event.pos
				GRID.updateGridRect(x,y)
				GRID.drawGrid()
			elif (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
				# User has released the left-click button, save state and move on to step 3
				GRID.resizeEnd()
				GRID.updateMenu("Press \'Enter\' to save your configuration, or Left-Click and drag from the top-left to the bottom-right as needed.")
				GRID.drawGrid()
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				# User has chosen the desired starting location move to step 4
				GRID.updateMenu("Saved Successfully")
				GRID.drawGrid()
		
				#save grid configuration file
				grid_config.write("scr_w=%d\n" % SCR.get_width())
				grid_config.write("scr_h=%d\n" % SCR.get_height())
				grid_config.write("g_w=%d\n" % GRID.surface.get_width())
				grid_config.write("g_h=%d\n" % GRID.surface.get_height())
				grid_config.write("g_x=%d\n" % GRID.x0)
				grid_config.write("g_y=%d\n" % GRID.y0)
				grid_config.write("g_x_step=%d\n" % GRID.x_step)
				grid_config.write("g_y_step=%d\n" % GRID.y_step)
				grid_config.write("g_x_tiles=%d\n" % GRID.x_tiles)
				grid_config.write("g_y_tiles=%d" % GRID.y_tiles)
				grid_config.close()
				done = True
				
	clock.tick(30)
pygame.quit()