import RPi.GPIO as GPIO
import time

# Configure the Pi to use the BCM (Broadcom) pin names, rather than the pin positions
#GPIO.setmode(GPIO.BCM)
GPIO.setmode(GPIO.BOARD)
led_pin = 12
#led_pin = 18

GPIO.setup(led_pin, GPIO.OUT)


try:
    while True:
        GPIO.output(led_pin, True)  # LED on
        time.sleep(0.5)             # delay 0.5 seconds
        GPIO.output(led_pin, False) # LED off
        time.sleep(0.5)             # delay 0.5 seconds

finally:
    print("Cleaning up")
    GPIO.cleanup()
