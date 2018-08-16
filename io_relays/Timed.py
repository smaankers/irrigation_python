import threading


class Timed(object):

    def __init__(self, callback_object):
        self._running      = False
        self._callback_object = callback_object
        self._timer = None

    #def __del__(self):
    #    if self._timer is not None:
    #        self._timer.cancel()

    def start(self, time_in_seconds):
        if self._timer is not None:
            self._timer.cancel()

        self._running = True
        self._callback_object.on_started()

        self._timer = threading.Timer(time_in_seconds, self.stop)
        self._timer.start()

    def stop(self):
        if self._timer is not None:
            self._timer.cancel()

        if self.is_running():
            self._callback_object.on_stopped()

        self._running = False

    def is_running(self):
        return self._running
