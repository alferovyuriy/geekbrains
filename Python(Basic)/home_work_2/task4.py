# просим пользователя ввести несколько слов разделяя их пробелами
words = input('Enter some words separate with space: ')
# проверяем что пользователь что-то ввел
if words != '':
	words = words.split()	# преобразуем в список
	for i in range(len(words)):	# в цикле будем проходить по индексам списка
		if len(words[i]) > 10:	# проверяем что элемент не более 10 символов
			words[i] = words[i][:10]	# если больше, то обрезаем
		print(f'{i} {words[i]}')	# вывод с нумерованием строки
else:
	print('No words')