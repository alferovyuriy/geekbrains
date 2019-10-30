"""
Реализован класс Matrix (матрица). Реализована перегрузка конструктора класса (метод __init__()),
который принимает данные (список списков) для формирования матрицы. Реализована перегрузка метода
__str__() для вывода матрицы в привычном виде. Реализована перегрузка метода __add__()
для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения является новая матрица.
"""


class Matrix:
	"""
	класс Matrix (матрица)
	"""
	def __init__(self, args):
		"""
		перегрузка конструктора класса, принимает данные (список списков) для формирования матрицы
		:param args: list
		"""
		self.args = args

	def __str__(self):
		"""
		перегрузка метода __str__() для вывода матрицы в привычном виде
		:return: str
		"""
		return '\n'.join([' '.join([str(item) for item in arg]) for arg in self.args])

	def __add__(self, other):
		"""
		перегрузка метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
		:param other: list
		:return: instance
		"""
		sum_args = [[self.args[i][j] + other.args[i][j] for j, item in enumerate(args)] \
					for i, args in enumerate(self.args)]
		return Matrix(sum_args)
