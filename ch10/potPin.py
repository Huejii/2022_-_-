from Arduino import Arduino
import time

potPin=0
ledPin=11


board = Arduino("9600", port="COM7") #포트변경
board.pinMode(ledPin, "OUTPUT")


while True:
    potValue=board.analogRead(potPin)
    brightness=potValue/4
    board.analogWrite(ledPin, brightness)
    time.sleep(0.1)
