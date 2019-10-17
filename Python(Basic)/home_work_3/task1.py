# функция принимает 2 позиционных аргумента и выполняет деление
def division_func(x, y):
	result = x / y if y != 0 else y / x
	print(f'result: x/y = {result}')


try:
	num1, num2 = input('enter 2 number: ').split()  # запрашиваем у пользователя два числа
	if num1.isdigit() and num2.isdigit():  # проверяем что введены числа
		division_func(int(num1), int(num2))  # передаем в функцию аргументы
except ValueError:
	print('Value must int')
