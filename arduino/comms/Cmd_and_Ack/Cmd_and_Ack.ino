/* 2020-01-14
 *  This code is a work in progress for the development of
 *  functions, constants, and data structures used to send 
 *  and receive commands (requests and acknowledgements)
 *  between the arduino and python
  */

#define max_data  64  // max message bytes

/* python commands */
#define P_UPDATE  0xF0
#define P_GETID 0xF1
#define P_GETXY 0xF2
#define P_BLOCK 0xF3
#define P_READID  0xF4
#define P_WRITEID 0xF5
#define P_READXY  0xF6
#define P_SYNC  0xFF

/* Arduino commands */
#define A_UPDATE  0x00
#define A_GETID 0x01
#define A_GETXY 0x02
#define A_BLOCK 0x03
#define A_READID  0x04
#define A_WRITEID 0x05
#define A_READXY  0x06
#define A_SYNC  0x0F


#define FALSE 0
#define TRUE  1

/* message sizes */
#define UPDATE_MSG_SZ 7
#define GETID_MSG_SZ  7
#define GETXY_MSG_SZ  7

/* Additional Constants */
#define UPDATE_MSG_SZ 7
#define TRIAL_THRESHOLD 1
#define READER_LIMIT 256
#define BANK_MAX 16
#define READER_MAX 16
#define BOARD_CONFIG4x4   0b0000000000000001
#define BOARD_CONFIG8x8   0b0000000000110011
#define BOARD_CONFIG12x12 0b0000011101110111
#define BOARD_CONFIG16x16 0b1111111111111111

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

struct Tile{
  uint32_t UID;
};

union data16{
  byte parts[2];
  uint16_t whole;
};

/*****************************************************************************/
/* Global Variables */
/*****************************************************************************/
byte event = FALSE;
uint8_t event_addr;
uint32_t event_ID;
struct Tile Tiles[READER_LIMIT];

/*****************************************************************************/
/* Functions */
/*****************************************************************************/
void sendUpdate(uint8_t addr, uint32_t ID){
  uint8_t msg[UPDATE_MSG_SZ];
  msg[0] = A_UPDATE;
  long_to_bytes(&msg[1], ID);
  addrToXY(addr,msg[5],msg[6]);
  #if DEBUG
    char buf[22];
    sprintf(buf,"%.2x %.2x %.2x %.2x %.2x %.2x %.2x",
                msg[0],msg[1],msg[2],msg[3],msg[4],msg[5],msg[6]);
    Serial.println(buf);
  #else
    Serial.write(msg,UPDATE_MSG_SZ);
  #endif
}

void sendGetID(uint8_t x, uint8_t y){
  uint8_t msg[GETID_MSG_SZ];
  uint8_t addr;
  
  msg[0] = A_GETID;
  XYToAddr(x, y, addr);
  long_to_bytes(&msg[1], Tiles[addr].UID);
  msg[5] = x;
  msg[6] = y;
  #if DEBUG
    char buf[22];
    sprintf(buf,"%.2x %.2x %.2x %.2x %.2x %.2x %.2x",
                msg[0],msg[1],msg[2],msg[3],msg[4],msg[5],msg[6]);
    Serial.println(buf);
  #else
    Serial.write(msg,GETID_MSG_SZ);
  #endif
}

/* converts byte array to 32bit long */
uint32_t bytes_to_long(uint8_t buf[]){
  union intUID tagID;
  tagID.uidArr[3] = buf[0];
  tagID.uidArr[2] = buf[1];
  tagID.uidArr[1] = buf[2];
  tagID.uidArr[0] = buf[3];
  return tagID.UID;
}
/* converts 32bit long to byte array */
void long_to_bytes(uint8_t buf[], uint32_t ID){
  union intUID tagID;
  tagID.UID = ID;
  buf[0] = tagID.uidArr[3];
  buf[1] = tagID.uidArr[2];
  buf[2] = tagID.uidArr[1];
  buf[3] = tagID.uidArr[0];
}

/* converts byte array to 16bit int */
uint16_t bytes_to_int(uint8_t buf[]){
  union data16 data;
  data.parts[1] = buf[0];
  data.parts[0] = buf[1];
  return data.whole;
}
/* converts 16bit int to byte array */
void int_to_bytes(uint8_t buf[], uint16_t num){
  union data16 data;
  data.whole = num;
  buf[0] = data.parts[1];
  buf[1] = data.parts[0];
}

int XYToAddr(byte x, byte y, byte &addr){
    union readerLocation RL;
    if((x > 15) || (y > 15)) return 1;
    RL.xy.xmod = x % 4;
    RL.xy.ymod = y % 4;
    RL.xy.xdiv = x/4;
    RL.xy.ydiv = y/4;
    addr = RL.addr8;
    return 0;
}

int addrToXY(uint8_t addr, uint8_t &x, uint8_t &y){
    union readerLocation RL;
    if(addr > 255) return 1;
    RL.addr8 = addr;
    x = (RL.xy.xdiv * 4) + RL.xy.xmod;
    y = (RL.xy.ydiv * 4) + RL.xy.ymod;
    return 0;    
}

void serialEvent(){
  event = TRUE;
  if(Serial.read() == P_GETID){
    event = TRUE;
    // parse message and accept acknowledgement
  }
}

/*****************************************************************************/
/* Arduino Setup() and Loop() */
/*****************************************************************************/
void setup() {
  Serial.begin(9600); // set the baud rate
  event_addr = 0x01;//0xFF&random(0xFF);
  event_ID = 0x01;//random(0xFFFFFFFF);
  Tiles[1].UID = 0xFF;
}
void loop() {
  if(event == TRUE){
    byte x = Serial.read();
    byte y = Serial.read();
    sendGetID(x, y);
    event = FALSE;
  }
  delay(1000);
}
