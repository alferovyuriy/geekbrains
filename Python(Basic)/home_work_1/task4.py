# просим ввести выручку и издержки
proceeds = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))
# проверяем финансовый результат
if costs > proceeds:
	print('Убыток: ', costs - proceeds)	# убыток фирмы
else:
	profit = proceeds - costs	# вычисляем прибыль
	print('Прибыль: ', profit)
	print('Рентабельность: ', profit/proceeds)	# вычисляем и выводим рентабельность
	workers = int(input('Сотрудников в фирме: '))	# запрашиваем кол-во сотрудников в фирме
	print('Прибыль на одного сотрудника: ', profit/workers)	# определяем и выводим прибыль на сотрудника