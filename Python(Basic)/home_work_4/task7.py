from sys import argv
from functools import reduce


def fibo_gen(n):
	"""
	генератор получет число факториала, создает очередное значение
	:param n: int
	:return: int
	"""
	facorial = reduce(lambda a, b: a * b, list(range(1, n + 1)))
	for arg in range(1, facorial + 1):
		yield arg


try:
	script_name, factorial = argv	# значение факториала указывается при запуске
	factorial = int(factorial)		# проверяем и проебразуем в числовое значение
except ValueError as e:
	print(e)

# выводим первые 15 чисел
for el in fibo_gen(factorial):
	if el > 15: break
	print(el)
