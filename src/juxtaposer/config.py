# coding: utf-8

import json

from PyQt5.QtCore import QSettings


class Config(object):

	def __init__(self):
		self.column1 = 6
		self.column2 = 14
		self.start = 8
		self.end = 14
		self.window_geometry = None
		self.window_state = None
		self.encoding = "cp1251"
		self.min_ratio = 0.95
		self.version = 1
		self.excepted_words = [
			"январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь",
			"декабрь"]

	def save(self):
		settings = QSettings()
		settings.setValue("column1", self.column1)
		settings.setValue("column2", self.column2)
		settings.setValue("start", self.start)
		settings.setValue("end", self.end)
		settings.setValue("window_geometry", self.window_geometry)
		settings.setValue("window_state", self.window_state)
		settings.setValue("encoding", self.encoding)
		settings.setValue("min_ratio", self.min_ratio)
		settings.setValue("excepted_words", json.dumps(self.excepted_words))
		settings.setValue("version", self.version)

	def load(self):
		settings = QSettings()
		version = self.read_int(settings, "version", 0)
		if version != self.version:
			return
		self.column1 = self.read_int(settings, "column1", self.column1)
		self.column2 = self.read_int(settings, "column2", self.column2)
		self.start = self.read_int(settings, "start", self.start)
		self.end = self.read_int(settings, "end", self.end)
		self.window_geometry = settings.value("window_geometry")
		self.window_state = settings.value("window_state")
		self.encoding = settings.value("encoding", self.encoding)
		self.min_ratio = self.read_float(settings, "min_ratio", self.min_ratio)
		self.excepted_words = json.loads(settings.value("excepted_words", json.dumps(self.excepted_words)))

	@staticmethod
	def read_int(settings, name, default):
		try:
			return int(settings.value(name, default))
		except ValueError:
			return default

	@staticmethod
	def read_float(settings, name, default):
		try:
			return float(settings.value(name, default))
		except ValueError:
			return default
