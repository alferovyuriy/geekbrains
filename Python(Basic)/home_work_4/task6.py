from itertools import count, cycle


def count_gen(start, step=1, stop=None):
	"""
	бесконечный итератор, генерирующий целые числа, начиная с указанного
	:param start: int
	:param step: int
	:param stop: int
	:return: int
	"""
	for i in count(start, step):
		if i == stop: break
		else: yield i


def cycle_gen(elements, stop=None):
	"""
	бесконечный итератор, повторяющий элементы заранее определенного списка
	:param elements: iter obj
	:param stop: int
	:return: obj
	"""
	counter = 0
	for element in cycle(elements):
		if counter == stop: break
		else:
			counter += 1
			yield element


for num in count_gen(start=3, stop=10):
	print(num)

for elem in cycle_gen('Hello World!', 12):
	print(elem)
