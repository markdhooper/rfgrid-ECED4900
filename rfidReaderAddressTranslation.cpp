/******************************************************************************
 Name: rfidReaderAddressTranslation.cpp
 Date: Nov 6, 2019
 Description:
 This is a simple example of how I intend to address the RFID readers on the 
 arduino. An 8 bit address will be written to the GPIO pins. Which in return
 will enable a specific RFID reader. I need a fast way of translating xy
 coordinates to an 8 bit address to respond to any command involving xy coordinates.
 additionally, since the grid consists of modular 4x4 tile sections, such a method
 might be handy for some of the graphics api. We can get the user to specify 
 how many rows and columns the grid has, and these can be transmitted to the arduino. 
 
 *this example currently uses #defines to set max values. 
 
 
 The addressing scheme for up to 255 possible readers os configured as follows:
  [] -> the bankID consists of the top 4 bits of the 8 bit address
  () -> the readerID address consists of the lower 4 bits of the 8 bit address
  
  The mapping of coordinates to addresses is as follows:
  
                                         X-COORDINATES
         0    1    2    3     4    5    6    7    8    9    A    B    C    D    E    F
        [        0       ]   [        1       ]  [        2       ]  [        3       ]
 Y   0  (0)  (1)  (2)  (3)   (0)  (1)  (2)  (3)  (0)  (1)  (2)  (3)  (0)  (1)  (2)  (3)
 -   1  (4)  (5)  (6)  (7)   (4)  (5)  (6)  (7)  (4)  (5)  (6)  (7)  (4)  (5)  (6)  (7)
 C   2  (8)  (9)  (A)  (B)   (8)  (9)  (A)  (B)  (8)  (9)  (A)  (B)  (8)  (9)  (A)  (B)
 O   3  (C)  (D)  (E)  (F)   (C)  (D)  (E)  (F)  (C)  (D)  (E)  (F)  (C)  (D)  (E)  (F)
 O      [        4       ]   [        5       ]  [        6       ]  [        7       ]
 R   4  (0)  (1)  (2)  (3)   (0)  (1)  (2)  (3)  (0)  (1)  (2)  (3)  (0)  (1)  (2)  (3)
 D   5  (4)  (5)  (6)  (7)   (4)  (5)  (6)  (7)  (4)  (5)  (6)  (7)  (4)  (5)  (6)  (7)
 I   6  (8)  (9)  (A)  (B)   (8)  (9)  (A)  (B)  (8)  (9)  (A)  (B)  (8)  (9)  (A)  (B)
 N   7  (C)  (D)  (E)  (F)   (C)  (D)  (E)  (F)  (C)  (D)  (E)  (F)  (C)  (D)  (E)  (F)
 A      [        8       ]   [        9       ]  [        A       ]  [        B       ]
 T   8  (0)  (1)  (2)  (3)   (0)  (1)  (2)  (3)  (0)  (1)  (2)  (3)  (0)  (1)  (2)  (3)
 E   9  (4)  (5)  (6)  (7)   (4)  (5)  (6)  (7)  (4)  (5)  (6)  (7)  (4)  (5)  (6)  (7)
 S   A  (8)  (9)  (A)  (B)   (8)  (9)  (A)  (B)  (8)  (9)  (A)  (B)  (8)  (9)  (A)  (B)
     B  (C)  (D)  (E)  (F)   (C)  (D)  (E)  (F)  (C)  (D)  (E)  (F)  (C)  (D)  (E)  (F)
        [        C       ]   [        D       ]  [        E       ]  [        F       ]
     C  (0)  (1)  (2)  (3)   (0)  (1)  (2)  (3)  (0)  (1)  (2)  (3)  (0)  (1)  (2)  (3)
     D  (4)  (5)  (6)  (7)   (4)  (5)  (6)  (7)  (4)  (5)  (6)  (7)  (4)  (5)  (6)  (7)
     E  (8)  (9)  (A)  (B)   (8)  (9)  (A)  (B)  (8)  (9)  (A)  (B)  (8)  (9)  (A)  (B)
     F  (C)  (D)  (E)  (F)   (C)  (D)  (E)  (F)  (C)  (D)  (E)  (F)  (C)  (D)  (E)  (F)
     
     If I want the address of the the reader located at (x,y) = (2,4) it corresponds
     to address 0x42 i.e. bankID 4, and readerID 2 [4](2). You can seperate the two
     parts of the address by looking at the x coordinate and y coordinate:
     
     Address bit location ->  7   6   5   4     3   2   1   0
                bankID ->   [               ]  (             ) <- readerID
                            [ {y/4}   {x/4} ]  ( {y%4}  {x%4})
                            
                            The code below does this. 
     
*******************************************************************************/

#include <iostream>
#include <stdint.h>
#include <iomanip>
using namespace std;

#define ADDRMAX 255
#define MODULEMAX 15
#define X_MAX 15
#define Y_MAX 15
#define READERMAX 15
#define FAIL 0
#define PASS 1
#define MOD 4

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
};

int XYToAddr(uint8_t x, uint8_t y, uint8_t &addr);
int addrToXY(uint8_t addr, uint8_t &x, uint8_t &y);


int main()
{
    uint8_t x, y, addr;
    
    /*****************************************************************************/
    /* Pick an XY coordinate to get the address of                               */
    /*****************************************************************************/
    
    x = 5;
    y = 3;
    
    if(XYToAddr(x,y,addr)){
        cout << " Testing XYToAddr: ";
        cout << endl << " (X,Y) -> (" << hex << (int)x << "," << hex << (int)y << ")\t";
        //output the address of the reader located at (x,y)
        cout << endl << " Address -> 0x" << setfill('0') << setw(2) << hex << (int)addr << endl << endl;
    }
    else{
        cout << endl << " invalid coordinates " << endl;
    }
    
    
    /*****************************************************************************/
    /* pick an address to get the xy coordinate of..                             */
    /*****************************************************************************/
    addr = 0x0A;
    
    if(addrToXY(addr,x,y)){
        cout << " Testing addrToXY: ";
        cout << endl << " Address -> 0x" << setfill('0') << setw(2) << hex << (int)addr << "\t";
        //Output the XY position of the reader
        cout << endl << " (X,Y) -> (" << hex << (int)x << "," << hex << (int)y << ")" << endl << endl;
    }
    else{
        cout << endl << " invalid address " << endl;
    }
    return 0;
}

int addrToXY(uint8_t addr, uint8_t &x, uint8_t &y){
    union readerLocation RL;
    if(addr > ADDRMAX) return FAIL;
    RL.addr8 = addr;
    x = (RL.xy.xdiv * MOD) + RL.xy.xmod;
    y = (RL.xy.ydiv * MOD) + RL.xy.ymod;
    return PASS;    
}

int XYToAddr(uint8_t x, uint8_t y, uint8_t &addr){
    union readerLocation RL;
    if((x > X_MAX) || (y > Y_MAX)) return FAIL;
    RL.xy.xmod = x % MOD;
    RL.xy.ymod = y % MOD;
    RL.xy.xdiv = x/MOD;
    RL.xy.ydiv = y/MOD;
    addr = RL.addr8;
    return PASS;
}
