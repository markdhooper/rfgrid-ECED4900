import time
import serial
import threading
import sys
import msvcrt

DEBUG = True
rfgridComms = True
COM_PORT = "COM6"

# message values
DEV_UPDATE = b'\x00'
DEV_GET_ID = b'\x01'
DEV_GET_XY = b'\x02'
DEV_BLOCK = b'\x03'
DEV_READ_ID = b'\x04'
DEV_WRITE_ID = b'\x05'
DEV_READ_XY = b'\x06'
DEV_SYNC = b'\x0F'

HOST_UPDATE = b'\xF0'
HOST_GET_ID = b'\xF1'
HOST_GET_XY = b'\xF2'
HOST_BLOCK = b'\xF3'
HOST_READ_ID = b'\xF4'
HOST_WRITE_ID = b'\xF5'
HOST_READ_XY = b'\xF6'
HOST_SYNC = b'\xFF'

ARG_SIZE = {
	"x":1,
	"y":1,
	"id":4,
	"off":2,
	"size":2,
	"begin":1,
	"x_max":1,
	"y_max":1,
	"num_readers":1,
	"arg":1,
	"data":-1
}

RX_FMT = [
	(DEV_UPDATE, 	0, ARG_SIZE["x"], 		ARG_SIZE["y"], 		ARG_SIZE["id"]),
	(DEV_GET_ID, 	1, ARG_SIZE["x"], 		ARG_SIZE["y"], 		ARG_SIZE["id"]),
	(DEV_GET_XY, 	2, ARG_SIZE["x"], 		ARG_SIZE["y"], 		ARG_SIZE["id"]),
	(DEV_BLOCK, 	3, ARG_SIZE["arg"], 	ARG_SIZE["id"]),
	(DEV_READ_ID, 	4, ARG_SIZE["id"], 		ARG_SIZE["off"], 	ARG_SIZE["size"], 	ARG_SIZE["data"]),
	(DEV_WRITE_ID, 	5, ARG_SIZE["id"], 		ARG_SIZE["off"], 	ARG_SIZE["size"]),
	(DEV_READ_XY, 	6, ARG_SIZE["x"], 		ARG_SIZE["y"], 		ARG_SIZE["id"], 	ARG_SIZE["off"], 	ARG_SIZE["data"]),
	(DEV_SYNC, 		7, ARG_SIZE["begin"], 	ARG_SIZE["num_readers"])
]



TX_FMT = [
	(HOST_UPDATE, 	0, ARG_SIZE["x"], 		ARG_SIZE["y"], 		ARG_SIZE["id"]),
	(HOST_GET_ID, 	1, ARG_SIZE["x"], 		ARG_SIZE["y"]),
	(HOST_GET_XY, 	2, ARG_SIZE["id"]),
	(HOST_BLOCK, 	3, ARG_SIZE["arg"], 	ARG_SIZE["id"]),
	(HOST_READ_ID, 	4, ARG_SIZE["id"], 		ARG_SIZE["off"], 	ARG_SIZE["size"]),
	(HOST_WRITE_ID, 5, ARG_SIZE["id"], 		ARG_SIZE["off"], 	ARG_SIZE["size"], 	ARG_SIZE["data"]),
	(HOST_READ_XY, 	6, ARG_SIZE["x"], 		ARG_SIZE["y"],		ARG_SIZE["off"], 	ARG_SIZE["size"]),
	(HOST_SYNC, 	7, ARG_SIZE["begin"], 	ARG_SIZE["x_max"],	ARG_SIZE["y_max"])
]


###############################################################################
#	TX FUNCTIONS
###############################################################################

# transmit formatted serial data to the rfgrid device
def tx_rfgrid(serPort, buf = []):
	print("TX <- RAW_BYTES: ", end = "")
	print(buf)
	serPort.write(buf)


# transmit an update acknowledgement message to the rfgrid device
def tx_update(serPort, x = 0, y = 0, id = 0):
	print("TX <- SYNC: ")


# transmit a get_id request to the rfgrid device
def tx_get_id(serPort, x = 0, y = 0):
	print("TX <- SYNC: ")


# transmit a get_xy request to the rfgrid device
def tx_get_xy(serPort, id):
	print("TX <- SYNC: ")


# transmit a block request to the rfgrid device
def tx_block(serPort, block = True, id = 0):
	print("TX <- SYNC: ")


# transmit a read_id request to the rfgrid device 
def tx_read_id(serPort, id):
	print("TX <- SYNC: ")


# transmit a write_id request to the rfgrid device
def tx_write_id(serPort,buf,id):
	print("TX <- SYNC: ")


# transmit a read_xy request to the rfgrid device
def tx_read_xy(serPort,x = 0,y = 0):
	print("TX <- SYNC: ")


# initiate/stop communication with rfgrid device 
def tx_sync(serPort, begin = 1, x_max = 8, y_max = 8):
	print("TX <- SYNC: begin=%d, x_max=%d, y_max=%d" % (begin,x_max,y_max))
	buf = HOST_SYNC + serial.to_bytes([begin,x_max,y_max])
	tx_rfgrid(serPort, buf)

