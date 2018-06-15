# coding: utf-8

import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog

from juxtaposer import utility
from juxtaposer.ui.main_window import Ui_MainWindow
from juxtaposer.config import Config
from juxtaposer.config_dialog import ConfigDialog


class MainWindow(QMainWindow):
	Filter = u"CSV Таблицы *.csv (*.csv);;Все файлы *(*)"

	def __init__(self, *args, **kwargs):
		QMainWindow.__init__(self, *args, **kwargs)
		self._ui = Ui_MainWindow()
		self._ui.setupUi(self)
		self._connect_signals()
		self._config = Config()
		self._config.load()
		if self._config.window_geometry:
			self.restoreGeometry(self._config.window_geometry)
		if self._config.window_state:
			self.restoreState(self._config.window_state)

	def _connect_signals(self):
		self._ui.act_open.triggered.connect(self.show_open_dialog)
		self._ui.act_juxtapose.triggered.connect(self._juxtapose)
		self._ui.act_save.triggered.connect(self.show_save_dialog)
		self._ui.act_config.triggered.connect(self.show_config_dialog)

	def closeEvent(self, event):
		self._config.window_geometry = self.saveGeometry()
		self._config.window_state = self.saveState()
		self._config.save()

	def show_open_dialog(self):
		file_name, filter_ = QFileDialog().getOpenFileName(self, filter=self.Filter)
		if not file_name:
			return
		self._load_file(file_name)

	def show_save_dialog(self):
		file_name, filter_ = QFileDialog().getSaveFileName(self, filter=self.Filter)
		if not file_name:
			return
		ext = os.path.splitext(file_name.lower())[1]
		if not ext:
			file_name += '.csv'
		table = self._read_table()
		utility.save(table, file_name, self._config.encoding)

	def _load_file(self, file_name):
		table = utility.read_csv(file_name, self._config.encoding)
		self.set_table(table)

	def set_table(self, table):
		self._ui.table_widget.setRowCount(len(table))
		column_count = len(table[0]) if table else 0
		self._ui.table_widget.setColumnCount(column_count)
		for row, words in enumerate(table):
			for column, word in enumerate(words):
				item = self.create_table_item(word)
				self._ui.table_widget.setItem(row, column, item)

	@staticmethod
	def create_table_item(word):
		item = QTableWidgetItem()
		item.setData(Qt.DisplayRole, word)
		item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
		return item

	def _juxtapose(self):
		table = self._read_table()
		utility.juxtapose(
			table, self._config.column1, self._config.column2, self._config.start, self._config.end,
			self._config.min_ratio)
		utility.push_different(table, self._config.column1, self._config.column2, self._config.min_ratio)
		self.set_table(table)

	def _read_table(self):
		table = []
		for row in range(self._ui.table_widget.rowCount()):
			words = []
			for column in range(self._ui.table_widget.columnCount()):
				item = self._ui.table_widget.item(row, column)
				word = item.text()
				words.append(word)
			table.append(words)
		return table

	def show_config_dialog(self):
		dialog = ConfigDialog(self._config)
		if dialog.exec_():
			dialog.read_values()
