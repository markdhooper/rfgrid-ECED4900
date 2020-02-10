/*****************************************************************************/
/* Program Name:  rfgrid.ino  (https://github.com/markdhooper/rfgridECED4900)*/
/* Programmer:    Mark Hooper (https://github.com/markdhooper)               */
/* Description:   This program is intended for use with an Arduino UNO       */
/*                microcontroller connected via usb to a host machine        */
/*                running a python script at the repository linked above.    */
/*                You will also require an rfgridShield and at least one     */
/*                rfgrid modular array unit. For more information, please    */
/*                see the github repo linked above.                          */
/* Behavior:      This sketch will determine how many readers are connected. */
/*                and will inform the host machine when it detects an rfid   */
/*                tag. The current protocol is only 1-way at present.        */
/*****************************************************************************/

#include <SPI.h>
#include <MFRC522.h> //https://github.com/miguelbalboa/rfid

/*****************************************************************************/
/* Constants */
/*****************************************************************************/

/* Pin Assignments */
#define S0_PIN 2    
#define S1_PIN 3    
#define S2_PIN 4    
#define S3_PIN 5    
#define S4_PIN 6    
#define S5_PIN 7    
#define S6_PIN 8    
#define S7_PIN 9    
#define SDA_PIN 10  
#define SCK_PIN 13  
#define MOSI_PIN 11 
#define MISO_PIN 12 
#define RST_PIN 14  
#define NOT_EN_PIN 6

/* Additional Constants */
#define UPDATE_MSG_SZ 7
#define TRIAL_THRESHOLD 1
#define READER_LIMIT 256
#define BANK_MAX 16
#define READER_MAX 16
#define BLOCKED_TAG_MAX 16
#define BOARD_CONFIG4x4   0b0000000000000001
#define BOARD_CONFIG8x8   0b0000000000110011
#define BOARD_CONFIG12x12 0b0000011101110111
#define BOARD_CONFIG16x16 0b1111111111111111

/*****************************************************************************/
/* Data Structures */
/*****************************************************************************/
union readerLocation {
    uint8_t addr8;
    struct BR
	{
        uint8_t readerID : 4;
        uint8_t bankID : 4;
    }addr4;
    struct ydxdymxm
	{
        uint8_t xmod : 2;
        uint8_t ymod : 2;
        uint8_t xdiv : 2;
        uint8_t ydiv : 2;
    }xy;
  struct ab
  {
    uint8_t ar0 : 1;
    uint8_t ar1 : 1;
    uint8_t ar2 : 1;
    uint8_t ar3 : 1;
    uint8_t ab0 : 1;
    uint8_t ab1 : 1;
    uint8_t ab2 : 1;
    uint8_t ab3 : 1;
  }addrBit;
};

union intUID 
{
  byte uidArr[4];
  uint32_t UID;
};

struct flg
{
	uint8_t ACK : 1;
	uint8_t BLOCK : 1;
	uint8_t reserved : 6;
};


struct Tile
{
  uint32_t UID;
  struct flg FLAGS;
};



/*****************************************************************************/
/* Communication Protocol Defines */
/*****************************************************************************/
#define RX_UPDATE_BYTES 6       //x,y,id
#define RX_GET_ID_BYTES 2       //x,y
#define RX_GET_XY_BYTES 4       //id
#define RX_BLOCK_BYTES 5        //arg, id
#define RX_READ_ID_BYTES 8      //id, offset, size
#define RX_WRITE_ID_BYTES 8     // id, offset, size (DATA)
#define RX_READ_XY_BYTES 6      // x, y, offset, size
#define RX_SYNC_BYTES 3         // begin, xmax, ymax

#define TX_UPDATE_BYTES 7       // CMD, x,y,id
#define TX_GET_ID_BYTES 7       // CMD, x,y,id
#define TX_GET_XY_BYTES 7       // CMD, x,y,id
#define TX_BLOCK_BYTES 6        // CMD, arg, id
#define TX_READ_ID_BYTES 9      // CMD, id, offset, size, (DATA)
#define TX_WRITE_ID_BYTES 9     // CMD, id, offset, size
#define TX_READ_XY_BYTES 11      // CMD, x, y, id, offset, size (DATA)
#define TX_SYNC_BYTES 4         // CMD, begin, x_max, y_max

