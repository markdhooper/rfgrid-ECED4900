/*****************************************************************************/
/* Data Structures */
/*****************************************************************************/
union readerLocation {
    uint8_t addr8;
    struct BR{
        uint8_t readerID : 4;
        uint8_t bankID : 4;
    }addr4;
    struct ydxdymxm{
        uint8_t xmod : 2;
        uint8_t ymod : 2;
        uint8_t xdiv : 2;
        uint8_t ydiv : 2;
    }xy;
  struct ab{
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

union intUID {
  byte uidArr[4];
  uint32_t UID;
};

/*****************************************************************************/
/* Command Functions */
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
#define TX_SYNC_BYTES 3         // CMD, begin, num_readers

/*****************************************************************************/
/* These automatically get called based on the CMD byte read in the loop()   */
/*****************************************************************************/
void RX_UPDATE()
{
  uint8_t x, y;
  intUID rx_id;
  
  byte argBytes[RX_UPDATE_BYTES];
  Serial.readBytes(argBytes,RX_UPDATE_BYTES);
  
  x = argBytes[0]; 
  y = argBytes[1]; 
  rx_id.uidArr[0] = argBytes[5];
  rx_id.uidArr[1] = argBytes[4]; 
  rx_id.uidArr[2] = argBytes[3]; 
  rx_id.uidArr[3] = argBytes[2]; 
  
  //do the things

}

void RX_GET_ID()
{
  uint8_t x, y;
  uint32_t id;
  
  byte argBytes[RX_GET_ID_BYTES];
  Serial.readBytes(argBytes,RX_UPDATE_BYTES);

  //do the things
  /*****************************************************************************/
  /* HARD CODED - ONLY FOR TESTING, THE REAL VALUES WILL NEED TO BE COMPUTED   */
              x = argBytes[0];
              y = argBytes[1];
              id = 0xDEAD;
  /*****************************************************************************/

  //transmit the result
  TX_GET_ID(x, y, id);
  
}

void RX_GET_XY()
{
  uint8_t x, y;
  intUID id;
  
  byte argBytes[RX_GET_XY_BYTES];
  Serial.readBytes(argBytes,RX_UPDATE_BYTES);

  //do the things
  /*****************************************************************************/
  /* HARD CODED - ONLY FOR TESTING, THE REAL VALUES WILL NEED TO BE COMPUTED   */
              x = 2;
              y = 2;
              id.uidArr[0] = argBytes[3];
              id.uidArr[1] = argBytes[2];
              id.uidArr[2] = argBytes[1];
              id.uidArr[3] = argBytes[0];
  /*****************************************************************************/

  //transmit the result
  TX_GET_XY(x,y,id.UID);
}

void RX_BLOCK()
{
  uint8_t arg;
  intUID id;
  
  byte argBytes[RX_BLOCK_BYTES];
  Serial.readBytes(argBytes,RX_UPDATE_BYTES);  

  //do the things

  /*****************************************************************************/
  /* HARD CODED - ONLY FOR TESTING, THE REAL VALUES WILL NEED TO BE COMPUTED   */
              arg = argBytes[0];
              id.uidArr[0] = argBytes[4];
              id.uidArr[1] = argBytes[3];
              id.uidArr[2] = argBytes[2];
              id.uidArr[3] = argBytes[1];
  /*****************************************************************************/

  //transmit the result
  TX_BLOCK(arg, id.UID);

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
  uint8_t num_readers;
  
  byte argBytes[RX_SYNC_BYTES];
  Serial.readBytes(argBytes,RX_UPDATE_BYTES);

  //do the things

  
  /**********************************************************************/
  /* HARDCODED ONLY FOR TESTING, these values will need to be computed  */
          arg = 0;
          num_readers = 64;
  /**********************************************************************/

  //transmit the result
  TX_SYNC(arg,num_readers);
}


/*****************************************************************************/
/* Call these when you want to transmit a specific response to the Host      */
/*****************************************************************************/

void TX_UPDATE(uint8_t x, uint8_t y, uint32_t id)
{
    intUID temp;
    temp.UID = id;
    uint8_t buf[TX_UPDATE_BYTES];
    buf[0] = 0x00;        //UPDATE COMMAND
    buf[1] =  x;
    buf[2] =  y;
    buf[3] = temp.uidArr[3];
    buf[4] = temp.uidArr[2];
    buf[5] = temp.uidArr[1];
    buf[6] = temp.uidArr[0];
    Serial.write(buf, TX_UPDATE_BYTES);
}

void TX_GET_ID(uint8_t x, uint8_t y, uint32_t id)
{
    intUID temp;
    temp.UID = id;
    uint8_t buf[TX_GET_ID_BYTES];
    buf[0] = 0x01;        //GET_ID COMMAND
    buf[1] =  x;
    buf[2] =  y;
    buf[3] = temp.uidArr[3];
    buf[4] = temp.uidArr[2];
    buf[5] = temp.uidArr[1];
    buf[6] = temp.uidArr[0];
    Serial.write(buf, TX_GET_ID_BYTES);
}

void TX_GET_XY(uint8_t x, uint8_t y, uint32_t id)
{
    intUID temp;
    temp.UID = id;
    uint8_t buf[TX_GET_XY_BYTES];
    buf[0] = 0x02;        //GET_XY COMMAND
    buf[1] =  x;
    buf[2] =  y;
    buf[3] = temp.uidArr[3];
    buf[4] = temp.uidArr[2];
    buf[5] = temp.uidArr[1];
    buf[6] = temp.uidArr[0];
    Serial.write(buf, TX_GET_XY_BYTES);
}

void TX_BLOCK(uint8_t arg, uint32_t id)
{
    intUID temp;
    temp.UID = id;
    uint8_t buf[TX_BLOCK_BYTES];
    buf[0] = 0x03;        //BLOCK COMMAND
    buf[1] =  arg;
    buf[2] = temp.uidArr[3];
    buf[3] = temp.uidArr[2];
    buf[4] = temp.uidArr[1];
    buf[5] = temp.uidArr[0];
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

void TX_SYNC(uint8_t arg, uint8_t num_readers)
{
  uint8_t buf[TX_SYNC_BYTES];
  buf[0] = 0x0F;     //SYNC Command
  buf[1] = arg;
  buf[2] = num_readers;
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
/* Arduino Setup() and Loop() */
/*****************************************************************************/

void setup() {
  Serial.begin(9600);
  while(!Serial);
  while(!Serial.available()){}
  
  
    byte cmd = Serial.read();
    cmd &= 0x07;
    if(cmd == 0x07)
    {
      //INITIALIZE GRID HERE!!!!!!!!!!!!
      //THEN TRANSMIT THE PROPER RESPONSE
      //TO SYNC
        byte argBytes[RX_SYNC_BYTES];
        Serial.readBytes(argBytes,RX_SYNC_BYTES);

              //INITIALIZE GRID HERE!!!!!!!!!!!!
              //THEN TRANSMIT THE PROPER RESPONSE TO SYNC
              /**********************************************************************/
              /* HARDCODED ONLY FOR TESTING, these values will need to be computed  */
                  uint8_t arg = argBytes[0];
                  uint8_t num_readers = 64;
              /**********************************************************************/
              TX_SYNC(arg,num_readers);

  }
}

uint8_t gX = 0;
uint8_t gY = 0;
uint32_t gID = 0;

void loop()
{
  if(Serial.available())
  {
    byte cmd = Serial.read();
    cmd &= 0x07;      //get the proper index for the LUT
    RX_LUT[cmd]();    //Call the appropriate RX function
  }
  else
  {
    /*****************************************************************************/
    /* THIS IS WHERE WE WOULD NORMALLY LOOP THROUGH THE READERS                  */
    /*****************************************************************************/
    delay(1500);                  //SIMULATION ONLY
    TX_UPDATE(gX++,gY++,gID++);   //SIMULATION ONLY
  }
}
