def my_gen(args):
	"""
	возвращает объект генератора, каждый элемент которого не повторяющийся
	:param args: lst
	:return: int
	"""
	for arg in args:
		if args.count(arg) == 1:
			yield arg


my_lst = [8, 2, 1, 4, 3, 2, 1, 5, 3, 2, 0]
unic_items = [arg for arg in my_gen(my_lst)]
print(unic_items)
