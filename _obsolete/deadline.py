import sys
import time


class Deadline:
	def __init__(self, duration_minutes):
		self.deadline = int(time.time()) + (int(duration_minutes) * 60)

	def is_achieved(self):
		return time.time() >= self.deadline
	
