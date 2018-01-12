import time ##Time Kütüphanesi eklendi
import RPi.GPIO as GPIO ##Raspberry'nin GPIO Kütüphanesi eklendi ismi GPIO larak tanımlandı

GPIO.setmode(GPIO.BCM)
LED = 4 ## Değeri 4 olan bir LED değişkeni tanımlandı
GPIO.setup(LED,GPIO.OUT) ##LED Output olarak tanımlandı
for counter in range(0,100): 
    GPIO.output(LED,True) ##4'e 5V ver
    print("LED ON")
    time.sleep(3)
    GPIO.output(4,False) ##4'e 0V ver
    print("LED OFF")
    time.sleep(1)