/*****************************************************************************/
/* Global Variables */
/*****************************************************************************/
union intUID objID;
struct Tile Tiles[READER_LIMIT];
MFRC522 Reader(SDA_PIN, RST_PIN);
int ReaderCount = 0;
uint16_t boardMask = 0xFFFF;
uint8_t boardSequence[16] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
uint8_t boardSeqLen = 0;
uint32_t blockedTags[BLOCKED_TAG_MAX];
int BLOCKS_IN_EFFECT = 0;
bool SYNC = 0;
uint8_t x_max_global = 0;
uint8_t y_max_global = 0;


/*****************************************************************************/
/* These automatically get called based on the CMD byte read in the loop()   */
/*****************************************************************************/
void RX_UPDATE()
{
	uint8_t x, y;
	intUID rx_id;
	
	byte argBytes[RX_UPDATE_BYTES];
	Serial.readBytes(argBytes,RX_UPDATE_BYTES);
	
	x = argBytes[4]; 
	y = argBytes[5]; 
	rx_id.uidArr[0] = argBytes[3];
	rx_id.uidArr[1] = argBytes[2]; 
	rx_id.uidArr[2] = argBytes[1]; 
	rx_id.uidArr[3] = argBytes[0]; 
	
	//host has acknowledged an update sent by the device
	//clear the ACK flag for the corresponding reader
	uint8_t addr;
	XYToAddr(x,y,addr);
	if(Tiles[addr].UID == rx_id.UID)
	{
		Tiles[addr].FLAGS.ACK = 0;
	}

}

void RX_GET_ID()
{
	uint8_t x, y;
	uint32_t id;
	
	byte argBytes[RX_GET_ID_BYTES];
	Serial.readBytes(argBytes,RX_GET_ID_BYTES);
	
	x = argBytes[0];
	y = argBytes[1];
	
	uint8_t addr;
	XYToAddr(x,y,addr);
	id = Tiles[addr].UID;
	
	//transmit the result
	TX_GET_ID(id, x, y);
  
}

void RX_GET_XY()
{
	uint8_t x = 255; 
	uint8_t y = 255;
	intUID id;
	
	byte argBytes[RX_GET_XY_BYTES];
	Serial.readBytes(argBytes,RX_UPDATE_BYTES);
	
	id.uidArr[0] = argBytes[3];
	id.uidArr[1] = argBytes[2];
	id.uidArr[2] = argBytes[1];
	id.uidArr[3] = argBytes[0];
       
	union readerLocation addr;
	for(int i = 0; i < boardSeqLen; i++)
	{
		addr.addr4.bankID = boardSequence[i];
		for(int j = 0; j < 16; j++)
		{
			addr.addr4.readerID = (uint8_t)j;
			
			if(Tiles[addr.addr8].UID == id.UID)
			{
				addrToXY(addr.addr8,x,y);
			}
		}
	}
	
	//transmit the result
	TX_GET_XY(id.UID,x,y);
}

void RX_BLOCK()
{
	uint8_t arg;
	intUID id;
  
	byte argBytes[RX_BLOCK_BYTES];
	Serial.readBytes(argBytes,RX_BLOCK_BYTES);  

    id.uidArr[0] = argBytes[3];
    id.uidArr[1] = argBytes[2];
    id.uidArr[2] = argBytes[1];
    id.uidArr[3] = argBytes[0];
    arg = argBytes[4];

  if(id.UID == 0){
    arg = 0;
    TX_BLOCK(id.UID,arg);
    return;
  }
  
  if(arg)
  {
	  //host wants us to block updates from this UID
	  for(int i = 0; i < BLOCKED_TAG_MAX; i++)
	  {
		  if(!blockedTags[i])
		  {
			  //we found a free slot, store the ID of the tag to block
			  blockedTags[i] = id.UID;
			  BLOCKS_IN_EFFECT++;
        for(int j = 0; j< READER_LIMIT; j++)
        {
          if(Tiles[j].UID == id.UID)
          {
            Tiles[j].FLAGS.BLOCK = 1;
            Tiles[j].FLAGS.ACK = 0;
            break;  
          }
        }
        break;
		  }
		  else if(i == BLOCKED_TAG_MAX -1)
		  {
			  //We can't block this tag until they unblock another one
			  arg = 0;
		  }
	  }
  }
  else
  {
	  //they want to unblock a tag
	  for(int i = 0; i < BLOCKED_TAG_MAX; i++)
	  {
		  if(blockedTags[i] == id.UID)
		  {
			  //we found a match
			  blockedTags[i] = 0;
			  BLOCKS_IN_EFFECT--;
        //Search for a reader with an id that matches our blocked tag
        // and clear the flag
        for(int j = 0; j< READER_LIMIT; j++)
        {
          if(Tiles[j].UID == id.UID)
          {
            //we found a match, unblock 
            //the reader. And ensure that
            //it tells the host where the
            //newely unblocked tag is.
            Tiles[j].FLAGS.BLOCK = 0;
            Tiles[j].FLAGS.ACK = 1;
            break;  
          }
        }
        break;
		  }
	  }
  }

  //transmit the result
  TX_BLOCK(id.UID,arg);
}

