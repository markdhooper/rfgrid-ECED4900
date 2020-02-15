# Add this later, simply process all background images in the background folder one at a time.
# os.chdir("./images/backgrounds/")
# for file in glob.glob("*.jpg"):
#	print(file)


import pygame
import sys
import os
import math
import glob

#os.chdir("./applications/" + sys.argv[1])
import ptext
#os.chdir("..")
#os.chdir("..")

# Configure Pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

# Pygame related variables
screen = None

# Command line argument variables
scriptDir = os.path.dirname('__file__')
bg_filename = []
bg_config = []
configDir = ""
bg_processed = 0

print("helloworld")

# get command line arguments
if len(sys.argv) == 1:
	# User did not provide any arguments
	configDir = os.path.join(scriptDir,"./configs/")
	os.chdir("./images/backgrounds/")
	for file in glob.glob("*.jpg"):
		bg_filename.append(file)
		f_name, ext = os.path.splitext((file))
		bg_config.append(f_name)
	os.chdir("..")
	os.chdir("..")
else:
	# user provided an argument (the name of the background image that they want to scale)
	bg_filename.append(str("./images/backgrounds/" + sys.argv[1]))
	bg_filename[0] = os.path.join(scriptDir, str(bg_filename[0]))
	if os.path.isfile(bg_filename[0]):
		# a file with the name provided by the user is in the ./images/backgrounds directory
		configDir = os.path.join(scriptDir,"./configs/")
		if not os.path.isdir(configDir):
			# there is no config directory, create one
			os.mkdir("configs")
		# store the name of the background image file (without the file extension)
		f_name, ext = os.path.splitext((sys.argv[1]))
		bg_config.append(f_name)
	else:
		# we were unable to locate an image matching the user's argument
		# in the ./images/backgrounds folder
		print("error: cannot find file " + str(bg_filename[0]))
		# close the application
		exit()




#################################################################################################
# Function Name: rfgridInit
# Description:
# 	This function loads in the .rfgrid configuration file and the background image.
#	It creates a Grid object using the parameters provided in the .rfgrid file
#	to create an area on the screen that matches the play area on the rfgrid device. 
#	if the .rfgrid file in the arguments provided does not exist or does not match the 
#	format. Then the user needs to run the rfgrid display calibration tool (rfgridDispCalib.py).
#	Which will create the file in the required format.
#################################################################################################
def rfgridInit(g_config_name = "./configs/grid.rfgrid", bg_filename = "./images/backgrounds/default.jpg"):
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
		#print("error: grid configuration file(" + g_config_name + ") not found")
		
		#print(
		#	"run the display calibration tool using this command ->" + 
		#	"python rfgridDispCalib.py"
		#	) 
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
	
	#check to ensure that the correct file name was called in rfgridInit()
	if not os.path.isfile(bg_filename):
		print("error: cannot find file (" + bg_filename + ")")
		exit()
	
	# Prepare background Image for Grid Constructor
	temp_bg = pygame.image.load(bg_filename)
	temp_w = temp_bg.get_width()
	temp_h = temp_bg.get_height()
	temp_bg_ofs_x = 0
	temp_bg_ofs_y = 0
	temp_bg_x_tiles = grid_args[8]
	temp_bg_y_tiles = grid_args[9]
	
	bg_args = [
		bg_filename,
		temp_w,
		temp_h,
		temp_bg_ofs_x,
		temp_bg_ofs_y,
		temp_bg_x_tiles,
		temp_bg_y_tiles
	]
		
	# Configuration files loaded successfully. Create the grid based on these settings
	global rfgrid
	global screen
	rfgrid = Grid(grid_args,bg_args)
	rfgrid.draw()
	return rfgrid
	
