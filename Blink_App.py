#blink.py
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LED = 4
GPIO.setup(LED,GPIO.OUT)
for counter in range(0,100):
    GPIO.output(LED,True)
    print("LED ON")
    time.sleep(3)
    GPIO.output(4,False)
    print("LED OFF")
    time.sleep(1)
