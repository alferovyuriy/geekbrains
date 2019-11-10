def my_sum(args):
	"""
	суммирует аргументы списка,
	если находит спецсимвол, то суммирует числа до символа,
	возвращает сумму и True/False если находит/не находит спецсимвол
	:param args: list
	:return: int, bool
	"""
	symbol = [args.index(arg) for arg in args if '\\' in arg] # поиск спецсимвола
	if bool(symbol):	# если находим, то берем числа до спецсимвола
		args = args[:symbol[0]]
	args = [int(arg) for arg in args if arg.isdigit()]	# преобразуем в числовое представление
	return sum(args), bool(symbol)	# возвращаем сумму и результат поиска спецсимвола


result = 0
# в цикле просим пользователя ввести числа через пробел
while True:
	numbers = input('enter numbers: ').split(' ')
	func_res, symbol = my_sum(numbers)
	result += func_res	# суммируем числа
	print(f'result: {result}')
	if symbol: break	# выход из цикла если был введен спецсимвол
