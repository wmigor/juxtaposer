# coding: utf-8

from difflib import SequenceMatcher


class Table(object):

	def __init__(self):
		self.rows = []

	def set_data(self, table):
		self.rows = []
		for row in table:
			self.rows.append(Row(row))

	def get_data(self):
		table = []
		for row in self.rows:
			table.append(list(row))
		return table

	def juxtapose(self, column1, column2, start2, end2, min_ratio, excepted_words):
		for i in range(2):
			last_index = 0
			for index1, row1 in enumerate(self.rows):
				if i == 0:
					row1.ratio = 0.0
				elif i == 1 and row1.ratio >= min_ratio:
					continue
				if column1 < 0 or column1 >= len(row1) or column1 < 0 or column2 >= len(row1):
					continue
				index2_1, ratio1 = self._find_row(row1[column1].lower(), column2, last_index, min_ratio, [])
				name = self._remove_words(row1[column1].lower(), excepted_words)
				index2_2, ratio2 = self._find_row(name, column2, last_index, min_ratio, excepted_words)
				if ratio1 >= ratio2:
					ratio = ratio1
					if ratio >= 1:
						ratio *= 1.1
					index2 = index2_1
				else:
					ratio = ratio2
					index2 = index2_2
				row1.ratio = ratio
				if index2 < 0:
					continue
				last_index += 1
				if index1 != index2:
					self._swap_rows(index1, index2, start2, end2)
		self.rows.sort(key=lambda x: x.ratio, reverse=True)

	@staticmethod
	def _remove_words(text, words):
		for word in words:
			text = text.replace(word.lower(), "")
		return text

	def _find_row(self, name, column, start_index, min_ratio, excepted_words):
		index = -1
		max_ratio = 0
		for i in range(start_index, len(self.rows)):
			row = self.rows[i]
			if column >= len(row):
				continue
			name2 = self._remove_words(row[column].lower(), excepted_words)
			matcher = SequenceMatcher(None, name, name2)
			ratio = matcher.ratio()
			if ratio > max_ratio:
				index = i
				max_ratio = ratio
		return index if max_ratio >= min_ratio else -1, max_ratio

	def _swap_rows(self, index1, index2, start, end):
		if index1 >= len(self.rows) or index2 > len(self.rows):
			return
		row1 = self.rows[index1]
		row2 = self.rows[index2]

		tmp1 = row1[start: end + 1]
		tmp2 = row2[start: end + 1]

		for i, value in enumerate(tmp1):
			row2[start + i] = value
		for i, value in enumerate(tmp2):
			row1[start + i] = value


class Row(list):

	def __init__(self, row):
		list.__init__(self, row)
		self.ratio = 0.0
