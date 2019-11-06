"""
Создан класс Клетка. В конструкторе класса инициализирован параметр, соответствующий
количеству ячеек клетки (целое число). В классе реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы применяются только к клеткам и выполняют увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно. В методе деления осуществляется
округление значения до целого числа. В классе реализован метод make_order(),
принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод возвращает строку вида *****\n*****\n*****..., где количество ячеек между \n равно
переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
"""


class Cell:
	def __init__(self, cell: int):
		"""
		:param cell: int
		"""
		self.cell = cell

	def __add__(self, other):
		"""
		Объединение двух клеток. Число ячеек общей клетки равняется сумме ячеек исходных двух клеток.
		:param other: Object - instance Cell
		:return: instance Cell
		"""
		if isinstance(other, self.__class__):
			return Cell(self.cell + other.cell)

	def __sub__(self, other):
		"""
		В вычитании участвуют две клетки. Операцию выполняется только если
		разность количества ячеек двух клеток больше нуля, иначе выводится соответствующее сообщение.
		:param other: object class Cell
		:return: instance class Cell
		"""
		if isinstance(other, self.__class__) and self.cell > other.cell:
			return Cell(self.cell - other.cell)
		else:
			print('cell <= 0')

	def __mul__(self, other):
		"""
		Создается общая клетка из двух. Число ячеек общей клетки определяется
		как произведение количества ячеек этих двух клеток.
		:param other: object class Cell
		:return: instance class Cell
		"""
		if isinstance(other, self.__class__):
			return Cell(self.cell * other.cell)

	def __truediv__(self, other):
		"""
		Создается общая клетка из двух. Число ячеек общей клетки определяется
		как целочисленное деление количества ячеек этих двух клеток.
		:param other: object class Cell
		:return: instance class Cell
		"""
		if isinstance(other, self.__class__):
			return Cell(self.cell // other.cell)

	def __str__(self):
		return f'{self.cell}'

	@staticmethod
	def make_order(instance, cell_in_row: int):
		"""
		Метод принимающий экземпляр класса и количество ячеек в ряду.
		Данный метод позволяет организовать ячейки по рядам
		:param instance: object class Cell
		:param cell_in_row: int
		:return: str
		"""
		result = ['*' * cell_in_row for i in range(instance.cell // cell_in_row)]
		if instance.cell % cell_in_row:
			result.append('*' * (instance.cell % cell_in_row))
		return '\n'.join(result)
