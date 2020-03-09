import pygame
import ptext
import sys
import os

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = None

def rfgridInit(g_config_name = "./configs/grid.rfgrid", bg_config_name = "./configs/default.rfgridbg",tag_config_name = "./configs/tags.rfgridtag"):
	# layout of .rfgrid file
	G_PARAM_MAX = 10
	G_PARAM_FMT = [
		"scr_w",
		"scr_h",
		"g_w",
		"g_h",
		"g_x",
		"g_y",
		"g_x_step",
		"g_y_step",
		"g_x_tiles",
		"g_y_tiles"
	]
	
	# layout of .rgfridbg file
	BG_PARAM_MAX = 7
	BG_PARAM_FMT = [
		"bg_filename",
		"bg_w",
		"bg_h",
		"bg_ofs_x",
		"bg_ofs_y",
		"bg_x_tiles",
		"bg_y_tiles"
	]

	# check for presence of config file
	if not os.path.isfile(g_config_name):
		print("error: grid configuration file(" + g_config_name + ") not found")
		print(
			"run the calibration tool using this command ->" + 
			"python rfgridCalibration.py default.jpg"
			) 
		exit()
	if not os.path.isfile(bg_config_name):
		print("error: background configuration file(" + bg_config_name + ") not found") 
		exit()

	if not os.path.isfile(tag_config_name):
		print("error: tag configuration file(" + tag_config_name + ") not found") 
		exit()
	g_config_file = open(g_config_name,"r")
	g_params = g_config_file.readlines()
	g_config_file.close()
	grid_args = []
	
	#load the grid parameters from the config file
	if len(g_params) == G_PARAM_MAX:
		for i in range(len(g_params)):
			param = g_params[i].split('=')
			if (len(param) == 2) and (param[0] == G_PARAM_FMT[i]):
				param_name = param[0]
				if param_name == G_PARAM_FMT[i]:
					grid_args.append(int(param[1]))
			else:
				print("error: in grid configuration file(" + g_config_name + ") on line " + (i+1))
				exit()
	else:
		print("error: in grid configuration file(" + g_config_name + ") invalid number of parameters")
		exit()
	
	#load the background parameters from the config file
	bg_config_file = open(bg_config_name,"r")
	bg_params = bg_config_file.readlines()
	bg_config_file.close()
	bg_args = []
	
	if len(bg_params) == BG_PARAM_MAX:
		for i in range(len(bg_params)):
			bg_params[i].rstrip('\n')
			param = bg_params[i].split('=')
			if (len(param) == 2) and (param[0] == BG_PARAM_FMT[i]):
				if i:
					bg_args.append(int(param[1]))
				else:
					bg_filename = str(param[1])
					bg_filename = bg_filename.strip()
					bg_args.append(bg_filename)
					if not os.path.isfile(bg_filename):
						print(
							"error: cannot find background image (" +
							bg_filename +
							") referenced in  background configuration file (" + 
							bg_config_name + 
							") on line " + (i+1)
							)
						exit()
			else:
				print(
					"error: in background configuration file(" + 
					bg_config_name + ") on line " + (i+1)
					)
				exit()
	else:
		print(
			"error: in background configuration file(" + 
			bg_config_name + ") invalid number of parameters"
			)
		exit()

	# Load the tag settings
	tag_config_file = open(tag_config_name,"r")
	tag_params = tag_config_file.readlines()
	tag_args = []
	for i in range(len(tag_params)):
		temp = (tag_params[i].rstrip("\n"))
		tag_args.append(temp.split(","))


		
	# Configuration files loaded successfully. Create the grid based on these settings
	global rfgrid
	global screen
	rfgrid = Grid(grid_args,bg_args,tag_args)
	rfgrid.draw()
	return rfgrid

def createTiles(x_dim,y_dim):
	tiles = {}
	for x in range(0, x_dim):
		for y in range(0,y_dim):
			tiles[x,y] = -1
	return tiles

def tagSearch(tagList,tagID):
	index = 0
	for i in tagList:
		if(int(i[0]) == tagID):
			return index
		index  = index + 1
	return -1

def updateTileMatrix(tileStateMatrix,objIDX,objPos_x,objPos_y):
	for x in range(0,x_dim):
		for y in range(0,y_dim):
			if(tileStateMatrix[x,y]== objIDX):
				tileStateMatrix[x,y] = 0
	tileStateMatrix[objPos_x,objPos_y] = objIDX


