import io_relays.Timed


class Timed_valve_left(io_relays.Timed.Timed):

    def __init__(self, io_irrigation):
        super().__init__(callback_object=self)
        self._io_irrigation = io_irrigation

    def on_started(self):
        self._io_irrigation.set_valve_left(True)

    def on_stopped(self):
        self._io_irrigation.set_valve_left(False)


class Timed_valve_right(io_relays.Timed.Timed):

    def __init__(self, io_irrigation):
        super().__init__(callback_object=self)
        self._io_irrigation = io_irrigation

    def on_started(self):
        self._io_irrigation.set_valve_right(True)

    def on_stopped(self):
        self._io_irrigation.set_valve_right(False)


class Timed_valve_drip(io_relays.Timed.Timed):

    def __init__(self, io_irrigation):
        super().__init__(callback_object=self)
        self._io_irrigation = io_irrigation

    def on_started(self):
        self._io_irrigation.set_valve_drip(True)

    def on_stopped(self):
        self._io_irrigation.set_valve_drip(False)


class Timed_pump(io_relays.Timed.Timed):

    def __init__(self, io_irrigation):
        super().__init__(callback_object=self)
        self._io_irrigation = io_irrigation

    def on_started(self):
        self._io_irrigation.set_pump(True)

    def on_stopped(self):
        self._io_irrigation.set_pump(False)


class Timed_valve_refill(io_relays.Timed.Timed):

    def __init__(self, io_irrigation):
        super().__init__(callback_object=self)
        self._io_irrigation = io_irrigation

    def on_started(self):
        self._io_irrigation.set_valve_refill(True)

    def on_stopped(self):
        self._io_irrigation.set_valve_refill(False)


class Timed_valve_filter(io_relays.Timed.Timed):

    def __init__(self, io_irrigation):
        super().__init__(callback_object=self)
        self._io_irrigation = io_irrigation

    def on_started(self):
        self._io_irrigation.set_valve_filter(True)

    def on_stopped(self):
        self._io_irrigation.set_valve_filter(False)


class Timed_valve_sewage(io_relays.Timed.Timed):

    def __init__(self, io_irrigation):
        super().__init__(callback_object=self)
        self._io_irrigation = io_irrigation

    def on_started(self):
        self._io_irrigation.set_valve_sewage(True)

    def on_stopped(self):
        self._io_irrigation.set_valve_sewage(False)


class Timed_sensors(io_relays.Timed.Timed):

    def __init__(self, io_irrigation):
        super().__init__(callback_object=self)
        self._io_irrigation = io_irrigation

    def on_started(self):
        self._io_irrigation.set_sensors(True)

    def on_stopped(self):
        self._io_irrigation.set_sensors(False)
