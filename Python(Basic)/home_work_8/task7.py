"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class MyTypeError(Exception):
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return self.message


class ComplexNum:
	""" класс «Комплексное число» """
	def __init__(self, a=0, b=0):
		""" инициализация закрытого атрибута комплексного числа """
		self._num = complex(a, b)

	@property
	def num(self):
		return self._num

	def __add__(self, other):
		"""
		перегрузка метода сложения комплексных чисел
		:param other: complex, ComplexNum instance
		:return: new instance ComplexNum
		"""
		try:	# валидация аргументов
			if isinstance(other, ComplexNum):
				return ComplexNum(self.num + other.num)
			elif isinstance(other, complex):
				return ComplexNum(self.num + other)
			raise MyTypeError('Value must be complex type')
		except MyTypeError as e:
			print(e)

	def __mul__(self, other):
		"""
		перегрузка метода умножения комплексных чисел
		:param other: complex, ComplexNum instance
		:return: new instance ComplexNum
		"""
		try:
			if isinstance(other, ComplexNum):
				return ComplexNum(self.num * other.num)
			elif isinstance(other, complex):
				return ComplexNum(self.num * other)
			raise MyTypeError('Value must be complex type')
		except MyTypeError as e:
			print(e)

	def __str__(self):
		return f'{self._num}'


if __name__ == '__main__':
	x = ComplexNum(1, 2)
	y = ComplexNum(3, 4)
	print(x + y)
	print(x * y)
	print(x + 1)
	print(x + complex(5, 6))
