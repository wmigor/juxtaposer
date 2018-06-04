# coding: utf-8

import os


def compile_ui(file_name, directory):
	py_name = os.path.join(directory, file_name[:-2] + 'py')
	os.system('pyuic5 -o %s %s' % (py_name, file_name))
	remove_resource_import(py_name)


def remove_resource_import(file_name):
	lines = open(file_name).readlines()
	with open(file_name, 'wt') as f:
		for line in lines:
			if 'import resources_rc' not in line:
				f.write(line)


def setup_directory(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
	init = os.path.join(directory, '__init__.py')
	if not os.path.exists(init):
		open(init, 'wt')


def main():
	directory = '../juxtaposer/'
	setup_directory(directory)
	compile_ui('ui/main_window.ui', directory)
	compile_ui('ui/config_dialog.ui', directory)


if __name__ == '__main__':
	main()
