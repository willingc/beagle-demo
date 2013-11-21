#!/usr/bin/python
import Adafruit_BBIO.ADC as ADC
import time

ADC.setup()

while True:
	print ADC.read("P9_33")
	time.sleep(0.5)
	