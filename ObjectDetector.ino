
/*****************************************************************************/
/* Purpose:       To test the functionality of Mifare RC522 RFID reader      */
/* Description:   This is a barebones test to identify the name of 4 RFID    */
/*                devices that came with a pair of RFID card readers.        */
/* Written by:    Mark Hooper, modified from sketch found from the following */
/*                Library examples created by Miguel Balboa:                 */
/*                        https://github.com/miguelbalboa/rfid               */
/*****************************************************************************/

#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN         9           // Configurable, see typical pin layout above
#define SS_PIN          10          // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);   // Create MFRC522 instance.

union intUID {
  byte uidArr[4];
  uint32_t UID;
};

struct Objects{
  uint32_t UID;
  char Name[10];
};


union intUID objID;

struct Objects ObjectList[4] = {
  {3661498880 , "FOB A" },
  {2543425536 , "FOB B" },
  {2830866688 , "CARD A"},
  {214977792  , "CARD B"}  
  };

void setup() {
  // put your setup code here, to run once:
    Serial.begin(9600); // Initialize serial communications with the PC
    while (!Serial);    // Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
    SPI.begin();        // Init SPI bus
    mfrc522.PCD_Init(); // Init MFRC522 card
    Serial.println(F("Scan a Card or Fob"));
}

void loop() {
    // Look for new cards
    if ( ! mfrc522.PICC_IsNewCardPresent())
        return;

    // Select one of the cards
    if ( ! mfrc522.PICC_ReadCardSerial())
        return;

    //Copy the scanned UID for uint32_t comparison in table
    for( int i = 0; i < 4; i++){
      objID.uidArr[4-i] = mfrc522.uid.uidByte[i];
    }
    
    // Tell user what object was scanned
    Serial.print(F("Object Scanned: "));

    
    for( int i = 0; i < 4; i++){
      if(objID.UID == ObjectList[i].UID){
            Serial.println(ObjectList[i].Name);
      }
    }

}
