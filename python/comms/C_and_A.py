





# 2019-10-03
# This code initializes a message and polls sending and receiving from
# the arduino. It is set to return nothing if 1s has passed. To be used
# in conjunction with SerialEvent-RW-example

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

# message values
A_UPDATE = b'\x00'
A_GETID = b'\x01'
A_GETXY = b'\x02'
A_BLOCK = b'\x03'
A_READID = b'\x04'
A_WRITEID = b'\x05'
A_READXY = b'\x06'
A_SYNC = b'\x0F'

P_UPDATE = b'\xF0'
P_GETID = b'\xF1'
P_GETXY = b'\xF2'
P_BLOCK = b'\xF3'
P_READID = b'\xF4'
P_WRITEID = b'\xF5'
P_READXY = b'\xF6'
P_SYNC = b'\xFF'

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

def parsecmd(cmd):
    ID = int(0)
    x = bytes(0)
    y = bytes(0)
    def recv_objectcord():
        # this subroutine is used for parsing the message structure [ID, x, y]
        nonlocal ID
        nonlocal x
        nonlocal y
        ID = int.from_bytes(serPort.read(4), byteorder = 'big', signed = 0)
        x  = int.from_bytes(serPort.read(1), byteorder = 'big', signed = 0)
        y  = int.from_bytes(serPort.read(1), byteorder = 'big', signed = 0)
        print("object " + str(ID) + " is now at (" + str(x) + ", " + str(y) + ")")
        
    if cmd == A_UPDATE:
        print("received an UPDATE msg from arduino")
        recv_objectcord()
        send_update()
    elif cmd == A_GETID:
        print("received a get ID msg from arduino")
        recv_objectcord()
        # update X,Y coord of obj ID
    elif cmd == A_GETXY:
        print("received a get XY msg from arduino")
        recv_objectcord()
        print("get xy: object " + str(ID) + " is now at (" + str(x) + ", " + str(y) + ")")
        # update X,Y coord of obj ID
    else:
        print("received unknown: " + str(cmd))

def send_update():
    objIDX = tagSearch(tagList,ID)
    updateTileMatrix(tileStateMatrix,objIDX,x,y)
    serPort.write(P_UPDATE)
    serPort.write(ID)
    serPort.write(x)
    serPort.write(y)
    print("ack sent for object " + str(ID) + " at (" + str(x) + ", " + str(y) + ")")

def send_getid(x, y):
    print("sent getid for object at " + str(x) +", " + str(y))
    x = bytes([x])
    y = bytes([y])
    print(str(P_GETID)+str(x)+str(y))
    serPort.write(P_GETID)
    serPort.write(x)
    serPort.write(y)

def send_getxy(ID):
    ID = ID.to_bytes(4, 'big')
    print("sent getxy for object " + str(ID))
    print(str(P_GETXY)+str(ID))
    serPort.write(P_GETXY)
    serPort.write(ID)
    
    
def Poll_Receive():
    while True:
        if (serPort.inWaiting() > 0):
            parsecmd()
            time.sleep(.1)                # Delay for one tenth of a second

def Main_func():
    while True:
        if (serPort.inWaiting() > 0):
            cmd = serPort.read(1)
            parsecmd(cmd)
        time.sleep(2)
        send_getid(0,0)
        #send_getxy(72)


##########################################################################################
#                                      START OF EXECUTION                                #
##########################################################################################
import serial
import time
import threading
import random
import binascii

# set up serial port and variables for communication
serPort = serial.Serial(port = 'COM14', baudrate = 9600, timeout = 1)
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

Main_func()

# set up main thread
#main = threading.Thread(target=Main_func)
#main.start()
# set up receiving thread
#poll = threading.Thread(target=Poll_Receive, daemon=True) 
#poll.start()
  

   

    
