# coding: utf-8

import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog, QMessageBox
from PyQt5.QtGui import QColor

from juxtaposer import utility
from juxtaposer.table import Table
from juxtaposer.ui.main_window import Ui_MainWindow
from juxtaposer.config import Config
from juxtaposer.config_dialog import ConfigDialog


class MainWindow(QMainWindow):
	Filter = u"CSV Таблицы *.csv (*.csv);;Все файлы *(*)"
	Red = QColor(255, 200, 200)
	Yellow = QColor(255, 255, 200)
	Green = QColor(200, 255, 200)

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
		self._table = Table()
		self._is_juxtaposed = False

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
		data = self._table.get_data()
		utility.save(data, file_name, self._config.encoding)

	def _load_file(self, file_name):
		try:
			data = utility.read_csv(file_name, self._config.encoding)
			self._table.set_data(data)
			self._is_juxtaposed = False
			self._update_table()
			self._ui.table_widget.resizeColumnsToContents()
			self._ui.table_widget.resizeRowsToContents()
		except Exception as e:
			print(e)
			message = "Не удалось открыть файл. Попробуйте в настройках изменить кодировку"
			QMessageBox.critical(self, self.windowTitle(), message)

	def _update_table(self):
		self._ui.table_widget.setRowCount(len(self._table.rows))
		column_count = len(self._table.rows[0]) if self._table.rows else 0
		self._ui.table_widget.setColumnCount(column_count)
		for row, words in enumerate(self._table.rows):
			color = self.get_color_by_ratio(words.ratio)
			tool_tip = "Совпадение {0}%".format(round(words.ratio * 100, 2))
			for column, word in enumerate(words):
				item = self.create_table_item(word)
				if self._is_juxtaposed:
					item.setToolTip(tool_tip)
					item.setData(Qt.BackgroundColorRole, color)
				self._ui.table_widget.setItem(row, column, item)

	def get_color_by_ratio(self, ratio):
		if ratio >= 1:
			return self.Green
		if ratio < self._config.min_ratio:
			return self.Red
		return self.Yellow

	@staticmethod
	def create_table_item(word):
		item = QTableWidgetItem()
		item.setData(Qt.DisplayRole, word)
		item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
		return item

	def _juxtapose(self):
		self._table.juxtapose(
			self._config.column1, self._config.column2, self._config.start, self._config.end, self._config.min_ratio,
			self._config.excepted_words)
		self._is_juxtaposed = True
		self._update_table()

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
