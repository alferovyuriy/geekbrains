def my_func(*args):
	"""
	функция принимает позиционные аргументы и возвращает сумму двух наибольших
	:param args: tuple
	:return: int
	"""
	c, a, b = sorted(args)  # сортируем стандартной функцией все аргументы
	return a + b


try:
	args = input('enter 3 number: ').split()  # запрашиваем у пользователя три числа
	a, b, c, *_ = [int(arg) for arg in args]  # берем первые три числа
	print(my_func(a, b, c))  # передаем числа в функцию и выводим полученный результат
except ValueError:
	print('value must be digit')
