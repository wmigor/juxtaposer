# coding: utf-8

import sys

from juxtaposer.app import App
from juxtaposer.main_window import MainWindow


def main():
	app = App()
	main_window = MainWindow()
	main_window.show()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