class Grid():
	def __init__(self, grid_args, bg_args, tag_args):
		global screen
		# grid parameters
		g_arg_idx = {
			"scr_w"    : 0,
			"scr_h"    : 1,
			"g_w"      : 2,
			"g_h"      : 3,
			"g_x"      : 4,
			"g_y"      : 5,
			"g_x_step" : 6,
			"g_y_step" : 7,
			"g_x_tiles": 8,
			"g_y_tiles": 9
		}
		
		scr_w =         grid_args[g_arg_idx["scr_w"]]
		scr_h =         grid_args[g_arg_idx["scr_h"]]
		g_w =           grid_args[g_arg_idx["g_w"]]
		g_h =           grid_args[g_arg_idx["g_h"]]
		g_x =           grid_args[g_arg_idx["g_x"]]
		g_y =           grid_args[g_arg_idx["g_y"]]
		g_x_step =      grid_args[g_arg_idx["g_x_step"]]
		g_y_step =      grid_args[g_arg_idx["g_y_step"]]
		g_x_tiles=      grid_args[g_arg_idx["g_x_tiles"]]
		g_y_tiles=      grid_args[g_arg_idx["g_y_tiles"]]
		
		# background parameters
		bg_arg_idx = {
			"bg_filename" : 0,
			"bg_w"        : 1,
			"bg_h"        : 2,
			"bg_ofs_x"    : 3,
			"bg_ofs_y"    : 4,
			"bg_x_tiles"  : 5,
			"bg_y_tiles"  : 6
		}
		
		bg_filename = bg_args[bg_arg_idx["bg_filename"]]
		bg_w =        bg_args[bg_arg_idx["bg_w"]]
		bg_h =        bg_args[bg_arg_idx["bg_h"]]
		bg_ofs_x =    bg_args[bg_arg_idx["bg_ofs_x"]]
		bg_ofs_y =    bg_args[bg_arg_idx["bg_ofs_y"]]
		bg_x_tiles =    bg_args[bg_arg_idx["bg_x_tiles"]]
		bg_y_tiles =    bg_args[bg_arg_idx["bg_y_tiles"]]

		# class variables
		self.menu_x = g_x
		self.menu_y = g_y - 2*g_y_step
		self.menu_w = g_w
		self.menu_h = 2*g_y_step
		self.menu_bg_color = (255, 255, 255)
		self.menu_text_color = (0, 0, 0)
		self.menu_text_size = 20
		self.menu_text_width = g_w - 2*g_x_step
		self.menu_str = ""
		self.menu_text_midleft = (g_x_step, g_y_step)
		self.menu_text_shadow_color = (128, 128, 128)
		self.menu_text_shadow_pos = (1,1)
		
		self.bg_filename = bg_filename
		self.bg_w = bg_x_tiles*g_x_step
		self.bg_h = bg_y_tiles*g_y_step
		self.bg_ofs_x = bg_ofs_x*g_x_step + 2
		self.bg_ofs_y = bg_ofs_y*g_y_step + 2
		self.bg_x_tiles = bg_x_tiles
		self.bg_y_tiles = bg_y_tiles

		self.grid_w = g_w
		self.grid_h = g_h
		self.grid_x = g_x
		self.grid_y = g_y
		self.grid_x_step = g_x_step
		self.grid_y_step = g_y_step
		self.grid_x_tiles = g_x_tiles
		self.grid_y_tiles = g_y_tiles

		#this will be the surface on which game objects will be drawn

		# setup the pygame screen
		screen = pygame.display.set_mode((scr_w,scr_h), pygame.FULLSCREEN)
		
		# make the surfaces
		self.grid_surf = pygame.Surface((g_w, g_h))
		self.bg_surf = pygame.transform.smoothscale(pygame.image.load(bg_filename),(bg_w,bg_h))
		self.game_surf = (pygame.Surface((self.bg_surf.get_width(), self.bg_surf.get_height()))).convert_alpha()
		self.game_surf.set_alpha(100)
		self.game_surf.fill((100,100,100,10))
		self.menu_surf = pygame.Surface((g_w, 2*g_y_step))
		self.menu_text_surf, self.menu_text_pos = ptext.draw(
			self.menu_str, 
			midleft = self.menu_text_midleft,
			color = self.menu_text_color,
			shadow = self.menu_text_shadow_pos,
			scolor = self.menu_text_shadow_color,
			fontsize = self.menu_text_size,
			width = self.menu_text_width
			)

		# Store Tag Information
		self.tags = []
		self.tag_count = 0
		for i in tag_args:
			tag = [int(i[0]),str(i[1]),str(i[2]),str(i[3])]
			self.tags.append(tag)
			self.tag_count += 1
		
		# Create a tile matrix corresponding to the size of the background initialized to zero
		self.game_tiles = createTiles(bg_x_tiles,bg_y_tiles)
		self.ignore_zero_ids = True

		# Create Audio channels for each tag
		self.audioChannels = []
		self.entranceSoundPlayed = []
		pygame.mixer.set_num_channels(self.tag_count)
		for i in range(0,self.tag_count):
			self.audioChannels.append(pygame.mixer.Channel(int(i)))
			self.entranceSoundPlayed.append(False)

		
	
	def draw(self):
		global screen
		self.grid_surf.blit(self.bg_surf,(self.bg_ofs_x, self.bg_ofs_y))
		self.game_surf.fill((0,0,0,0))
		x0 = int(round(abs(self.bg_ofs_x)/self.grid_x_step))
		y0 = int(round(abs(self.bg_ofs_y)/self.grid_y_step))
		for x in range(x0,x0 + self.grid_x_tiles):
			for y in range(y0,y0 + self.grid_y_tiles):
				if (self.game_tiles[x,y] != -1):
					# There is a tag on this square
					if self.tags[self.game_tiles[x,y]][1]:
						# there is an image to draw
						img = pygame.image.load(self.tags[self.game_tiles[x,y]][1])
						img = pygame.transform.smoothscale(img,(self.grid_x_step,self.grid_y_step))
						self.drawGame(x,y,img)
		self.grid_surf.blit(self.game_surf,((self.bg_ofs_x, self.bg_ofs_y)))
		self.menu_surf.fill(self.menu_bg_color)
		self.menu_surf.blit(self.menu_text_surf,self.menu_text_pos)
		screen.fill((0,0,0))
		screen.blit(self.grid_surf,(self.grid_x, self.grid_y))
		screen.blit(self.menu_surf,(self.menu_x, self.menu_y))
		pygame.display.flip()

	def playTagSound(self,tag_index):
		if len(self.tags) > tag_index:
			#valid index supplied
			if self.tags[tag_index][2] or self.tags[tag_index][3]:
				#there is a sound file to play
				if not self.entranceSoundPlayed[tag_index]:
					# entrance sound has not been played
					if self.tags[tag_index][2] != '':
						soundEffect = pygame.mixer.Sound(self.tags[tag_index][2])
						self.audioChannels[tag_index].play(soundEffect)
					self.entranceSoundPlayed[tag_index] = True
				elif not (self.audioChannels[tag_index].get_busy()) and (self.tags[tag_index][3] != ''):
					# play movement sound
					soundEffect = pygame.mixer.Sound(self.tags[tag_index][3])
					self.audioChannels[tag_index].play(soundEffect)

	#Draws using absolute x and y coordinates
	def drawGame(self, game_x, game_y, surf):
		if (game_x <= self.bg_x_tiles) and (game_y <= self.bg_y_tiles):
			self.game_surf.blit(surf, (game_x*self.grid_x_step,game_y*self.grid_y_step))

	#Draws using x and y grid coordinates
	def drawGrid(self, grid_x, grid_y, surf):
		if (grid_x <= self.grid_x_tiles) and (grid_y <= self.grid_y_tiles):
			self.game_surf.blit(surf, ((grid_x*self.grid_x_step)-self.bg_ofs_x,(grid_y*self.grid_y_step)-self.bg_ofs_y))
	
	def scrollBackground(self,dx,dy,smooth = False,speed = 5):
		x_test = self.bg_ofs_x + dx*self.grid_x_step
		y_test = self.bg_ofs_y + dy*self.grid_y_step
		if (0 >= x_test) and (x_test >= -(self.bg_surf.get_width() - self.grid_x_tiles*self.grid_x_step)):
			if smooth and int(dx):
				bg_ofs_x_target = self.bg_ofs_x + dx*self.grid_x_step
				nudge_x = int(dx/abs(dx))*speed
				if(dx < 0):
					# we're moving the background right (scrolling the viewport left)
					while(self.bg_ofs_x > bg_ofs_x_target):
						if((self.bg_ofs_x + nudge_x)<bg_ofs_x_target):
							# only advance 1 pixel at a time to ensure
							# that we don't lose grid alignment
							self.bg_ofs_x += int(dx/abs(dx))
							self.draw()
						else:
							# we can scroll faster than 1 pixel/frame
							self.bg_ofs_x += nudge_x
							self.draw()
				else:
					# we're moving the background left (scrolling the viewport right)
					while(self.bg_ofs_x < bg_ofs_x_target):
						if((self.bg_ofs_x + nudge_x)>bg_ofs_x_target):
							# only advance 1 pixel at a time to ensure
							# that we don't lose grid alignment
							self.bg_ofs_x += int(dx/abs(dx))
							self.draw()
						else:
							# we can scroll faster than 1 pixel/frame
							self.bg_ofs_x += nudge_x
							self.draw()
			else:
				self.bg_ofs_x += dx*self.grid_x_step
				self.draw()
		if (0 >= y_test) and (y_test >= -(self.bg_surf.get_height() - self.grid_y_tiles*self.grid_y_step)):
			if smooth and int(dy):
				#we want to scroll the background smoothly
				bg_ofs_y_target = self.bg_ofs_y + dy*self.grid_y_step
				nudge_y = int(dy/abs(dy))*speed
				if(dy < 0):
					# we're moving the background down (scrolling the viewport up)
					while(self.bg_ofs_y > bg_ofs_y_target):
						if((self.bg_ofs_y + nudge_y)<bg_ofs_y_target):
							# only advance 1 pixel at a time to ensure
							# that we don't lose grid alignment
							self.bg_ofs_y += int(dy/abs(dy))
							self.draw()
						else:
							# we can scroll faster than 1 pixel/frame
							self.bg_ofs_y += nudge_y
							self.draw()
				else:
					# we're moving the background up (scrolling the viewport down)
					while(self.bg_ofs_y < bg_ofs_y_target):
						if((self.bg_ofs_y + nudge_y)>bg_ofs_y_target):
							# only advance 1 pixel at a time to ensure
							# that we don't lose grid alignment
							self.bg_ofs_y += int(dy/abs(dy))
							self.draw()
						else:
							# we can scroll faster than 1 pixel/frame
							self.bg_ofs_y += nudge_y
							self.draw()
					
			else:
				self.bg_ofs_y += dy*self.grid_y_step
				self.draw()

	def updateMenu(self, menu_str, txt_sz = 15, col=(0,0,0), bg_col=(255,255,255)):
		self.menu_str = str(menu_str)
		self.menu_text_size = txt_sz
		self.menu_text_color = col
		self.menu_bg_color = bg_col
		self.menu_text_surf, self.menu_text_pos = ptext.draw(
			self.menu_str, 
			midleft = self.menu_text_midleft,
			color = self.menu_text_color,
			shadow = self.menu_text_shadow_pos,
			scolor = self.menu_text_shadow_color,
			fontsize = self.menu_text_size,
			width = self.menu_text_width
			)
		self.draw()

	# uniquely assigns the index to the game_tiles matrix at the coordinates provided
	# Use this one to address global x and y
	def updateGameTiles(self, game_x, game_y, index):
		for x in range(0,self.bg_x_tiles):
			for y in range(0,self.bg_y_tiles):
				if(self.game_tiles[x,y] == index):
					self.game_tiles[x,y] = -1
		self.game_tiles[game_x,game_y] = index
	
	# use this one to address x and y using the values transmitted by the hardware
	def updateGridTiles(self, grid_x, grid_y, index):
		x0 = int(round(abs(self.bg_ofs_x)/self.grid_x_step))
		y0 = int(round(abs(self.bg_ofs_y)/self.grid_y_step))
		for x in range(0,self.bg_x_tiles):
			for y in range(0,self.bg_y_tiles):
				if(self.game_tiles[x,y] == index):
					self.game_tiles[x,y] = -1
		self.game_tiles[x0+grid_x,y0+grid_y] = index
		
	def moveCameraToTag(self,index):
		cam_x = int(round(abs(self.bg_ofs_x)/self.grid_x_step))
		cam_y = int(round(abs(self.bg_ofs_y)/self.grid_y_step))
		tag_x = 0
		tag_y = 0
		for x in range(0,self.bg_x_tiles):
			for y in range(0,self.bg_y_tiles):
				if(self.game_tiles[x,y] == index):
					tag_x = x
					tag_y = y
					break
		if tag_x - 4> cam_x:
			for i in range(0,(tag_x-4)-cam_x):
				self.scrollBackground(-1,0,smooth = True, speed = 20)
		elif tag_x -4< cam_x:
			for i in range(0,cam_x-(tag_x-4)):
				self.scrollBackground(+1,0,smooth = True, speed = 20)
		if tag_y -4> cam_y:
			for i in range(0,(tag_y-4)-cam_y):
				rfgrid.scrollBackground(0,-1,smooth = True,speed = 20)
		elif tag_y -4 < cam_y:
			for i in range(0,cam_y-(tag_y-4)):
				rfgrid.scrollBackground(0,+1,smooth = True,speed = 20)
			