import hal.Timed


class Timed_valve_left(hal.Timed.Timed):

    def __init__(self, io_irrigation):
        super().__init__(callback_object=self)
        self._io_irrigation = io_irrigation

    def on_started(self):
        self._io_irrigation.set_valve_left(True)

    def on_stopped(self):
        self._io_irrigation.set_valve_left(False)


class Timed_valve_right(hal.Timed.Timed):

    def __init__(self, io_irrigation):
        super().__init__(callback_object=self)
        self._io_irrigation = io_irrigation

    def on_started(self):
        self._io_irrigation.set_valve_right(True)

    def on_stopped(self):
        self._io_irrigation.set_valve_right(False)


class Timed_pump(hal.Timed.Timed):

    def __init__(self, io_irrigation):
        super().__init__(callback_object=self)
        self._io_irrigation = io_irrigation

    def on_started(self):
        self._io_irrigation.set_pump(True)

    def on_stopped(self):
        self._io_irrigation.set_pump(False)

