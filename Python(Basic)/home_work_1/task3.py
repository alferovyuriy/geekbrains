# coding: utf8
# просим ввести целое положительное число
number = int(input('enter Number > 0: '))
# задаем базавое значение максимальной цифры
nmax = 0
# цикл определения максимальной цифры в числе
while 1:
	nnext = number % 10	# берем цифру для сравнения с максимальным
	numbers = number // 10	# оставшиеся цисла для проверки

	if nnext > nmax: nmax = nnext	# сравниваем с максимальным
	if numbers == 0: break	# если цифры кончились, то выходим из цикла
	number = number // 10	# оставшиеся числа для следующей итерации
# вывод результата
print('max: %s' % (nmax))