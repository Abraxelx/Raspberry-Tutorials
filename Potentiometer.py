import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LED = 4
PTM = 17
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(PTM,GPIO.IN)

count = 0
while True:
    k = GPIO.input(PTM)
    if (k == 1):
        GPIO.output(LED,True)
        print("LED ON")
        print(k)
        time.sleep(1)
    elif (k==0):
        GPIO.output(4,False)
        print("LED OFF")
        print(k)
        time.sleep(1)

