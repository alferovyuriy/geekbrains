# набор чисел рейтинга
my_list = [7, 5, 3, 3, 2]
# запрашиваем у мользователя новое число для рейтинга
element = input('enter new element of rating: ')
# проверяем что введено число
if element.isdigit():
	element = int(element)	# преобразуем строку в число
	for i in range(len(my_list)):	# в цикле пройдемся по индексам списка рейтинга
		# проверяем что элемент списка не последний и меньше нового элемента, тогда вставляем в список
		if i != len(my_list) - 1 and element >= my_list[i]:
			my_list.insert(i, element)
			break
		elif i == len(my_list) - 1:	# иначе если текущий элемент последний, новый элемент добавляем в конец
			my_list.append(element)
	print(my_list)
else:
	print('ValueError')