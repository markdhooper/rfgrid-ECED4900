from rfgrid import *
import numpy

rfgrid = rfgridInit(bg_config_name = "./configs/interior1.rfgridbg")
rfgrid.updateMenu("Demo Jan 21, 2020",100,(0,0,0),(100,100,100))
done = False

tags = {
	"0"			: "./images/objects/blank.png",
	"1952181250"	: "./images/objects/dwarf_male_def 03.png",
	"3871206146"	: "./images/objects/elf_fem_arch 01.png",
	"1993009922"	: "./images/objects/extras_hum_male_sage 00.png",
	"935914242"	: "./images/objects/halfling_male_war 00.png",
	"1322117890"	: "./images/objects/hum_fem_div 04.png",
	"163375874"	: "./images/objects/hum_male_caster 23.png",
	"963196400"	: "./images/objects/dark caster 00.png",
	"2313895152"	: "./images/objects/dark caster 01.png",
	"3910286320"	: "./images/objects/dark cavalry 00.png",
	"1506097648"	: "./images/objects/dark champion_halforc 00.png",
	"3388159472"	: "./images/objects/dark general 00.png",
	"1766797808"	: "./images/objects/dark paladin 00.png",
	"421278960"	: "./images/objects/doppelganger 00.png",
	"2041722096"	: "./images/objects/Doresain the Ghoul King 00.png",
	"1231895280"	: "./images/objects/drow_male_arc 00.png",
	"3646501104"	: "./images/objects/firbolg_bloodhunter 00.png",
	"1506490864"	: "./images/objects/firbolg_ghostraven 00.png",
	"2577282800"	: "./images/objects/ghost_goblin 01.png",
	"2034515184"	: "./images/objects/ghoul_stench 01.png",
	"3910349040"	: "./images/objects/goblin_blackblade 00.png",
	"961101040"	: "./images/objects/goblin_blackblade 01.png",
	"971455728"	: "./images/objects/goblin_caster 00.png",
	"963459824"	: "./images/objects/goblin_minion 00.png",
	"4184814064"	: "./images/objects/goblin_ninja 00.png",
	"2312647152"	: "./images/objects/goblin_pirate 00.png",
	"963853040"	: "./images/objects/halforc_fem_war 01.png",
	"972369904"	: "./images/objects/halforc_male 03.png",
	"1232419056"	: "./images/objects/halforc_male_div 00.png",
	"2303800816"	: "./images/objects/halforc_male_war 02.png",
	"3108255728"	: "./images/objects/halforc_male_war 03.png",
	"695941360"	: "./images/objects/halforc_male_war 04.png",
	"432812272"	: "./images/objects/corrupted_hum_caster 00.png",
	"1765291504"	: "./images/objects/hum_dark champion 00.png",
	"3120051696"	: "./images/objects/hum_male 16.png",
	"163462128"	: "./images/objects/hum_male_caster 20.png",
	"2311927792"	: "./images/objects/hum_male_def 09.png",
	"1227045360"	: "./images/objects/hum_male_knight 01.png",
	"435040496"	: "./images/objects/hum_male_rog 06.png",
	"2312321008"	: "./images/objects/lich_baelnorn 00.png",
	"960444400"	: "./images/objects/minotaur_shaman 00.png",
	"4189928432"	: "./images/objects/minotaur_warrior 00.png",
	"2849124848"	: "./images/objects/ogre_01.png",
	"2307276272"	: "./images/objects/ogre_brute 00.png",
	"429471472"	: "./images/objects/orc_armored 00.png",
	"1774926320"	: "./images/objects/orc_brute 00.png",
	"2300393968"	: "./images/objects/orc_brute 01.png",
	"699741424"	: "./images/objects/orc_caster 00.png",
	"4179704304"	: "./images/objects/blaspheme_chill 00.png",
	"164115696"	: "./images/objects/blaspheme_entomber 00.png",
	"167456752"	: "./images/objects/blaspheme_knight 00.png",
	"2302950640"	: "./images/objects/blaspheme_soul vessel 00.png",
	"1775908336"	: "./images/objects/bronze dragon_Gar 00.png",
	"2568502256" : "./images/objects/goliath_male_war 06.png"
}

import serial

# set up serial port and variables for communication
CMD_UPDATE = b'\x00'
serPort = serial.Serial(port = "COM3", baudrate = 9600, timeout = 1)
serPort.flushOutput() 
serPort.flushInput() 
ID = 0
x = 0
y = 0


while not done:
	if (serPort.inWaiting() > 0):
		if serPort.read(1) == CMD_UPDATE:
			ID = int.from_bytes(serPort.read(4), byteorder = 'big', signed = 0)
			x  = int.from_bytes(serPort.read(1), byteorder = 'big', signed = 0)
			y  = int.from_bytes(serPort.read(1), byteorder = 'big', signed = 0)
			if ID != 0:
				image = pygame.transform.smoothscale(pygame.image.load(tags[str(ID)]),(rfgrid.grid_x_step,rfgrid.grid_y_step))
				rfgrid.drawGrid(x,y,image)
			else:
				blankRect = pygame.Surface((rfgrid.grid_x_step,rfgrid.grid_y_step))
				blankRect.blit(rfgrid.bg_surf, (rfgrid.bg_ofs_x + x*rfgrid.grid_x_step,rfgrid.bg_ofs_y+ y*rfgrid.grid_y_step))
				print(rfgrid.grid_x_step*x + rfgrid.bg_ofs_x)
				print(rfgrid.grid_y_step*y - rfgrid.bg_ofs_y)
				print(rfgrid.grid_x_step + rfgrid.grid_x_step*x + rfgrid.bg_ofs_x)
				print(rfgrid.grid_y_step + rfgrid.grid_y_step*y - rfgrid.bg_ofs_y)
				rfgrid.drawGrid(x,y,blankRect)


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

		# a will spawn a rect at a random place within view
		if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
			x = numpy.random.randint(0,8)
			y = numpy.random.randint(0,8)
			w = rfgrid.grid_x_step
			h = rfgrid.grid_y_step
			randRect = pygame.Surface((w,h))
			randRect.fill((255,255,255))
			rfgrid.drawGrid(x,y,randRect)
	
	clock.tick(30)
pygame.quit()