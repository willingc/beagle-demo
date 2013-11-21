#!/usr/bin/python
import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P8_11", GPIO.IN)

while True:
	if GPIO.input("P8_11"):
		print "The button was pressed!"
		while GPIO.input("P8_11"):
			time.sleep(.01)
		print "The button was released!"
	time.sleep(.01)
	