void RX_READ_ID()
{
  intUID id;
  uint16_t ofs;
  uint16_t sz;
  byte data[16];    //FIXED SIZES WILL BE NEEDED, WE CAN PICK A MAXIMUM (FOR NOW) OF 16
  
  byte argBytes[RX_READ_ID_BYTES];
  Serial.readBytes(argBytes,RX_UPDATE_BYTES);

  //do the things

  /*****************************************************************************/
  /* HARD CODED - ONLY FOR TESTING, THE REAL VALUES WILL NEED TO BE COMPUTED   */
              id.uidArr[0] = argBytes[3];
              id.uidArr[1] = argBytes[2];
              id.uidArr[2] = argBytes[1];
              id.uidArr[3] = argBytes[0];
              ofs = argBytes[4] + (argBytes[5]<<8);
              sz = 16;  //going with a fixed size for now....
  /*****************************************************************************/

  //transmit the result
  TX_READ_ID(id.UID, ofs, sz, data);
}

void RX_WRITE_ID()
{
  intUID id;
  uint16_t ofs;
  uint16_t sz;
  
  byte argBytes[RX_WRITE_ID_BYTES];
  Serial.readBytes(argBytes,RX_UPDATE_BYTES);

  //do the things

  /*****************************************************************************/
  /* HARD CODED - ONLY FOR TESTING, THE REAL VALUES WILL NEED TO BE COMPUTED   */
              id.uidArr[0] = argBytes[3];
              id.uidArr[1] = argBytes[2];
              id.uidArr[2] = argBytes[1];
              id.uidArr[3] = argBytes[0];
              ofs = argBytes[5] + (argBytes[4]<<8);
              sz = argBytes[7] + (argBytes[6]<<8);
  /*****************************************************************************/

  //transmit the result
  TX_WRITE_ID(id.UID, ofs, sz);
}

void RX_READ_XY()
{
  uint8_t x;
  uint8_t y;
  uint32_t id;
  uint16_t ofs;
  uint16_t sz;
  
  byte argBytes[RX_READ_XY_BYTES];
  Serial.readBytes(argBytes,RX_UPDATE_BYTES);  

  //do the things


  /**********************************************************************/
  /* HARDCODED ONLY FOR TESTING, these values will need to be computed  */
          x = argBytes[0];
          y = argBytes[1];
          id = 0xBEEF;
          ofs = (argBytes[2]<<8) + argBytes[3];
          sz = (argBytes[4]<<8) + argBytes[5];
          byte data[sz];
  /**********************************************************************/
  
  //transmit the result
  TX_READ_XY(x, y, id, ofs, sz, data);
}

void RX_SYNC()
{
	uint8_t arg;
	uint8_t x_max;
	uint8_t y_max;
	
	byte argBytes[RX_SYNC_BYTES];
	Serial.readBytes(argBytes,RX_SYNC_BYTES);
	

	arg = argBytes[0];
  x_max = argBytes[1];
  y_max = argBytes[2];
  
	if(!arg){
		//host wants to stop communicating
		SYNC = false;
	}else if(x_max_global == x_max && y_max_global == y_max){
    SYNC = true;
	}else{
	  arg = 0;
    x_max = x_max_global;
    y_max = y_max_global;
	}
	
	//transmit the result
	TX_SYNC(arg,x_max,y_max);
}


