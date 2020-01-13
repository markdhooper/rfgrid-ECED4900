import pygame
import ptext
import sys
import os

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()
screen = None

scriptDir = os.path.dirname('__file__')
bg_filename = ""
bg_config = ""
configDir = ""

if len(sys.argv) == 1:
	print(
		"error: filename for background not provided.\n" +
		"\tplease provide the name of the desired background image in the /images/backgrounds folder."
		) 
	exit()
else:
	bg_filename = "./images/backgrounds/" + sys.argv[1]
	bg_filename = os.path.join(scriptDir, bg_filename)
	if os.path.isfile(bg_filename):
		configDir = os.path.join(scriptDir,"./configs/")
		if not os.path.isdir(configDir):
			os.mkdir("configs")
		bg_config, ext = os.path.splitext((sys.argv[1]))
	else:
		print("error: cannot find file " + bg_filename)
		exit()


def rfgridInit(g_config_name = './configs/grid.rfgrid', bg_filename = "./images/backgrounds/default.jpg"):
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
			"run the display calibration tool using this command ->" + 
			"python rfgridDispCalib.py"
			) 
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
		if (0 >= x_test) and (x_test >= -(self.bg_surf.get_width() - self.grid_x_tiles*self.grid_x_step)):
			self.bg_ofs_x += dx*self.grid_x_step
		if (0 >= y_test) and (y_test >= -(self.bg_surf.get_height() - self.grid_y_tiles*self.grid_y_step)):
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
		self.bg_surf = pygame.image.load(self.bg_filename)
		self.bg_ofs_x = 0
		self.bg_ofs_y = 0
		REL_DIVISOR_H = int(((self.bg_surf.get_height()*2)/(self.grid_surf.get_height()*1)))
		REL_DIVISOR_W = int(((self.bg_surf.get_width()*2)/(self.grid_surf.get_width()*1)))
		grid_tile_w = float(self.grid_w/self.grid_x_tiles)
		grid_tile_h = float(self.grid_h/self.grid_y_tiles)
		self.bg_surf = pygame.image.load(self.bg_filename)
		selection = 0
		msgStr = ( "Select a tile area:\n" +
					"1:" + str(REL_DIVISOR_W) + "x" + str(REL_DIVISOR_H) + "\n" +
					"2:" + str(REL_DIVISOR_W//2) + "x" + str(REL_DIVISOR_H//2) + "\n" +
					"3:" + str(REL_DIVISOR_W*2) + "x" + str(REL_DIVISOR_H*2) + "\n" +
					"4:" + str(REL_DIVISOR_W//3) + "x" + str(REL_DIVISOR_H//3) + "\n"
				)
		self.updateMenu(msgStr, txt_sz = 30)
		self.draw()
		selection = False
		while not selection:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
					selection = True
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_2:
					REL_DIVISOR_H=REL_DIVISOR_H//2
					REL_DIVISOR_W=REL_DIVISOR_W//2
					selection = True
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_3:
					REL_DIVISOR_H=REL_DIVISOR_H*2
					REL_DIVISOR_W=REL_DIVISOR_W*2
					selection = True
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_4:
					REL_DIVISOR_H=REL_DIVISOR_H//3
					REL_DIVISOR_W=REL_DIVISOR_W//3
					selection = True
			clock.tick(30)
		
		msgStr = (	"Drag the cursor to highlight a " + 
					str(REL_DIVISOR_W) + "x" + str(REL_DIVISOR_H) +
					"section of tiles"
				)
		self.updateMenu(msgStr, txt_sz = 30)
		self.draw()
		scale_done = False
		x0,y0,x1,y1 = 0,0,1,1
		scale_moving = False
		scale_valid = False
		scale_rect = pygame.rect.Rect(x0,y0,x1,y1)	
		while not scale_done:
			for event in pygame.event.get():
				if (event.type == pygame.MOUSEBUTTONDOWN) and (event.button == 1):
					if scale_moving == False:
						scale_rect.x, scale_rect.y = event.pos
						scale_rect.w = 1
						scale_rect.h = 1
					scale_moving = True
					self.draw()
				elif (event.type == pygame.MOUSEMOTION) and scale_moving:
					x, y = event.pos
					if((x > scale_rect.x + 5) and (y > scale_rect.y + 5)):
						scale_valid = True
						scale_rect.width = x - scale_rect.x
						scale_rect.height = y - scale_rect.y
						self.draw()
						x_inc = int(round(scale_rect.width/REL_DIVISOR_W))
						y_inc = int(round(scale_rect.height/REL_DIVISOR_H))
						innerRect = pygame.rect.Rect(scale_rect.x,scale_rect.y,x_inc,y_inc)

						for i in range (0,REL_DIVISOR_W):
							for j in range (0,REL_DIVISOR_H):
								pygame.draw.rect(screen, (200,128,128), innerRect, 1)
								innerRect.y = innerRect.y + y_inc
							innerRect.x = int(innerRect.x + x_inc)
							innerRect.y = int(innerRect.y - REL_DIVISOR_H*y_inc)
						pygame.draw.rect(screen, (255,255,255), scale_rect, 3)
						pygame.display.flip()
						
				elif (event.type == pygame.MOUSEBUTTONUP) and (event.button == 1):
					scale_moving = False
					if scale_valid:
						scale_valid = False
						bg_tile_w = float(scale_rect.width/REL_DIVISOR_W)
						bg_tile_h = float(scale_rect.height/REL_DIVISOR_H)
						self.bg_x_tiles = round(self.bg_surf.get_width()/bg_tile_w)
						self.bg_y_tiles = round(self.bg_surf.get_height()/bg_tile_h)
						horizontal_factor = ((self.grid_w)/self.grid_x_tiles)/(self.bg_surf.get_width()/self.bg_x_tiles)
						vertical_factor = ((self.grid_h)/self.grid_y_tiles)/(self.bg_surf.get_height()/self.bg_y_tiles)
						new_bg_width = int(round(self.bg_surf.get_width()*horizontal_factor))
						new_bg_height = int(round(self.bg_surf.get_height()*vertical_factor))
						self.bg_surf = pygame.transform.smoothscale(self.bg_surf,(new_bg_width,new_bg_height))
						self.updateMenu("Scaling Complete:\n use the arrow keys to choose the starting position and press \'s\' to save or \'r\' to re-scale", txt_sz = 30)
						scale_done = True
			clock.tick(30)
		self.draw()

rfgrid = rfgridInit(bg_filename = bg_filename)
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
			bg_config_file = open(configDir + bg_config + ".rfgridbg", "w+")
			# save background configuration file
			bg_config_file.write("bg_filename=%s\n" % rfgrid.bg_filename)
			bg_config_file.write("bg_w=%d\n" % rfgrid.bg_surf.get_width())
			bg_config_file.write("bg_h=%d\n" % rfgrid.bg_surf.get_height())
			bg_config_file.write("bg_ofs_x=%d\n" % rfgrid.bg_ofs_x)
			bg_config_file.write("bg_ofs_y=%d\n" % rfgrid.bg_ofs_y)
			bg_config_file.write("bg_x_tiles=%d\n"% rfgrid.bg_x_tiles)
			bg_config_file.write("bg_y_tiles=%d\n"% rfgrid.bg_y_tiles)
			bg_config_file.close()
			done=True
	clock.tick(30)
pygame.quit()