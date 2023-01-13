from Arduino import Arduino
import time

board = Arduino('9600')
board.pinMode(13, "OUTPUT")

def blink1():
    board.digitalWrite(13, "LOW")
    time.sleep(1)
    board.digitalWrite(13, "HIGH")
    time.sleep(1)

while True:
    blink1()