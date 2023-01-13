from Arduino import Arduino
import time

led1 = 13
led2 = 12
led3 = 11


board = Arduino('9600')
board.pinMode(led1, "OUTPUT")
board.pinMode(led2, "OUTPUT")
board.pinMode(led3, "OUTPUT")

def blinkLED(pin, s):
    board.digitalWrite(pin, "HIGH")
    time.sleep(s)
    board.digitalWrite(pin, "LOW")
    time.sleep(s)

while True:
    blinkLED(led1, 1)
    blinkLED(led2, 1)
    blinkLED(led3, 1)

