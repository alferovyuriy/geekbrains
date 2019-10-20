from functools import reduce


def my_gen(args):
	"""
	генератор определет четные числа последовательности
	:param args: lst
	:return: int
	"""
	for arg in args:
		if arg % 2 == 0:
			yield arg


my_lst = [item for item in my_gen(list(range(100, 1001)))]
result = reduce(lambda a, b: a * b, my_lst)
