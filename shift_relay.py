import RPi.GPIO as GPIO
from time import sleep

pin_latch = 20
pin_clock = 23
pin_data  = 18

def clock_pulse():
	GPIO.output(pin_clock, 1)
	sleep(0.5)
	GPIO.output(pin_clock, 0)
	sleep(0.5)
	
def latch():
	GPIO.output(pin_latch, 1)
	sleep(0.5)
	GPIO.output(pin_latch, 0)
	sleep(0.5)

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin_latch, GPIO.OUT)
GPIO.setup(pin_clock, GPIO.OUT)
GPIO.setup(pin_data, GPIO.OUT)

	
GPIO.output(pin_latch, 0)
GPIO.output(pin_clock, 0)
GPIO.output(pin_data, 0)
sleep(1)

GPIO.output(pin_data, 1)
clock_pulse()
latch()	

GPIO.output(pin_data, 0)
clock_pulse()
latch()
clock_pulse()
latch()	

GPIO.cleanup()


	
	
	