class Grid():
	def __init__(self, grid_args, bg_args):
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
		
		bg_filename =   bg_args[bg_arg_idx["bg_filename"]]
		bg_w =          bg_args[bg_arg_idx["bg_w"]]
		bg_h =          bg_args[bg_arg_idx["bg_h"]]
		bg_ofs_x =      bg_args[bg_arg_idx["bg_ofs_x"]]
		bg_ofs_y =      bg_args[bg_arg_idx["bg_ofs_y"]]
		bg_x_tiles =    bg_args[bg_arg_idx["bg_x_tiles"]]
		bg_y_tiles =    bg_args[bg_arg_idx["bg_y_tiles"]]
		
		# class variables
		self.menu_x = g_x
		self.menu_y = g_y - 2*g_y_step
		self.menu_w = g_w
		self.menu_h = 2*g_y_step
		self.menu_bg_color = (200, 200, 200)
		self.menu_text_color = (0, 0, 0)
		self.menu_text_size = 20
		self.menu_text_width = g_w - 2*g_x_step
		self.menu_str = ""
		self.menu_text_midleft = (g_x_step, g_y_step)
		self.menu_text_shadow_color = (128, 128, 128)
		self.menu_text_shadow_pos = (1,1)
		
		self.bg_filename = bg_filename
		self.bg_w = bg_w 
		self.bg_h = bg_h
		self.bg_ofs_x = bg_ofs_x
		self.bg_ofs_y = bg_ofs_y
		self.bg_x_tiles = g_x_tiles
		self.bg_y_tiles = g_y_tiles
		
		self.grid_w = g_w
		self.grid_h = g_h
		self.grid_x = g_x
		self.grid_y = g_y
		self.grid_x_step = g_x_step
		self.grid_y_step = g_y_step
		self.grid_x_tiles = g_x_tiles
		self.grid_y_tiles = g_y_tiles
		
		# setup the pygame screen
		screen = pygame.display.set_mode((scr_w,scr_h), pygame.FULLSCREEN)
		
		# make the surfaces
		self.grid_surf = pygame.Surface((g_w, g_h))
		self.bg_surf = pygame.transform.smoothscale(pygame.image.load(bg_filename),(bg_w,bg_h))
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
	
	def draw(self):
		global screen
		self.grid_surf.fill((0,0,0))
		self.grid_surf.blit(self.bg_surf,(self.bg_ofs_x, self.bg_ofs_y))
		self.menu_surf.fill(self.menu_bg_color)
		self.menu_surf.blit(self.menu_text_surf,self.menu_text_pos)
		screen.fill((0,0,0))
		screen.blit(self.grid_surf,(self.grid_x, self.grid_y))
		screen.blit(self.menu_surf,(self.menu_x, self.menu_y))
		pygame.display.flip()
			
	def scrollBackground(self,dx,dy):
		x_test = self.bg_ofs_x + dx*self.grid_x_step
		y_test = self.bg_ofs_y + dy*self.grid_y_step
		if ((self.grid_x_step//2) >= x_test) and (x_test >= -(self.bg_surf.get_width() - self.grid_x_tiles*self.grid_x_step)):
			self.bg_ofs_x += dx*self.grid_x_step
		if ((self.grid_y_step//2) >= y_test) and (y_test >= -(self.bg_surf.get_height() - self.grid_y_tiles*self.grid_y_step)):
			self.bg_ofs_y += dy*self.grid_y_step
		self.draw()
	
	def updateMenu(self, menu_str, txt_sz = 15, col=(0,0,0), bg_col=(200,200,200)):
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
	
	def scaleBackground(self):
		#Load the backgroud image
		self.bg_surf = pygame.image.load(self.bg_filename)
		self.bg_ofs_x = 0
		self.bg_ofs_y = 0
		OPT_W = [2, 3, 4, 6, 10]
		OPT_H = [2, 3, 4, 6, 10]
		tile_count_w = 1
		tile_count_h = 1
		
		
		# allow user to select 
		msgStr = ( "Choose a tile area to select (the bigger the better)\n" +
					"1: " + str(OPT_W[0]) + " x " + str(OPT_H[0]) + "\n" +
					"2: " + str(OPT_W[1]) + " x " + str(OPT_H[1]) + "\n" +
					"3: " + str(OPT_W[2]) + " x " + str(OPT_H[2]) + "\n" +
					"4: " + str(OPT_W[3]) + " x " + str(OPT_H[3]) + "\n" +
					"5: " + str(OPT_W[4]) + " x " + str(OPT_H[4])
				)
		self.updateMenu(msgStr, txt_sz = 20)
		self.draw()
		selection = False
		
		# wait for the user to select an option in the menu
		while not selection:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_1:
						selection = True
						tile_count_h=OPT_H[0]
						tile_count_w=OPT_W[0]
					elif event.key == pygame.K_2:
						selection = True
						tile_count_h=OPT_H[1]
						tile_count_w=OPT_W[1]
					elif event.key == pygame.K_3:
						selection = True
						tile_count_h=OPT_H[2]
						tile_count_w=OPT_W[2]
					elif event.key == pygame.K_4:
						selection = True
						tile_count_h=OPT_H[3]
						tile_count_w=OPT_W[3]
					elif event.key == pygame.K_5:
						selection = True
						tile_count_h=OPT_H[4]
						tile_count_w=OPT_W[4]
			clock.tick(30)
			
		# update the instructions for the user
		msgStr = (	"Drag the cursor to highlight a " + 
					str(tile_count_w) + " x " + str(tile_count_h) +
					" section of tiles in the background"
				)
		self.updateMenu(msgStr, txt_sz = 30)
		self.draw()
		
		
		# Now we can let the user use the mouse to select a tile area
		scale_done = False
		x0,y0,x1,y1 = 0,0,1,1
		scale_moving = False
		scale_valid = False
		scale_rect = pygame.rect.Rect(x0,y0,x1,y1)
		scale_color = ((255,255,255))
		inner_color = ((255,100,100))
		
		while not scale_done:
			for event in pygame.event.get():
				if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
					# user has clicked on the top left corner of a group of tiles
					if scale_moving == False:
						scale_rect.x, scale_rect.y = event.pos
						scale_rect.w = 1
						scale_rect.h = 1
					scale_moving = True
					self.draw()
					
				elif (event.type == pygame.MOUSEMOTION) and scale_moving:
					x, y = event.pos
					if((x > scale_rect.x + 10) and (y > scale_rect.y + 10)):
						# user is intentionally dragging the mouse cursor
						scale_valid = True
						scale_rect.width = x - scale_rect.x
						scale_rect.height = y - scale_rect.y
						scale_rect_ratio = round((scale_rect.width/scale_rect.height),3)
						target_ratio = round((tile_count_w/tile_count_h),3)
						
						#clear the previous rectangle
						self.draw()
						
						if scale_rect_ratio == target_ratio:
							inner_color = ((80,255,80))
							x_inc = int(scale_rect.width/tile_count_w)
							y_inc = int(scale_rect.height/tile_count_h)
							innerRect = pygame.rect.Rect(scale_rect.x+4,scale_rect.y+4,x_inc-tile_count_w,y_inc-tile_count_h)
							for i in range (0,tile_count_w):
								for j in range (0,tile_count_h):
									pygame.draw.rect(screen, inner_color, innerRect, 2)
									innerRect.y = int(innerRect.y + y_inc)
								innerRect.x = int(innerRect.x + x_inc)
								innerRect.y = int(innerRect.y - tile_count_h*y_inc)
							
						pygame.draw.rect(screen, scale_color, scale_rect, 2)
						pygame.display.flip()
						
				elif (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
					scale_moving = False
					if scale_valid:
						# user didn't mis-click
						scale_valid = False
						bg_tile_w = float(scale_rect.width/tile_count_w)
						bg_tile_h = float(scale_rect.height/tile_count_h)
						self.bg_x_tiles = int(round(self.bg_surf.get_width()/bg_tile_w))
						self.bg_y_tiles = int(round(self.bg_surf.get_height()/bg_tile_h))
						new_bg_width = self.bg_x_tiles*self.grid_x_step
						new_bg_height = self.bg_y_tiles*self.grid_y_step
						self.bg_surf = pygame.transform.smoothscale(self.bg_surf,(new_bg_width,new_bg_height))
						self.bg_ofs_x = -round((((new_bg_width/self.bg_x_tiles)*(self.grid_x_tiles))-self.grid_surf.get_width())/2)
						self.bg_ofs_y = -round((((new_bg_height/self.bg_y_tiles)*(self.grid_y_tiles))-self.grid_surf.get_height())/2)
						print(self.bg_ofs_x)
						print(self.bg_ofs_y)
						self.updateMenu("Scaling Complete:\n use the arrow keys to choose the starting position and press \'s\' to save or \'r\' to re-scale", txt_sz = 30)
						scale_done = True
			clock.tick(30)
		self.draw()

	def configureNewBackground(self,bg_img):
		self.bg_surf = pygame.image.load(bg_img)
		self.bg_filename = bg_img
		self.bg_w = self.bg_surf.get_width() 
		self.bg_h = self.bg_surf.get_height()
		self.bg_ofs_x = 0
		self.bg_ofs_y = 0
		self.bg_x_tiles = self.grid_x_tiles
		self.bg_y_tiles = self.grid_x_tiles
		rfgrid.updateMenu("rfgrid background scaler:\n Press \'Enter\' to start",30)
		self.draw()
		

rfgrid = rfgridInit(bg_filename = str(bg_filename[0]))
rfgrid.updateMenu("rfgrid background scaler:\n Press \'Enter\' to start",30)
done = False

while not done:
	for event in pygame.event.get():
		# IF USER CLOSES THE WINDOW
		if event.type == pygame.QUIT:
			done=True
		
		# ESCAPE KEYPRESS
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			done=True
		if event.type == pygame.KEYDOWN and (event.key == pygame.K_RETURN):
			rfgrid.scaleBackground()
		elif event.type == pygame.KEYDOWN and (event.key == pygame.K_r):
			rfgrid.scaleBackground()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			rfgrid.scrollBackground(-1,0)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			rfgrid.scrollBackground(+1,0)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			rfgrid.scrollBackground(0,+1)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			rfgrid.scrollBackground(0,-1)
		elif event.type == pygame.KEYDOWN and (event.key == pygame.K_s):
			
			bg_config_file = open(configDir + str(bg_config[bg_processed]) + ".rfgridbg", "w+")
			# save background configuration file
			bg_config_file.write("bg_filename=%s\n" % rfgrid.bg_filename)
			bg_config_file.write("bg_w=%d\n" % rfgrid.bg_surf.get_width())
			bg_config_file.write("bg_h=%d\n" % rfgrid.bg_surf.get_height())
			bg_config_file.write("bg_ofs_x=%d\n" % int(round(rfgrid.bg_ofs_x//rfgrid.grid_x_step)))
			bg_config_file.write("bg_ofs_y=%d\n" % int(round(rfgrid.bg_ofs_y//rfgrid.grid_y_step)))
			bg_config_file.write("bg_x_tiles=%d\n"% rfgrid.bg_x_tiles)
			bg_config_file.write("bg_y_tiles=%d\n"% rfgrid.bg_y_tiles)
			bg_config_file.close()
			bg_processed += 1
			if bg_processed == len(bg_filename):
				done=True
			else:
				print(str(bg_filename[bg_processed]))
				rfgrid.configureNewBackground("./images/backgrounds/" + str(bg_filename[bg_processed]))
	clock.tick(30)
pygame.quit()