/*****************************************************************************/
/* Call these when you want to transmit a specific response to the Host      */
/*****************************************************************************/

void TX_UPDATE(uint32_t id, uint8_t x, uint8_t y )
{
    intUID temp;
    temp.UID = id;
    uint8_t buf[TX_UPDATE_BYTES];
    buf[0] = 0x00;        //UPDATE COMMAND
    buf[1] = temp.uidArr[3];
    buf[2] = temp.uidArr[2];
    buf[3] = temp.uidArr[1];
    buf[4] = temp.uidArr[0];
    buf[5] =  x;
    buf[6] =  y;
    Serial.write(buf, TX_UPDATE_BYTES);
}

void TX_GET_ID(uint32_t id, uint8_t x, uint8_t y)
{
    intUID temp;
    temp.UID = id;
    uint8_t buf[TX_GET_ID_BYTES];
    buf[0] = 0x01;        //GET_ID COMMAND
    buf[1] = temp.uidArr[3];
    buf[2] = temp.uidArr[2];
    buf[3] = temp.uidArr[1];
    buf[4] = temp.uidArr[0];
    buf[5] =  x;
    buf[6] =  y;
    Serial.write(buf, TX_GET_ID_BYTES);
}

void TX_GET_XY(uint32_t id, uint8_t x, uint8_t y)
{
    intUID temp;
    temp.UID = id;
    uint8_t buf[TX_GET_XY_BYTES];
    buf[0] = 0x02;        //GET_XY COMMAND
    buf[1] = temp.uidArr[3];
    buf[2] = temp.uidArr[2];
    buf[3] = temp.uidArr[1];
    buf[4] = temp.uidArr[0];
    buf[5] =  x;
    buf[6] =  y;
    Serial.write(buf, TX_GET_XY_BYTES);
}

void TX_BLOCK(uint32_t id, uint8_t arg)
{
    intUID temp;
    temp.UID = id;
    uint8_t buf[TX_BLOCK_BYTES];
    buf[0] = 0x03;        //BLOCK COMMAND
    buf[1] = temp.uidArr[3];
    buf[2] = temp.uidArr[2];
    buf[3] = temp.uidArr[1];
    buf[4] = temp.uidArr[0];
    buf[5] =  arg;
    Serial.write(buf, TX_BLOCK_BYTES);
}

void TX_READ_ID(uint32_t id, uint16_t ofs, uint16_t sz, byte* data)
{
    intUID temp;
    temp.UID = id;
    uint8_t buf[TX_READ_ID_BYTES + sz];
    buf[0] = 0x04;        //READ_ID COMMAND
    buf[1] = temp.uidArr[3];
    buf[2] = temp.uidArr[2];
    buf[3] = temp.uidArr[1];
    buf[4] = temp.uidArr[0];
    buf[5] = (ofs & 0xFF00)>>8;
    buf[6] = (ofs & 0x00FF);
    buf[7] = (sz & 0xFF00)>>8;
    buf[8] = (sz & 0x00FF);
    for(int i = 0; i < sz; i++)
    {
      buf[i+8] = *data;
      data++; 
    }
    Serial.write(buf, TX_READ_ID_BYTES + sz);
}

void TX_WRITE_ID(uint32_t id, uint16_t ofs, uint16_t sz)
{
    intUID temp;
    temp.UID = id;
    uint8_t buf[TX_READ_XY_BYTES];
    buf[0] = 0x05;        //WRITE_ID COMMAND
    buf[1] = temp.uidArr[3];
    buf[2] = temp.uidArr[2];
    buf[3] = temp.uidArr[1];
    buf[4] = temp.uidArr[0];
    buf[5] = (ofs & 0xFF00)>>8;
    buf[6] = (ofs & 0x00FF);
    buf[7] = (sz & 0xFF00)>>8;
    buf[8] = (sz & 0x00FF);
    Serial.write(buf, TX_WRITE_ID_BYTES + sz);
}

