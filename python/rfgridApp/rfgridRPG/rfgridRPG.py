import pygame
import ptext

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

def rfgridInit(
	scr_w = 1600, scr_h = 900, fullScreen = False, 
	x_tiles = 8, y_tiles = 8,
	x0 = 388, x1 = 1029 , y0 = 244 , y1 = 894,
	bg_img = 'bg.jpg'  #CHANGE THIS LATER & ADD ERROR CHECKING
	):
	
	#declare globals
	global SCR	#screen - which is the pygame.display()
	global GRID #a grid object
	global BG	#a copy of the original background image file
	global MAX_RES

	MAX_RES = 32*scr_w
	
	#save a copy of the original background image
	BG = pygame.image.load(bg_img)
	
	#create pygame window
	if fullScreen:
		SCR = pygame.display.set_mode((scr_w,scr_h), pygame.FULLSCREEN)
	else:
		SCR = pygame.display.set_mode((scr_w,scr_h), pygame.RESIZABLE)
		
	#set up the grid
	GRID = Grid(x0,x1,y0,y1,x_tiles,y_tiles, bg_img)
	GRID.drawGrid()

def initTiles(x_tiles,y_tiles):
    tiles = {}
    for x in range(0, x_tiles):
        for y in range(0, y_tiles):
            tiles[x,y] = 0
    return tiles

class Grid():
	def __init__(self, x0, x1, y0, y1, x_tiles, y_tiles, bg_img):
		self.surface = pygame.Surface((int(x1-x0),int(y1-y0)))
		######################################################
		# POSITION
		######################################################
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
		
		#######################################################
		# STATE
		#######################################################
		self.tiles = initTiles(x_tiles, y_tiles)	# 2D dictionary of tile state information
		self.show_grid_lines = False				# flag indicates whether to draw gridlines
		
		#######################################################
		# BACKGROUND 
		#######################################################
		self.bg_offset_x = 0						# x-offset into the background image
		self.bg_offset_y = 0						# y-offset into the background image
		self.bg = pygame.image.load(bg_img)			# the background image
		
		# the scale rect is used to allign the background image to our gridlines
		# by right-clicking and draging the mouse from the top-left corner 
		# to the bottom-right corner of a single tile
		self.scaleRect = pygame.rect.Rect(x0,y0,x1//x_tiles,y1//y_tiles) 
		self.scaleRect_draging = False				# flags used when resizing
		self.scaleRect_dragged = True
		
		self.x_scale = 2244
		self.y_scale = 2756
		
		#######################################################
		# MENU
		#######################################################
		self.menu = pygame.Surface(((self.x1-self.x0),(2*self.y_step)))
		self.menuColor = (200,200,200)
		self.menu.fill(self.menuColor)
		self.menuStr = 'RFGRID'
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

	def scaleStart(self,x,y):
		if self.scaleRect_draging == False:
			self.scaleRect.width = 1
			self.scaleRect.height = 1
			self.scaleRect.x = x
			self.scaleRect.y = y
		self.scaleRect_draging = True
	
	def scaleEnd(self):
		self.scaleRect_draging = False
		if self.scaleRect_dragged == True:
			self.scaleRect_dragged = False
			self.x_scale = int(round(self.bg.get_width()*((self.x1-self.x0)/(self.scaleRect.width*(self.x_tiles/3)))))
			self.y_scale = int(round(self.bg.get_height()*((self.y1-self.y0)/((self.scaleRect.height)*(self.y_tiles/3)))))
			if ( (self.x_scale < MAX_RES) and (self.y_scale < MAX_RES) ):
				self.bg = pygame.transform.smoothscale(BG,(self.x_scale,self.y_scale))
			self.drawGrid()

	def updateScaleRect(self,x,y):
		x_adj = 5
		y_adj = 0
		if((x > self.scaleRect.x + x_adj) and (y > self.scaleRect.y + y_adj)):
			self.scaleRect_dragged = True
			self.scaleRect.width = x - self.scaleRect.x - x_adj
			self.scaleRect.height = y - self.scaleRect.y - y_adj
			self.drawGrid()
			x_inc = self.scaleRect.width//3
			y_inc = self.scaleRect.height//3
			innerRect = pygame.rect.Rect(self.scaleRect.x,self.scaleRect.y,x_inc,y_inc)

			for i in range (0,3):
				for j in range (0,3):
					pygame.draw.rect(SCR, (200,200,200), innerRect, 1)
					innerRect.y = innerRect.y + y_inc
					pygame.display.flip()
				innerRect.x = innerRect.x + x_inc
				innerRect.y = innerRect.y - 3*y_inc

			pygame.draw.rect(SCR, (255,255,255), self.scaleRect, 2)
			pygame.display.flip()
			

	def drawGrid(self):
		self.bg = pygame.transform.smoothscale(BG,(self.x_scale,self.y_scale))
		self.surface.blit(self.bg,(GRID.bg_offset_x, GRID.bg_offset_y))#(0,0, GRID.x1-GRID.x0, GRID.y1-GRID.y0))
		self.menu.fill(self.menuColor)
		tsurf, tpos = ptext.draw(self.menuStr,midleft=(self.x_step,self.y_step),fontname="fonts/whitrabt.ttf",color=self.menuFontColor, shadow=(1,1),scolor=(128,128,128),fontsize=15, width=(self.menu.get_width() - self.x_step*2))
		self.menu.blit(tsurf,tpos)
		SCR.fill((0,0,0))
		SCR.blit(self.surface,(self.x0, self.y0))
		SCR.blit(self.menu,(self.x0, self.y0 - 2*self.y_step))
		pygame.display.flip()
			
	def scrollGrid(self,dx,dy):
		x_test = self.bg_offset_x + dx*self.x_step
		y_test = self.bg_offset_y + dy*self.y_step
		if (0 >= x_test) and (x_test >= -(self.bg.get_width() - self.x_tiles*self.x_step)):
			self.bg_offset_x += dx*self.x_step
		if (0 >= y_test) and (y_test >= -(self.bg.get_height() - self.y_tiles*self.y_step)):
			self.bg_offset_y += dy*self.y_step
		self.drawGrid()
		
#######################################################################
# Beginning of Calibration Loop
#######################################################################
rfgridInit(1600,900,True,8,8)
done = False

while not done:
	for event in pygame.event.get():
		# IF USER CLOSES THE WINDOW
		if event.type == pygame.QUIT:
			done=True
		
		# ESCAPE KEYPRESS
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			done=True

		# ARROW KEYPRESSES
		if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			GRID.scrollGrid(-1,0)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			GRID.scrollGrid(+1,0)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			GRID.scrollGrid(0,+1)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			GRID.scrollGrid(0,-1)
	
	clock.tick(30)
pygame.quit()