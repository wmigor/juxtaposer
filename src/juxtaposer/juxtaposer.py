# coding: utf-8

import sys
import csv
import os

Column1 = 3
Column2 = 8
MoveColumnStart = 5
MoveColumnEnd = 8


def read_csv(file_name):
	table = []
	with open(file_name, "rb") as f:
		reader = csv.reader(f)
		for row in reader:
			table.append(row)
	return table


def save(table, file_name):
	with open(file_name, "wb") as f:
		writer = csv.writer(f)
		for row in table:
			writer.writerow(row)


def find_row(table, name, column, start_index):
	for i in xrange(start_index, len(table)):
		row = table[i]
		if column >= len(row):
			continue
		if name == row[column]:
			return i
	return -1


def swap_rows(table, index1, index2, start, end):
	if index1 >= len(table) or index2 > len(table):
		return
	row1 = table[index1]
	row2 = table[index2]

	tmp1 = row1[start: end + 1]
	tmp2 = row2[start: end + 1]

	for i, value in enumerate(tmp1):
		row2[start + i] = value
	for i, value in enumerate(tmp2):
		row1[start + i] = value


def juxtapose(table, column1, column2, start2, end2):
	for index1, row1 in enumerate(table):
		if column1 < 0 or column1 >= len(row1) or column1 < 0 or column2 >= len(row1):
			continue
		name = row1[column1]
		index2 = find_row(table, name, column2, index1)
		if index2 < 0 or index1 == index2:
			continue
		swap_rows(table, index1, index2, start2, end2)


def push_different(table, column1, column2):
	i = 0
	count = len(table)
	for step in xrange(count):
		row = table[i]
		if column1 < 0 or column2 < 0 or column1 >= len(row) or column2 > len(row):
			continue
		if row[column1] != row[column2]:
			table.append(table.pop(i))
		else:
			i += 1


def print_table(table):
	for row in table:
		for word in row:
			print word,
		print


def get_out_file_name(file_name):
	directory = os.path.dirname(file_name)
	out_file_name = os.path.basename(file_name)
	name, ext = os.path.splitext(out_file_name)
	return os.path.join(directory, name + u"_converted" + ext)


def input_int(text, default):
	print u"%s [%s]:" % (text, default),
	value = raw_input()
	try:
		return int(value)
	except ValueError:
		return default


def main():
	file_name = sys.argv[1] if len(sys.argv) > 1 else ""
	while True:
		if not file_name:
			print u"Введите путь к файлу:",
			file_name = raw_input()
		if not file_name:
			break
		if not os.path.exists(file_name):
			print u"Файл не существует"
			file_name = ""
			continue
		column1 = input_int(u"Столбец первой таблицы для сравнивания", Column1 + 1) - 1
		column2 = input_int(u"Столбец второй таблицы для сравнивания", Column2 + 1) - 1
		start = input_int(u"Первый столбец второй таблицы", MoveColumnStart + 1) - 1
		end = input_int(u"Последний столбец второй таблицы", MoveColumnEnd + 1) - 1
		table = read_csv(file_name)
		juxtapose(table, column1, column2, start, end)
		push_different(table, column1, column2)
		out_file_name = get_out_file_name(file_name)
		save(table, out_file_name)
		print u"Создан файл " + out_file_name
		file_name = ""
	print u"Пока"


if __name__ == '__main__':
	main()