void TX_READ_XY(uint8_t x, uint8_t y,uint32_t id, uint16_t ofs, uint16_t sz, byte* data)
{
    intUID temp;
    temp.UID = id;
    uint8_t buf[TX_READ_XY_BYTES + sz];
    buf[0] = 0x06;        //READ_XY COMMAND
    buf[1] = x;
    buf[2] = y;
    buf[3] = temp.uidArr[3];
    buf[4] = temp.uidArr[2];
    buf[5] = temp.uidArr[1];
    buf[6] = temp.uidArr[0];
    buf[7] = (ofs & 0xFF00)>>8;
    buf[8] = (ofs & 0x00FF);
    buf[9] = (sz & 0xFF00)>>8;
    buf[10] = (sz & 0x00FF);
    for(int i = 0; i < sz; i++)
    {
      buf[i+10] = *data;
      data++; 
    }
    Serial.write(buf, TX_READ_XY_BYTES + sz);
}

void TX_SYNC(uint8_t arg, uint8_t x_max, uint8_t y_max)
{
  uint8_t buf[TX_SYNC_BYTES] = {0x0F, arg, x_max, y_max};
  Serial.write(buf, TX_SYNC_BYTES);
}


/*****************************************************************************/
/* Lookup table: the CMD is bitwise anded with 0x07 which gives the index of */
/* the function to call                                                      */
/*****************************************************************************/
void (*RX_LUT[])() = 
{
  RX_UPDATE,
  RX_GET_ID,
  RX_GET_XY,
  RX_BLOCK,
  RX_READ_ID,
  RX_WRITE_ID,
  RX_READ_XY,
  RX_SYNC
}; 


/*****************************************************************************/
/* Functions: (SPI communication, and address translation) */
/*****************************************************************************/

/* Output an 8-bit address to the SPI MUX */
void outputAddress(uint8_t addr)
{
  union readerLocation readerAddr;
  readerAddr.addr8 = addr;
  digitalWrite(S0_PIN, readerAddr.addrBit.ar0);
  digitalWrite(S1_PIN, readerAddr.addrBit.ar1);
  digitalWrite(S2_PIN, readerAddr.addrBit.ar2);
  digitalWrite(S3_PIN, readerAddr.addrBit.ar3);
  digitalWrite(S4_PIN, readerAddr.addrBit.ab0);
  digitalWrite(S5_PIN, readerAddr.addrBit.ab1);
  digitalWrite(S6_PIN, readerAddr.addrBit.ab2);
  digitalWrite(S7_PIN, readerAddr.addrBit.ab3);
}

/* Tests if a reader is present at a given address */
bool initReader(uint8_t addr)
{
  bool result;
  outputAddress(addr);
  delay(10);
  Reader.PCD_Init();
  int numTrials = 0;
  int gainTest = 16;
  for(int j = 0; j < TRIAL_THRESHOLD; j++)
  {
    Reader.PCD_SetAntennaGain(gainTest);
    if(Reader.PCD_GetAntennaGain() == gainTest)
	{
      numTrials++;
    }
  }
  Reader.PCD_AntennaOff();  
  return (numTrials == TRIAL_THRESHOLD);
}
/*****************************************************************************/
//                                                                                       DELETE LATER
/*  */
void sendUpdate(uint8_t addr, uint32_t ID)
{
  union intUID tagID;
  tagID.UID = ID;
  uint8_t msg[UPDATE_MSG_SZ];
  msg[0] = 0;
  msg[1] = tagID.uidArr[3];
  msg[2] = tagID.uidArr[2];
  msg[3] = tagID.uidArr[1];
  msg[4] = tagID.uidArr[0];
  addrToXY(addr,msg[5],msg[6]);
  Serial.write(msg,UPDATE_MSG_SZ);
}

/* Translates an x,y coordinate to an address */
int XYToAddr(byte x, byte y, byte &addr)
{
    union readerLocation RL;
    if((x > 15) || (y > 15)) return 1;
    RL.xy.xmod = x % 4;
    RL.xy.ymod = y % 4;
    RL.xy.xdiv = x/4;
    RL.xy.ydiv = y/4;
    addr = RL.addr8;
    return 0;
}

/* Translates an address to an xy coordinate */
int addrToXY(uint8_t addr, uint8_t &x, uint8_t &y)
{
    union readerLocation RL;
    if(addr > 255) return 1;
    RL.addr8 = addr;
    x = (RL.xy.xdiv * 4) + RL.xy.xmod;
    y = (RL.xy.ydiv * 4) + RL.xy.ymod;
    return 0;    
}

