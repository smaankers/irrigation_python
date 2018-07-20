import RPi.GPIO as GPIO
import sys
from time import sleep
import deadline

pin_id_pump          = 5
pin_id_sensors       = 11
pin_id_valve_sewage  = 4
pin_id_valve_refill  = 17
pin_id_valve_filter  = 27
pin_id_valve_group_3 = 22
pin_id_valve_group_2 = 10
pin_id_valve_group_1 = 9

pins = [pin_id_pump,          \
        pin_id_sensors,       \
        pin_id_valve_sewage,  \
	pin_id_valve_refill,  \
	pin_id_valve_filter,  \
	pin_id_valve_group_3, \
	pin_id_valve_group_2, \
	pin_id_valve_group_1]

def init():
	GPIO.setmode(GPIO.BCM)

	for pin_id in pins:
		GPIO.setup(pin_id, GPIO.OUT)
		set_pin(pin_id, False)

def deinit():
	GPIO.cleanup()

def set_pin(pin_id, on):
	if on:
		GPIO.output(pin_id, 0)
	else:
		GPIO.output(pin_id, 1)

def main():
	init()

	duration_minutes = sys.argv[1]
	d                 = deadline.Deadline(duration_minutes)
	
	try:
		running = True
		while running:
			set_pin(pin_id_pump,		False)
			set_pin(pin_id_sensors,	True)
			set_pin(pin_id_valve_sewage,	False)
			set_pin(pin_id_valve_refill,	True)
			set_pin(pin_id_valve_filter,	False)
			set_pin(pin_id_valve_group_3,	False)
			set_pin(pin_id_valve_group_2,	False)
			set_pin(pin_id_valve_group_1,	False)
			
			if d.is_achieved():
				print "finished, exiting"
				running = False
			else:
				sleep(1)
		
	except KeyboardInterrupt:
		pass
	
	deinit()

main()
