"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class ZeroDivisionException(Exception):
	"""
	Собственный класс-исключение
	"""
	def __init__(self, message):
		"""
		init error message
		:param message: str
		"""
		self.message = message


try:
	a, b = map(int, input('Enter a and b for division: ').split())
	if b == 0:
		raise ZeroDivisionException('cannot be divided by zero')
	print(f'Result: {a/b}')
except ZeroDivisionException as e:
	print(e)
except ValueError as e:
	print(e)