/* checks to see if a given UID is blocked */
bool blocked(uint32_t UID){
	for(int i = 0; i < BLOCKED_TAG_MAX; i++)
	{
		if(blockedTags[i] == UID && UID)
		{
			return true;
		}
	}
	return false;
}

/*****************************************************************************/
/* Arduino Setup() and Loop() */
/*****************************************************************************/
void setup(){
  bool start = false;
  Serial.begin(9600);
  while(!Serial);
  while(!start){
	while(!Serial.available()){}
	byte cmd = Serial.read();
	cmd &= 0x07;
	if(cmd == 0x07)
	{
		byte argBytes[RX_SYNC_BYTES];
		Serial.readBytes(argBytes,RX_SYNC_BYTES);
		
		uint8_t arg = argBytes[0];
		uint8_t x_max = argBytes[1];
		uint8_t y_max = argBytes[2];
		
		/*****************************************************************************/
		/* START UP THE GRID IN RESPONSE TO THE SYNC COMMAND */
		
		/* Configure GPIO */
		pinMode(S0_PIN, OUTPUT);
		pinMode(S1_PIN, OUTPUT);
		pinMode(S2_PIN, OUTPUT);
		pinMode(S3_PIN, OUTPUT);
		pinMode(S4_PIN, OUTPUT);
		pinMode(S5_PIN, OUTPUT);
		pinMode(S6_PIN, OUTPUT);
		pinMode(S7_PIN, OUTPUT);
		pinMode(SDA_PIN, OUTPUT);
		pinMode(RST_PIN, OUTPUT);
		
		/* Initialize the SPI bus */
		SPI.begin(); 
		
		/* Test each reader within our addressable space (0-255) */
		union readerLocation testAddress; 
		for(int i = 0; i < BANK_MAX; i++)
		{
			// configure the high nibble of the address (BANK)
			testAddress.addr4.bankID = (uint8_t)i;
			for(int j = 0; j < READER_MAX; j++)
			{
				// configure the low nibble of the address (READER)
				testAddress.addr4.readerID = (uint8_t)j;
				if(initReader(testAddress.addr8))
				{
					//There is a reader at the current testAddress
					ReaderCount++;  
				}
				else
				{
					//Clear the bit in the board mask since a reader failed
					boardMask &= ~(1 << testAddress.addr4.bankID);
					break;	//no need to test the remaining readers (reliability)
				}
			}
		}
		switch(boardMask)
		{
			case BOARD_CONFIG4x4:
				if( x_max == 4 && y_max == 4 && arg)
				{
					//we have the correct number of
					//readers, and they want to communicate
					start = true;
					SYNC = true;
					boardSeqLen = 1;
          x_max_global = 4;
          y_max_global = 4;
				}
				else
				{
					//we inform them that we don't have 
					//the desired number of readers
					//change the arg to 0, and
					//inform them of our maximum
					//and reset the board mask
					arg = 0;
					x_max = 4;
					y_max = 4;
					boardMask = 0xFFFF;
				}
				break;
			
			case BOARD_CONFIG8x8:
				if( x_max == 8 && y_max == 8 && arg)
				{
					//we have the correct number of
					//readers, and they want to communicate
					start = true;
					SYNC = true;
					boardSeqLen = 4;
					boardSequence[1] = 1;
					boardSequence[2] = 4;
					boardSequence[3] = 5;
          x_max_global = 8;
          y_max_global = 8;
				}
				else
				{
					//we inform them that we don't have 
					//the desired number of readers
					//change the arg to 0, and
					//inform them of our maximum
					//and reset the board mask
					arg = 0;
					x_max = 8;
					y_max = 8;
					boardMask = 0xFFFF;
				}
				break;
			
			case BOARD_CONFIG12x12:
				if( x_max == 12 && y_max == 12 && arg)
				{
					//we have the correct number of
					//readers, and they want to communicate
					start = true;
					SYNC = true;
					boardSeqLen = 9;
					boardSequence[1] = 1;
					boardSequence[2] = 2;
					boardSequence[3] = 4;
					boardSequence[4] = 5;
					boardSequence[5] = 6;
					boardSequence[6] = 8;
					boardSequence[7] = 9;
					boardSequence[8] = 10;
          x_max_global = 12;
          y_max_global = 12;          
				}
				else
				{
					//we inform them that we don't have 
					//the desired number of readers
					//change the arg to 0, and
					//inform them of our maximum
					//and reset the board mask
					arg = 0;
					x_max = 12;
					y_max = 12;
					boardMask = 0xFFFF;
				}
				break;
			
			case BOARD_CONFIG16x16:
				if( x_max == 16 && y_max == 16 && arg){
					//we have the correct number of
					//readers, and they want to communicate
					start = true;
					SYNC = true;
					boardSeqLen = 16;
					for(uint8_t i; i < 16; i++)
					{
						boardSequence[i] = i;
					}
          x_max_global = 16;
          y_max_global = 16;
				}
				else
				{
					//we inform them that we don't have 
					//the desired number of readers
					//change the arg to 0,
					//inform them of our maximum
					//and reset the board mask
					arg = 0;
					x_max = 16;
					y_max = 16;
					boardMask = 0xFFFF;
				}
				break;
			
			default:
				//device error or unsupported configuration
				arg = 0;
				x_max = 255;
				y_max = 255;
				boardMask = 0xFFFF;
		}
		
		// Transmit our response to the host.
		TX_SYNC(arg,x_max,y_max);
		
	}
	else
	{
		// Sync message was not sent,
		// get the rest of the bytes from 
		// the buffer so as not 
		// to interpret them as a valid SYNC command
		while(Serial.available())
		{
			Serial.read();
		}
	}
  }
}

