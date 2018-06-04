# coding: utf-8

from PyQt5.QtCore import QSettings


class Config(object):

	def __init__(self):
		self.column1 = 3
		self.column2 = 8
		self.start = 5
		self.end = 8
		self.window_geometry = None
		self.window_state = None

	def save(self):
		settings = QSettings()
		settings.setValue("column1", self.column1)
		settings.setValue("column2", self.column2)
		settings.setValue("start", self.start)
		settings.setValue("end", self.end)
		settings.setValue("window_geometry", self.window_geometry)
		settings.setValue("window_state", self.window_state)

	def load(self):
		settings = QSettings()
		self.column1 = self.read_int(settings, "column1", self.column1)
		self.column2 = self.read_int(settings, "column2", self.column2)
		self.start = self.read_int(settings, "start", self.start)
		self.end = self.read_int(settings, "end", self.end)
		self.window_geometry = settings.value("window_geometry")
		self.window_state = settings.value("window_state")

	@staticmethod
	def read_int(settings, name, default):
		try:
			return int(settings.value(name, default))
		except ValueError:
			return default
