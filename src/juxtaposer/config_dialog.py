# coding: utf-8

from PyQt5.QtWidgets import QDialog

from juxtaposer.ui.config_dialog import Ui_ConfigDialog


class ConfigDialog(QDialog):

	def __init__(self, config, *args, **kwargs):
		QDialog.__init__(self, *args, **kwargs)
		self._ui = Ui_ConfigDialog()
		self._ui.setupUi(self)
		self._config = config
		self._set_values()

	def _set_values(self):
		self._ui.sb_column1.setValue(self._config.column1 + 1)
		self._ui.sb_column2.setValue(self._config.column2 + 1)
		self._ui.sb_start.setValue(self._config.start + 1)
		self._ui.sb_end.setValue(self._config.end + 1)

	def read_values(self):
		self._config.column1 = self._ui.sb_column1.value() - 1
		self._config.column2 = self._ui.sb_column2.value() - 1
		self._config.start = self._ui.sb_start.value() - 1
		self._config.end = self._ui.sb_end.value() - 1
