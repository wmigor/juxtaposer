# coding: utf-8

import csv
import os


def read_csv(file_name, encoding):
	table = []
	with open(file_name, "r", encoding=encoding) as f:
		reader = csv.reader(f)
		for row in reader:
			table.append(row)
	return table


def save(table, file_name, encoding):
	with open(file_name, "w", encoding=encoding, newline="") as f:
		writer = csv.writer(f)
		for row in table:
			writer.writerow(row)


def get_out_file_name(file_name):
	directory = os.path.dirname(file_name)
	out_file_name = os.path.basename(file_name)
	name, ext = os.path.splitext(out_file_name)
	return os.path.join(directory, name + u"_converted" + ext)
