# зададим список элементов разного типа
elements = ['string', 1, 3.14, True, None, (1, 'a', False), [9.8, 'spam']]
# цикл определения типа элемента
for element in elements:
	print(f'type of element: {type(element)}')