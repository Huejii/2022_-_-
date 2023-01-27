from Arduino import Arduino
import time

servoPin = 9

board = Arduino("9600", port = "COM3")
board.Servo.attach(servoPin)

while True:
    board.Servo.write(servoPin, 0)
    time.sleep(1)
    board.Servo.write(servoPin, 90)
    time.sleep(1)
    board.Servo.write(servoPin, 180)
    time.sleep(1)
    board.Servo.write(servoPin, 90)
    time.sleep(1)