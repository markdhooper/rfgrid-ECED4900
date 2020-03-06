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
	[True,	False,	False,	False,	False,	False,	False,	False]
]

print('seq state')
print(seq_state)
print(seq_state[0][0])
print(seq_state[0,0])


seq_surface = {}
for x in range(0,8):
	for y in range(0,8):
		print(seq_state[x][y])
		if(seq_state[x][y]):
			surf = pygame.image.load(seq_zone_dict[seq_zone_map[y][x]])
			surf = pygame.transform.smoothscale(surf,(rfgrid.grid_x_step,rfgrid.grid_y_step))
			seq_surface[x,y] = surf

for x in range(0,8):
	for y in range(0,8):
		if seq_state[x][y]:
			rfgrid.drawGame(x,y,seq_surface[x,y])
			rfgrid.draw()