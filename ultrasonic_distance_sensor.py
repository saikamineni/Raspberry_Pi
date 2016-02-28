#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

#assigning pin numbers
TRIG = 23
ECHO = 24

print "Distance Measurement In Progress"

#setting up pins
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

#stop the trigger
GPIO.output(TRIG, False)

print "Waiting For Sensor To Settle"
time.sleep(2)

#start the trigger for 0.00001 seconds and stop
GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

#calculate the latest time when echo is off
while GPIO.input(ECHO)==0:
	pulse_start = time.time()

#calculate the latest time when echo is on
while GPIO.input(ECHO)==1:
	pulse_end = time.time()   

#calculate duration of echo
pulse_duration = pulse_end - pulse_start

#speed of sound is 343m/s
#distance = speed * time
#distance = 34300 cm/s * time/2 (since time is the total to and fro time)
distance = pulse_duration * 17150

distance = round(distance, 2)
print "Distance:",distance,"cm"

GPIO.cleanup()