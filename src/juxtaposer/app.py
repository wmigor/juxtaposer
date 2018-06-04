# coding: utf-8

import sys

from PyQt5.QtWidgets import QApplication

from juxtaposer import resources


class App(QApplication):

	def __init__(self):
		QApplication.__init__(self, sys.argv)
		self.setApplicationName("juxtaposer")
		self.setOrganizationName("iakulov")