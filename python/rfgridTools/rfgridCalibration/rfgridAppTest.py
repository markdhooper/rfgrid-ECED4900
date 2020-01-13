from rfgrid import *
import numpy

rfgrid = rfgridInit(bg_config_name = "./configs/pit1.rfgridbg")
rfgrid.updateMenu("Application Test",100,(255,0,128),(255,255,255))
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