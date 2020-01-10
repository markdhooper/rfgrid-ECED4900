from time import sleep
import serial

filename = "tags.txt"
tagFile = open(filename,'w')
userInput = input("Tag Scanner: ('s' start, 'q' quit):")
startMenu = True
while startMenu:
        if userInput == "q":
            tagFile.close()
            exit()
        elif userInput == "s":
            print("Initializing Grid: Please Wait")
            startMenu = False
        else:
            print("\tInvalid Selection")
            userInput = input("Tag Scanner: ('s' start, 'q' quit):")

ID = 0
x = 0
y = 0

CMD_UPDATE = b'\x00'
serPort = serial.Serial(port = "COM3", baudrate = 9600, timeout = 1)
serPort.flushOutput() 
serPort.flushInput() 
done = False
scan = False
scannedx, scannedy = 0,0

while not done:
    if scan:
        if serPort.read(1) == CMD_UPDATE:
            ID = int.from_bytes(serPort.read(4),byteorder = "big", signed = 0)
            x = int.from_bytes(serPort.read(1),byteorder = 'big')
            y = int.from_bytes(serPort.read(1),byteorder = 'big')
            if ID != 0:
                print("TAG FOUND: ID: "+ str(hex(ID))+ " (" + str(hex(x)) + "," + str(hex(y)) + ")")
                tagFile.write(str(ID) + ' ' + str(x) + ' ' + str(y) + '\n')
                scannedx = x
                scannedy = y
                print("Tag ID stored as: " + str(ID) + ' ' + str(x) + ' ' + str(y))
            else:
                print("Tag Removal Detected " + str(hex(ID))+ " (" + str(hex(x)) + "," + str(hex(y)) + ")")
                scan = False
    else:
        userInput = input("Ready:  ('s' scan, 'q' quit):")
        if userInput == "q":
            tagFile.close()
            exit()
        elif userInput == "s":
            scan = True
    sleep(0.1)