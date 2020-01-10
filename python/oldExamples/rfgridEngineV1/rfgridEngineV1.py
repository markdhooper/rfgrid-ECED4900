#CONSTANTS (INDICIES OF PARAMETERS)
GRIDLINES = 0
TAGS = 1
FX = 2
DIM_X = 3
DIM_Y = 4
SCREEN_W = 5
SCREEN_H = 6
CENTER_X = 7
CENTER_Y = 8
GRID_W = 9
GRID_H = 10
X_STEP = 11
Y_STEP = 12
TAG_COUNT = 13

#PARAMETERS (essentially global)
PARAM = [
    0, #GRIDLINES
    1, #TAGS
    0, #FX
    0, #DIM_X
    0, #DIM_Y
    1024, #SCREEN_W
    768, #SCREEN_H
    416, #CENTER_X
    384, #CENTER_Y
    720, #GRID_W
    720, #GRID_H
    90, #X_STEP
    90, #Y_STEP
    0,  #TAG_COUNT
]

def drawTiles(tileSurface, tileStateMatrix, tagImages, screen, bg):
    screen.fill((0,0,0))
    tileSurface = pygame.transform.scale(tileSurface,(PARAM[GRID_W],PARAM[GRID_H]))
    bg_scaled = pygame.transform.scale(bg,(PARAM[GRID_W],PARAM[GRID_H]))
    tileSurface.blit(bg_scaled,(0,0))

    for y in range(0, PARAM[DIM_Y]):
        for x in range(0, PARAM[DIM_X]):
            index = tileStateMatrix[y,x]
            if index != 0:
                tagIMG_scaled = pygame.transform.scale(tagImages[index],(PARAM[X_STEP],PARAM[Y_STEP]))
                tileSurface.blit(tagIMG_scaled,(x*PARAM[X_STEP],y*PARAM[Y_STEP]))

    # DRAW GRID LINES
    if PARAM[GRIDLINES]:
        for i in range(0,8):
            pygame.draw.line(tileSurface,(0,0,0),(i*PARAM[X_STEP],0),(i*PARAM[X_STEP],8*PARAM[Y_STEP]),3)
            pygame.draw.line(tileSurface,(0,0,0),(0,i*PARAM[Y_STEP]),(8*PARAM[X_STEP],i*PARAM[Y_STEP]),3)
        pygame.draw.line(tileSurface,(0,0,0),(8*PARAM[X_STEP]-1,0),(8*PARAM[X_STEP]-1,8*PARAM[Y_STEP]-1),3)
        pygame.draw.line(tileSurface,(0,0,0),(0,8*PARAM[Y_STEP]-1),(8*PARAM[X_STEP]-1,8*PARAM[Y_STEP]-1),3)
    screen.blit(tileSurface,(PARAM[CENTER_X] - PARAM[GRID_W]//2, PARAM[CENTER_Y] - PARAM[GRID_H]//2))

def loadAssets(fileName,tagList):
    #open config file
    config = open(fileName,"r")

    # read grid dimensions from config file
    PARAM[DIM_X] = int(config.readline())
    PARAM[DIM_Y] = int(config.readline())

    # read the tag count from config file
    PARAM[TAG_COUNT] = int(config.readline())

    # get the data for each tag from the config file
    for i in range(0, PARAM[TAG_COUNT]):
        line = config.readline()
        data = line.replace('\n','')
        tagID, tagIMG, tagSound = data.split(',')
        tagID = int(tagID)
        tag = [tagID, tagIMG, tagSound]
        tagList.append(list(tag))

    # get the background image filename
    bgIMG = config.readline()
    bgIMG = bgIMG.replace('\n','')

    # get the backgound music filename
    bgSound = config.readline()
    bgSound = bgSound.replace('\n','')

    return bgIMG, bgSound

def tagSearch(tagList, tagID):
    index = 0
    for i in tagList:
        if i[0] == tagID:
            return index
        index = index + 1

def updateTileMatrix(tileStateMatrix,objIDX,objPos_x,objPos_y):
    for y in range(0, PARAM[DIM_Y]):
        for x in range(0, PARAM[DIM_X]):
            if tileStateMatrix[y,x] == objIDX:
                tileStateMatrix[y,x] = 0
    tileStateMatrix[objPos_y,objPos_x] = objIDX

def initTileMatrix():
    tileStateMatrix = {}
    for x in range(0, PARAM[DIM_X]):
        for y in range(0,PARAM[DIM_Y]):
            tileStateMatrix[x,y] = 0
    return tileStateMatrix

##########################################################################################
#                                      START OF EXECUTION                                #
##########################################################################################
import pygame
import numpy
import serial

# set up serial port and variables for communication
CMD_UPDATE = b'\x00'
serPort = serial.Serial(port = "COM5", baudrate = 9600, timeout = 1)
serPort.flushOutput() 
serPort.flushInput() 
ID = 0
x = 0
y = 0

#Load parameters from config file
tagList = []
configFile = "rfgridConfig.txt"
bgIMG, bgSound = loadAssets(configFile,tagList)
tileStateMatrix = initTileMatrix()

#Initialize pygame
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

#create pygame screen
screen = pygame.display.set_mode((PARAM[SCREEN_W],PARAM[SCREEN_H]), pygame.FULLSCREEN)
screen.fill((0,0,0))

#load background image
bg = pygame.image.load(bgIMG)
tileSurface = pygame.Surface((PARAM[GRID_W],PARAM[GRID_H]), pygame.SRCALPHA, 32)
tileSurface = tileSurface.convert_alpha()

#load RFID tag images
tagImages = []
for i in range(0, PARAM[TAG_COUNT]):
    tagIMG = pygame.image.load(tagList[i][1])
    tagIMG = tagIMG.convert_alpha()
    tagImages.append(tagIMG)

#initialize the pygame sound mixer and play background music (looped)
pygame.mixer.init()
pygame.mixer.set_num_channels(PARAM[TAG_COUNT])
pygame.mixer.music.load(bgSound)
pygame.mixer.music.play(-1,0.0)

tagChannels = []  
for i in range(0, PARAM[TAG_COUNT]):
    tagChannels.append(pygame.mixer.Channel(int(i)))


#draw the play surface
drawTiles(tileSurface, tileStateMatrix, tagImages, screen, bg)

#Create additional game loop parameters
done = False
clock = pygame.time.Clock()

########################################################################
# GAME LOOP                                                            #
########################################################################
while not done:
    clock.tick(10)

    ################################################
    # Check the serial port
    ################################################
    if (serPort.inWaiting() > 0):
        if serPort.read(1) == CMD_UPDATE:
            ID = int.from_bytes(serPort.read(4), byteorder = 'big', signed = 0)
            x  = int.from_bytes(serPort.read(1), byteorder = 'big', signed = 0)
            y  = int.from_bytes(serPort.read(1), byteorder = 'big', signed = 0)
            objIDX = tagSearch(tagList,ID)
            updateTileMatrix(tileStateMatrix,objIDX,x,y)
            if(not tagChannels[objIDX].get_busy()):
                soundEffect = pygame.mixer.Sound(tagList[objIDX][2])
                tagChannels[objIDX].play(soundEffect)
                #soundEffect.play()
            drawTiles(tileSurface, tileStateMatrix, tagImages, screen, bg)
        ## OTHER COMMANDS CAN GO HERE ##########################


    ################################################
    # GAME EVENTS
    ################################################

    for event in pygame.event.get():
        # IF USER CLOSES THE WINDOW 
        if event.type == pygame.QUIT:
            done=True 

        # ESCAPE KEYPRESS
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done=True

        # DOWN ARROW WILL SHRINK THE PLAY AREA
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            PARAM[GRID_W] = int(PARAM[GRID_W] - 8)
            PARAM[GRID_H] = PARAM[GRID_W]
            PARAM[X_STEP] = int(PARAM[GRID_W]/8)
            PARAM[Y_STEP] = int(PARAM[GRID_H]/8)
            drawTiles(tileSurface, tileStateMatrix, tagImages, screen, bg)

        # UP ARROW WILL ENLARGE THE PLAY AREA
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            PARAM[GRID_W] = int(PARAM[GRID_W] + 8)
            PARAM[GRID_H] = PARAM[GRID_W]
            PARAM[X_STEP] = int(PARAM[GRID_W]/8)
            PARAM[Y_STEP] = int(PARAM[GRID_H]/8)
            drawTiles(tileSurface, tileStateMatrix, tagImages, screen, bg)

        # LEFT ARROW WILL PAN THE SCREEN LEFT
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            PARAM[CENTER_X] = PARAM[CENTER_X] - 8
            drawTiles(tileSurface, tileStateMatrix, tagImages, screen, bg)

        # RIGHT ARROW WILL PAN THE SCREEN RIGHT
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            PARAM[CENTER_X] = PARAM[CENTER_X] + 8
            drawTiles(tileSurface, tileStateMatrix, tagImages, screen, bg)

        # TYPING 'g' will turn on grid lines
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            PARAM[GRIDLINES] = not PARAM[GRIDLINES]
            drawTiles(tileSurface, tileStateMatrix, tagImages, screen, bg)

        # TYPING 'o' WILL SIMULATE A DETECTED OBJECT
        if event.type == pygame.KEYDOWN and event.key == pygame.K_o:           
            if PARAM[TAGS]:
                # REPLACE THIS WITH HARDWARE UPDATES 
                objPos_x = numpy.random.randint(0,8)
                objPos_y = numpy.random.randint(0,8)
                tagID = numpy.random.randint(100,110)
                objIDX = tagSearch(tagList,tagID)
                # THE REST WILL BE THE SAME
                updateTileMatrix(tileStateMatrix,objIDX,objPos_x,objPos_y)
                soundEffect = pygame.mixer.Sound(tagList[objIDX][2])
                soundEffect.play()
            drawTiles(tileSurface, tileStateMatrix, tagImages, screen, bg)

        # TYPING 'd' WILL TOGGLE TAG DISPLAY UPDATES
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            PARAM[TAGS] = not PARAM[TAGS]

         # 'c' WILL CLEAR THE SCREEN
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            tileStateMatrix = initTileMatrix()
            drawTiles(tileSurface, tileStateMatrix, tagImages, screen, bg)
    pygame.display.flip()
pygame.quit()
