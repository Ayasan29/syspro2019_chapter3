import time
import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
 
while True:
    GPIO.output(14, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(14, GPIO.LOW)
    sleep(0.5)
