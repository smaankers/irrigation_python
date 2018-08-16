import RPi.GPIO as GPIO


class IO_irrigation(object):

    def __init__(self):

        self.__pin_list = 	{
                 5 : 	{'name'	: 'pump',		'state' : False},
                11 : 	{'name'	: 'sensors',		'state' : False},
                 4 : 	{'name'	: 'valve sewage',	'state' : False},
                17 : 	{'name'	: 'valve refill',	'state' : False},
                27 : 	{'name'	: 'valve filter',	'state' : False},
                22 : 	{'name'	: 'valve right',	'state' : False},
                10 : 	{'name'	: 'valve drip',	'state' : False},
                 9 : 	{'name'	: 'valve left',	'state' : False},
                }

        for pin_id in self.__pin_list:
            print("pin: #" + str(pin_id) + "name: " + self.__pin_list[pin_id]['name'])

    def start(self):
        GPIO.setmode(GPIO.BCM)

        for pin_id in self.__pin_list:
            GPIO.setup(pin_id, GPIO.OUT)

        self.__set_all_pins_off()

        print ("io started")

    def stop(self):
        self.__set_all_pins_off()
        GPIO.cleanup()

        print ("io stopped")

    def get_pump(self):
        return self.__pin_list[5]['state']

    def set_pump(self, on):
        self.__set_pin(5, on)

    def get_sensors(self):
        return self.__pin_list[11]['state']

    def set_sensors(self, on):
        self.__set_pin(11, on)

    def set_valve_sewage(self, on):
        self.__set_pin(4, on)

    def set_valve_refill(self, on):
        self.__set_pin(17, on)

    def set_valve_filter(self, on):
        self.__set_pin(27, on)

    def get_valve_right(self):
        return self.__pin_list[22]['state']

    def set_valve_right(self, on):
        self.__set_pin(22, on)

    def set_valve_drip(self, on):
        self.__set_pin(10, on)

    def get_valve_left(self):
        return self.__pin_list[9]['state']

    def set_valve_left(self, on):
        self.__set_pin(9, on)

    def __set_pin(self, pin_id, on):
        self.__pin_list[pin_id]['state'] = on

        if on:
            GPIO.output(pin_id, 0)
        else:
            GPIO.output(pin_id, 1)

    def __set_all_pins_off(self):
        for pin_id in self.__pin_list:
            self.__set_pin(pin_id, False)



