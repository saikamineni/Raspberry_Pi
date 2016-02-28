import RPi.GPIO as GPIO
import time

#Use the physical pin numbers, not the logical names
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
#Set pin 11, 12, 13 as outputs
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
#Keep looping over and over
try:
        while True:
                GPIO.output(11, False)
                GPIO.output(12, True)
                GPIO.output(13, False)
                time.sleep(0.5)
                GPIO.output(11, True)
                GPIO.output(12, False)
                GPIO.output(13, False)
                time.sleep(0.5)
                GPIO.output(11, False)
                GPIO.output(12, False)
                GPIO.output(13, True)
                time.sleep(0.5)

finally:
        print("Cleaning up")
        GPIO.cleanup()
