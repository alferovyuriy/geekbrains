def division_func(x, y):
	"""
	функция принимает 2 позиционных аргумента и выполняет деление
	:param x: int
	:param y: int
	:return: float
	"""
	try:
		print(f'result: {x / y}')
	except ZeroDivisionError:
		print('try division by zero ')


try:
	num1, num2 = input('enter 2 number for division: ').split()  # запрашиваем у пользователя два числа
	if num1.isdigit() and num2.isdigit():  # проверяем что введены числа
		division_func(int(num1), int(num2))  # передаем в функцию аргументы
except ValueError:
	print('Value must int')
