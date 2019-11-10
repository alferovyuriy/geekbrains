def gen_source_list(lst):
	"""
	принимает итерируемый объект и возвращает генератор
	:param lst: list
	:return: int
	"""
	for item in lst:
		yield item


lst = [5, 2, 2, 8, 6, 3, 8, 0]
source_lst = {arg for arg in gen_source_list(lst)}
print(f'source list: {source_lst}')