void loop()
{
	if(Serial.available())
	{
		byte cmd = Serial.read();
		cmd &= 0x07;      //get the proper index for the LUT
		RX_LUT[cmd]();    //Call the appropriate RX function
	}
	else if(SYNC)
	{
	//No messages from host, scan grid for updates.
		union readerLocation currentAddress;
		for(int i = 0; i < boardSeqLen; i++)
		{
			currentAddress.addr4.bankID = boardSequence[i];
			for(int j = 0; j < 16; j++)
			{
				currentAddress.addr4.readerID = (uint8_t)j;
				outputAddress(currentAddress.addr8); 
				delay(10);
				Reader.PCD_AntennaOn();
				Reader.PCD_SetAntennaGain(16);
				if(Reader.PICC_IsNewCardPresent() && Reader.PICC_ReadCardSerial())
				{
					Reader.PCD_AntennaOff();  
					for( int k = 1; k <= 4; k++)
					{
						objID.uidArr[4-k] = Reader.uid.uidByte[k-1];
					}      
					if((objID.UID != Tiles[currentAddress.addr8].UID)||Tiles[currentAddress.addr8].FLAGS.ACK)
					{
						//State change or host has yet to acknowledge previous state change
						Tiles[currentAddress.addr8].UID = objID.UID;
						if(BLOCKS_IN_EFFECT && blocked(Tiles[currentAddress.addr8].UID))
						{
							Tiles[currentAddress.addr8].FLAGS.BLOCK = 1;
						}
						else
						{
							Tiles[currentAddress.addr8].FLAGS.ACK = 1; //set the acknowledge required flag
							sendUpdate(currentAddress.addr8,Tiles[currentAddress.addr8].UID);
						}
					}
				}
				else
				{
          //No tag was detected 
					Reader.PCD_AntennaOff();
					if((Tiles[currentAddress.addr8].UID != 0))
					{
						//State change or host has yet to acknowledge previous state change
						Tiles[currentAddress.addr8].UID = 0;
            
						if(!Tiles[currentAddress.addr8].FLAGS.BLOCK)
						{
							//updates for the tag previously on this reader are not blocked by host
							Tiles[currentAddress.addr8].FLAGS.ACK = 1; //set the acknowledge required flag
							sendUpdate(currentAddress.addr8,Tiles[currentAddress.addr8].UID);
						}
						else
						{
							//updates for the tag previously on this reader were blocked
							Tiles[currentAddress.addr8].FLAGS.BLOCK = 0;
              Tiles[currentAddress.addr8].FLAGS.ACK = 0;
						}
					}
				}
			}
		}
	}
}