###############################################################################
#	RX FUNCTIONS
###############################################################################
def rx_rfgrid(rx_buf):
	cmdIdx = -1;
	# read in the command byte from the serial buffer
	cmd = rx_buf.read(1)
	# search the RX_FMT list for an entry that matches the command byte
	for cmdType in RX_FMT:
		if cmdType[0] == cmd:
			# Match found, begin extraction of arguments according to RX_FMT list entry
			# and save the index in order to call the correct function upon return
			args = []
			cmdIdx = cmdType[1];
			for i in range(2,len(cmdType)):
				if(cmdType[i] != -1):
					#just read the pre-defined number of bytes
					arg = rx_buf.read(cmdType[i])
				else:
					#read in the number of bytes defined by the 
					#size argument (the current value of arg)
					arg = rx_buf.read(arg)
				# add the argument to the args list
				args.append(arg)
			break
	return cmdIdx, args #return both the command byte and the list of arguments

def rx_update(args):
	x = int.from_bytes(args[0], byteorder = 'big', signed = 0)
	y  = int.from_bytes(args[1], byteorder = 'big', signed = 0)
	id  = int.from_bytes(args[2], byteorder = 'big', signed = 0)
	print("\nRX -> UPDATE: x=%d, y=%d, id=%d" % (x,y,id))
	
def rx_get_id(args):
	print("\nRX -> GET_ID: ")

def rx_get_xy(args):
	print("\nRX -> GET_XY: ")

def rx_block(args):
	print("\nRX -> BLOCK: ")
	
def rx_read_id(args):
	print("\nRX -> READ_ID: ")
	
def rx_write_id(args):
	print("\nRX -> WRITE_ID: ")
	
def rx_read_xy(args):
	print("\nRX -> READ_XY: ")
	
def rx_sync(args):
	begin = int.from_bytes(args[0], byteorder = 'big', signed = 0)
	max_readers = int.from_bytes(args[1], byteorder = 'big', signed = 0)
	print("\nRX -> SYNC: begin=%d, max_readers=%d" % (begin, max_readers))

RX_LUT = {
	"RX_UPDATE"		: rx_update,
	"RX_GET_ID"		: rx_get_id,
	"RX_GET_XY"		: rx_get_xy,
	"RX_BLOCK"		: rx_block,
	"RX_READ_ID"	: rx_read_id,
	"RX_WRITE_ID"	: rx_write_id,
	"RX_READ_XY"	: rx_read_xy,
	"RX_SYNC"		: rx_sync
}

RX_LUT_KEYS = [
	"RX_UPDATE",
	"RX_GET_ID",
	"RX_GET_XY",
	"RX_BLOCK",
	"RX_READ_ID",
	"RX_WRITE_ID",
	"RX_READ_XY",
	"RX_SYNC"
]


TX_LUT = {
	"TX_UPDATE"		: tx_update,
	"TX_GET_ID"		: tx_get_id,
	"TX_GET_XY"		: tx_get_xy,
	"TX_BLOCK"		: tx_block,
	"TX_READ_ID"	: tx_read_id,
	"TX_WRITE_ID"	: tx_write_id,
	"TX_READ_XY"	: tx_read_xy,
	"TX_SYNC"		: tx_sync
}

TX_LUT_KEYS = [
	"TX_UPDATE",
	"TX_GET_ID",
	"TX_GET_XY",
	"TX_BLOCK",
	"TX_READ_ID",
	"TX_WRITE_ID",
	"TX_READ_XY",
	"TX_SYNC"
]


def TXMENU(serPort):
	print("COMMUNICATION PROTOCOL TESTING:")
	print("     OPTIONS:")
	print("			1: TX_UPDATE"     )
	print("			2: TX_GET_ID"     )
	print("			3: TX_GET_XY"     )
	print("			4: TX_BLOCK"      )
	print("			5: TX_READ_ID"    )
	print("			6: TX_WRITE_ID"   )
	print("			7: TX_READ_XY"    )
	print("			8: TX_SYNC"       )
	selection = input("select an option:")
	
	if selection == '1':
		#x
		#y
		#id
		tx_update(serPort, x = 0, y = 0, id = 0)
	elif selection == '2':
		#x
		#y
		tx_get_id(serPort, x = 0, y = 0)
	elif selection == '3':
		#id
		tx_get_xy(serPort, id)
	elif selection == '4':
		#block
		#id
		tx_block(serPort, block = True, id = 0)
	elif selection == '5':
		#id
		tx_read_id(serPort, id)
	elif selection == '6':
		#buf
		#id
		tx_write_id(serPort,buf,id)
	elif selection == '7':
		#x
		#y
		tx_read_xy(serPort,x = 0,y = 0)
	elif selection == '8':
		#begin
		#x_max
		#y_max
		tx_sync(serPort, begin = 1, x_max = 8, y_max = 8)
		
	
	##PUT YOUR CODE HERE CATHY

###############################################################################
# Setup 
###############################################################################
serPort = serial.Serial(port = COM_PORT, baudrate = 9600, timeout = 1)
serPort.flushOutput()
serPort.flushInput()

print("RFGRID COMMUNICATION PROTOCOL TESTER:")
print("\t Press 'Enter' at any time to send a message.")
print("\t( a SYNC message must be sent to begin communication with the device )")

###############################################################################
# Loop
###############################################################################
while rfgridComms:
	if (serPort.inWaiting() > 0):
		# there is data in the serial buffer
		# extract the command byte, and the arguments from the buffer
		cmdIdx, args = rx_rfgrid(serPort)
		RX_LUT[RX_LUT_KEYS[cmdIdx]](args)
	
	#no data on serial.. output a "." to the console
	msvcrt.putch('.'.encode())

	#keystroke detected, output a newline character and display TX Menu
	if msvcrt.kbhit():
		msvcrt.getch()
		msvcrt.putch("\n".encode())
		TXMENU(serPort)
	
	time.sleep(0.4)
	