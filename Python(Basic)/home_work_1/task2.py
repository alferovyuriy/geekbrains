# coding: utf8
# запрашиваем у пользователя число
number = input('enter Number: ')
# проверяем что введено число
if number.isdigit():
	# вычисляем сумму и выводим результат
	summa = int(number) + int(2*number) + int(3*number)
	print('summa: ', summa)
else:
	print('ValueError')	# если введено не число