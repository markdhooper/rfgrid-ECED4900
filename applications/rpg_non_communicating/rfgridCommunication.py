import serial.tools.list_ports
from rfgrid import *
from time import sleep

def rfgridCommInit(x_max,y_max):
	global rfgridSerial
	ports = list(serial.tools.list_ports.comports())
	for p in ports:
		if "Arduino" in p[1]:
			COM_PORT = p[0]
			rfgridSerial = serial.Serial(port = COM_PORT, baudrate = 9600, timeout = 1)
			rfgridSerial.flushOutput()
			rfgridSerial.flushInput()
			print("Device detected on %s" % COM_PORT)
			sleep(5)
			tx_sync(rfgridSerial,1,x_max,y_max)
			return rfgridSerial
			
###############################################################################
# Communication Protocols 
###############################################################################
# Command Types
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
	(DEV_UPDATE, 	0, ARG_SIZE["id"], 		ARG_SIZE["x"], 		ARG_SIZE["y"]),
	(DEV_GET_ID, 	1, ARG_SIZE["id"], 		ARG_SIZE["x"], 		ARG_SIZE["y"]),
	(DEV_GET_XY, 	2, ARG_SIZE["id"], 		ARG_SIZE["x"], 		ARG_SIZE["y"]),
	(DEV_BLOCK, 	3, ARG_SIZE["id"], 		ARG_SIZE["arg"]),
	(DEV_READ_ID, 	4, ARG_SIZE["id"], 		ARG_SIZE["off"], 	ARG_SIZE["size"], 	ARG_SIZE["data"]),
	(DEV_WRITE_ID, 	5, ARG_SIZE["id"], 		ARG_SIZE["off"], 	ARG_SIZE["size"]),
	(DEV_READ_XY, 	6, ARG_SIZE["id"], 		ARG_SIZE["x"], 		ARG_SIZE["y"], 		ARG_SIZE["off"], 	ARG_SIZE["size"], ARG_SIZE["data"]),
	(DEV_SYNC, 		7, ARG_SIZE["begin"], 	ARG_SIZE["x_max"], 	ARG_SIZE["y_max"] )
]



TX_FMT = [
	(HOST_UPDATE, 	0, ARG_SIZE["id"], 		ARG_SIZE["x"], 		ARG_SIZE["y"]),
	(HOST_GET_ID, 	1, ARG_SIZE["x"], 		ARG_SIZE["y"]),
	(HOST_GET_XY, 	2, ARG_SIZE["id"]),
	(HOST_BLOCK, 	3, ARG_SIZE["id"], 	    ARG_SIZE["arg"]),
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
def tx_update(serPort, id = 0, x = 0, y = 0):
	print("TX <- UPDATE: id=%d, x=%d, y=%d" % (id,x,y))
	buf = HOST_UPDATE + id.to_bytes(4,"big",signed = False) + serial.to_bytes([x,y])
	tx_rfgrid(serPort,buf)

# transmit a get_id request to the rfgrid device
def tx_get_id(serPort, x = 0, y = 0):
	print("TX <- GET_ID: x=%d, y=%d" % (x,y))
	buf = HOST_GET_ID + serial.to_bytes([x,y])
	tx_rfgrid(serPort,buf)


# transmit a get_xy request to the rfgrid device
def tx_get_xy(serPort, id):
	print("TX <- GET_XY: id=%d" % id)
	buf = HOST_GET_XY + id.to_bytes(4,"big",signed = False)
	tx_rfgrid(serPort,buf)

# transmit a block request to the rfgrid device
def tx_block(serPort, id, block):
	print("TX <- BLOCK: id=%d, block=%d" % (id,block))
	buf = HOST_BLOCK + id.to_bytes(4,"big",signed = False) + serial.to_bytes([block])
	tx_rfgrid(serPort,buf)

# transmit a read_id request to the rfgrid device 
def tx_read_id(serPort, id, ofs, size):
	print("TX <- READ_ID: id=%d, offset=%d, size=%d" % (id,ofs,size))
	buf = HOST_READ_ID + serial.to_bytes([id,ofs,size])
	tx_rfgrid(serPort,buf)

# transmit a write_id request to the rfgrid device
def tx_write_id(serPort,id,ofs,size,data):
	print("TX <- WRITE_ID: id=%d, offset=%d, size=%d, data=%x" % (id,ofs,size,data))
	buf = HOST_WRITE_ID + serial.to_bytes([id,ofs,size,data])
	tx_rfgrid(serPort,buf)
	
# transmit a read_xy request to the rfgrid device
def tx_read_xy(serPort, x, y, ofs, size):
	print("TX <- READ_XY: id=%d, offset=%d, size=%d" % (x,y,ofs,size))
	buf = HOST_READ_ID + serial.to_bytes([x,y,ofs,size])
	tx_rfgrid(serPort,buf)
	
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
	args = []
	# read in the command byte from the serial buffer
	cmd = rx_buf.read(1)
	# search the RX_FMT list for an entry that matches the command byte
	for cmdType in RX_FMT:
		if cmdType[0] == cmd:
			# Match found, begin extraction of arguments according to RX_FMT list entry
			# and save the index in order to call the correct function upon return
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

def rx_update(args,rfgrid):
	id = int.from_bytes(args[0], byteorder = 'big', signed = 0)
	x  = int.from_bytes(args[1], byteorder = 'big', signed = 0)
	y  = int.from_bytes(args[2], byteorder = 'big', signed = 0)
	print("\nRX -> UPDATE: id=%d, x=%d, y=%d" % (id,x,y))
	tx_update(rfgridSerial, id, x, y)
	index = tagSearch(rfgrid.tags,id)
	if index != -1:
		rfgrid.updateGridTiles(x,y,index)
		rfgrid.draw()
	
def rx_get_id(args,rfgrid):
	id = int.from_bytes(args[0], byteorder = 'big', signed = 0)
	x  = int.from_bytes(args[1], byteorder = 'big', signed = 0)
	y  = int.from_bytes(args[2], byteorder = 'big', signed = 0)
	print("\nRX -> GET_ID: id=%d, x=%d, y=%d" % (id,x,y))

def rx_get_xy(args,rfgrid):
	id = int.from_bytes(args[0], byteorder = 'big', signed = 0)
	x  = int.from_bytes(args[1], byteorder = 'big', signed = 0)
	y  = int.from_bytes(args[2], byteorder = 'big', signed = 0)
	print("\nRX -> GET_XY: id=%d, x=%d, y=%d" % (id,x,y))

def rx_block(args,rfgrid):
	id = int.from_bytes(args[0], byteorder = 'big', signed = 0)
	arg = int.from_bytes(args[1], byteorder = 'big', signed = 0)
	print("\nRX -> BLOCK: id=%d, arg=%d" % (id,arg))
	
def rx_read_id(args,rfgrid):
	print("\nRX -> READ_ID: ")
	
def rx_write_id(args,rfgrid):
	print("\nRX -> WRITE_ID: ")
	
def rx_read_xy(args,rfgrid):
	print("\nRX -> READ_XY: ")
	
def rx_sync(args,rfgrid):
	begin = int.from_bytes(args[0], byteorder = 'big', signed = 0)
	x_max = int.from_bytes(args[1], byteorder = 'big', signed = 0)
	y_max = int.from_bytes(args[2], byteorder = 'big', signed = 0)
	print("\nRX -> SYNC: begin=%d, x_max=%d, y_max=%d" % (begin,x_max,y_max))

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
	