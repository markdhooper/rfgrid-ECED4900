/*****************************************************************************/
/* Program Name:  rfgrid.ino  (https://github.com/markdhooper/rfgridECED4900)        */
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

/* SET TO 1 to enable Serial Monitor Messages */
#define DEBUG 0

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

/*****************************************************************************/
/* Global Variables */
/*****************************************************************************/
union intUID objID;
struct Tile Tiles[READER_LIMIT];
int updateFlag = 0;
MFRC522 Reader(SDA_PIN, RST_PIN);
int ReaderCount = 0;
uint16_t boardMask = 0xFFFF;
uint8_t boardSequence[16] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
uint8_t boardSeqLen = 0;

/*****************************************************************************/
/* Functions */
/*****************************************************************************/

void outputAddress(uint8_t addr){
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

bool initReader(uint8_t addr){
  bool result;
  outputAddress(addr);
  delay(10);
  Reader.PCD_Init();
  int numTrials = 0;
  int gainTest = 16;
  for(int j = 0; j < TRIAL_THRESHOLD; j++){
    Reader.PCD_SetAntennaGain(gainTest);
    if(Reader.PCD_GetAntennaGain() == gainTest){
      numTrials++;
    }
  }
  Reader.PCD_AntennaOff();  
  return (numTrials == TRIAL_THRESHOLD);
}


void sendUpdate(uint8_t addr, uint32_t ID){
  union intUID tagID;
  tagID.UID = ID;
  uint8_t msg[UPDATE_MSG_SZ];
  msg[0] = 0;
  msg[1] = tagID.uidArr[3];
  msg[2] = tagID.uidArr[2];
  msg[3] = tagID.uidArr[1];
  msg[4] = tagID.uidArr[0];
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


/*****************************************************************************/
/* Arduino Setup() and Loop() */
/*****************************************************************************/

void setup() {
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

  Serial.begin(9600);
  while(!Serial);   
  SPI.begin(); 
  union readerLocation testAddress; 
  for(int i = 0; i < BANK_MAX; i++){
    testAddress.addr4.bankID = (uint8_t)i;
    for(int j = 0; j < READER_MAX; j++){
      testAddress.addr4.readerID = (uint8_t)j;
      if(initReader(testAddress.addr8)){
        #if DEBUG
          Serial.print("Reader[");
          Serial.print(testAddress.addr8, HEX);
          Serial.println("]...PASS ");
        #endif
        ReaderCount++;  
      }else{
        boardMask &= ~(1 << testAddress.addr4.bankID);
        #if DEBUG
          Serial.print("Reader[");
          Serial.print(testAddress.addr8, HEX);  
          Serial.print("]...FAIL  BoardMask = ");
          Serial.println(boardMask, HEX);
        #endif
      }
    }
  }
    #if DEBUG
      Serial.print("Initialization Complete: ");
      Serial.print(ReaderCount);
      Serial.println(" Readers were detected");
    #endif
    switch(boardMask){
        case BOARD_CONFIG4x4:
          boardSeqLen = 1;
          #if DEBUG
            Serial.println("Grid Configuration : 4x4");
          #endif
          break;
        case BOARD_CONFIG8x8:
          boardSeqLen = 4;
          boardSequence[1] = 1;
          boardSequence[2] = 4;
          boardSequence[3] = 5;
          #if DEBUG
            Serial.println("Grid Configuration : 8x8");
          #endif
          break;
        case BOARD_CONFIG12x12:
          boardSeqLen = 9;
          boardSequence[1] = 1;
          boardSequence[2] = 2;
          boardSequence[3] = 4;
          boardSequence[4] = 5;
          boardSequence[5] = 6;
          boardSequence[6] = 8;
          boardSequence[7] = 9;
          boardSequence[8] = 10;
          #if DEBUG
            Serial.println("Grid Configuration : 12x12");
          #endif
          break;
        case BOARD_CONFIG16x16:
          boardSeqLen = 16;
          for(uint8_t i; i < 16; i++){
            boardSequence[i] = i;
          }
          #if DEBUG
            Serial.println("Grid Configuration : 16x16");
          #endif
          break;
    }

}


void loop() {
  union readerLocation currentAddress;
  for(int i = 0; i < boardSeqLen; i++){
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
            if(objID.UID != Tiles[currentAddress.addr8].UID){
                updateFlag = 1;
                Tiles[currentAddress.addr8].UID = objID.UID;
                sendUpdate(currentAddress.addr8,Tiles[currentAddress.addr8].UID);
            }
      }else{
        Reader.PCD_AntennaOff();
        if((Tiles[currentAddress.addr8].UID != 0)){
          updateFlag = 1;
          Tiles[currentAddress.addr8].UID = 0;
          sendUpdate(currentAddress.addr8,Tiles[currentAddress.addr8].UID);
        }
      }
    }
  }
}
