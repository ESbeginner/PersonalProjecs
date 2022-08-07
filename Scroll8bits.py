#I found this code in the comment section of the same web 

from machine import Pin
from time import sleep
import utime

# LCD Code
class LCD:
    """
https://www.instructables.com/Raspberry-Pi-PICO-L...

     RPI PICO   LCD Pins on most Hitachi HD44780 controlled LCDs
        GND     1 - VSS Ground
       VBUS     2 - VDD / VCC +3.3 to +5V (typical)
         -      3 - VO - Contrast adjust - Use 10K Pot OR 2K ohm resistor to GND
        GP0     4 - RS - Register Select. RS=0: Command, RS=1: Data
        GND     5 - Read/Write (R/W). R/W=0: Write, R/W=1: Read, Not used connected to ground.
        GP1     6 - Clock (Enable). Falling edge triggered
         -      7 - Bit 0 (Not used in 4-bit operation)
         -      8 - Bit 1 (Not used in 4-bit operation)
         -      9 - Bit 2 (Not used in 4-bit operation)
         -      10 - Bit 3 (Not used in 4-bit operation)
        GP2     11 - Bit 4
        GP3     12 - Bit 5
        GP4     13 - Bit 6
        GP5     14 - Bit 7
       VBUS     15 - A Backlight Anode (+) (If applicable) 
        GND     16 - K Backlight Cathode (-) (If applicable)
    """


    def __init__(self):
self.rs = Pin(0,Pin.OUT)
        self.e = Pin(1,Pin.OUT)
        self.d4 = Pin(2,Pin.OUT)
        self.d5 = Pin(3,Pin.OUT)
        self.d6 = Pin(4,Pin.OUT)
        self.d7 = Pin(5,Pin.OUT)




    def scrollText(self, text, line=1, breakChars=" | ", displayWidth=16):
        xindex = 0
        st = text + breakChars + text + breakChars
        scrollSlice = text
        while True:
            if len(text) > displayWidth:
                scrollSlice = st[xindex:displayWidth+xindex]
                xindex += 1
                if xindex > len(st) - displayWidth:
                    xindex = 0
            self.whichLinePos(line, 0)
            self.prt(scrollSlice)

            yield None

    def prt(self, text):
        for x in text:
            self.send2LCD8(ord(x))




    def delayShort(self):
        utime.sleep_us(40)

    def delay(self):
        utime.sleep_ms(2)

    def delayBig(self):
        utime.sleep(0.3)

    def pulseE(self):
        self.e.value(1)
        self.delayShort()
        self.e.value(0)
        self.delayShort()

    def send2LCD4(self, BinNum):
        self.d4.value((BinNum & 0b00000001) >>0)
        self.d5.value((BinNum & 0b00000010) >>1)
        self.d6.value((BinNum & 0b00000100) >>2)
        self.d7.value((BinNum & 0b00001000) >>3)
        self.pulseE()

    def send2LCD8(self, BinNum):
        self.d4.value((BinNum & 0b00010000) >>4)
        self.d5.value((BinNum & 0b00100000) >>5)
        self.d6.value((BinNum & 0b01000000) >>6)
        self.d7.value((BinNum & 0b10000000) >>7)
        self.pulseE()
        self.d4.value((BinNum & 0b00000001) >>0)
        self.d5.value((BinNum & 0b00000010) >>1)
        self.d6.value((BinNum & 0b00000100) >>2)
        self.d7.value((BinNum & 0b00001000) >>3)
        self.pulseE()




    def whichLinePos(self, line, pos):
        b = 0
        if (line == 1):
            b = 0
        if (line == 2):
            b = 40
        if (line == 3):
            b = 20
        if (line == 4):
            b = 60
        self.cursorHome()
        for x in range(0,b+pos):
            self.moveCursorR()




    def clearDisplay(self):#blanks the LCD, needs a long delay.
self.rs.value(0)
        self.send2LCD8(0b00000001)
self.rs.value(1)
        self.delay()        
    def cursorHome(self):#returns the cursor to home, needs a long delay.
self.rs.value(0)
        self.send2LCD8(0b00000010)
self.rs.value(1)
        self.delay()
    def cursorMoveForward(self):
self.rs.value(0)
        self.send2LCD8(0b00000110)
self.rs.value(1)
    def cursorMoveBack(self):
self.rs.value(0)
        self.send2LCD8(0b00000100)
self.rs.value(1)
    def moveCursorR(self):#write text from left to right
self.rs.value(0)
        self.send2LCD8(0b00010100)
self.rs.value(1)
    def moveCursorL(self):#write text from right to left (backwards)
self.rs.value(0)
        self.send2LCD8(0b00010000)
self.rs.value(1)
    def cursorOff(self):
self.rs.value(0)
        self.send2LCD8(0b00001100)
self.rs.value(1)
    def cursorOn(self):
self.rs.value(0)
        self.send2LCD8(0b00001110)
self.rs.value(1)
    def blinkOn(self):
self.rs.value(0)
        self.send2LCD8(0b00001111)
self.rs.value(1)
    def blinkOff(self):
self.rs.value(0)
        self.send2LCD8(0b00001100)
self.rs.value(1)
    def displayShiftR(self):#move all caractors one space right
self.rs.value(0)
        self.send2LCD8(0b00011100)
self.rs.value(1)
    def displayShiftL(self):#move all caractors one space left
self.rs.value(0)
        self.send2LCD8(0b00011000)
self.rs.value(1)
    def displayOff(self):
self.rs.value(0)
        self.send2LCD8(0b00001000)
self.rs.value(1)
    def displayOn(self):
self.rs.value(0)
        self.send2LCD8(0b00001100)
self.rs.value(1)

    def setUpLCD(self):
self.rs.value(0)
        self.send2LCD4(0b0011)
        self.send2LCD4(0b0011)
        self.send2LCD4(0b0011)
        self.send2LCD4(0b0010)
        self.send2LCD8(0b00101000)
        self.send2LCD8(0b00001100)
        self.send2LCD8(0b00000110)
        self.send2LCD8(0b00000001)
self.rs.value(1)




if __name__ == "__main__":




    l = LCD()
    l.setUpLCD()
    l.clearDisplay()


    line1 = l.scrollText("Hello There", line=1, breakChars="", displayWidth=16)
    line2 = l.scrollText("Do you like my scrolling sign?", line=2, breakChars=" | ", displayWidth=16)


    while True:
        sleep(0.2)
        next(line1)
        next(line2)


    # This code never actually gets here but to clean up the 2 generators
    # Call the following lines:
    line1.close()
    line2.close()
