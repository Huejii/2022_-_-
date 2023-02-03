from Arduino import Arduino
import time

tempPin = 0

board = Arduino("9600", port = "COM9")

while True:
    value = board.analogRead(tempPin)
    print("value: ", value)

    # 섭씨온도 = ADC(analogRead로 읽은 값) / 1024 * 전압(mv)/10(mv/C)
    millivolts = (value / 1024.0) * 5000.0
    celsius = (millivolts)/ 10.0

    print("celsius: ", celsius)
    time.sleep(1)