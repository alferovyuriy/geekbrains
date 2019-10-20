def my_func(x: float, y: int):
	"""
	возводит x в степень y
	:param x: float
	:param y: int
	:return: float
	"""
	result = 1
	for i in range(abs(y)):
		result *= x
	if y < 0:
		return 1 / result
	return result


x = float(input('enter float X: '))
y = int(input('enter Y < 0 : '))
print(f'result: {my_func(x, y)}')
