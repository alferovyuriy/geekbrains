# просим пользователя задать элементы списка через пробел, преобразуем все в список
elements = input('enter elements separate with space: ').split()
i = 0	# определяем счетчик
# цикл обмена соседних значений списка элементов
while i < len(elements) - 1:
	elements[i], elements[i + 1] = elements[i + 1], elements[i]
	i += 2

print(f'sorted list of elements {elements}')
