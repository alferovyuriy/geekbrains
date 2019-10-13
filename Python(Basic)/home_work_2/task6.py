products = []	# список товаров
product = None	# товар
num_product = 0	# номер товара
add_new = None	# ключ проверки добавления нового товара
# цикл добавления новых товаров
while 1:
	add_new = input('add new product? (y/n): ')	# спрашиваем у пользователя добавить товар или выйти
	if add_new == 'y':
		product = {}	# при добавлении нового товара обновляем словарь
		for key in ('name', 'price', 'number', 'unit'):	# проходимся по характеристикам товара
			value = input(f'enter {key}: ')
			if value == '':			# если значение не было задано, то установим None
				value = None
			if value.isdigit():
				value = int(value)
			num_product += 1		# счетчик номера товара
			product[key] = value	# заполняем словарь товара
		products.append((num_product, product))	# добавляем новый товар в список
	else:
		break
print(f'list of products: {products}')
analitics_dict = {}	# словарь аналитики товаров
# внешний цикл по списку кортежей, возвращает номер товара и словарь с характеристиками
for num, prod in products:
	for key, value in prod.items():	# внутренний цикл, проходимся по характеристикам товара, название и значение
		if analitics_dict.get(key) is None:	# проверяем есть ли в аналитическом словаре такая характеристика товара
			analitics_dict.setdefault(key, [])	# если нет, то создаем и устанавливаем базовое значение пустой список
		analitics_dict[key].append(value)	# добавляем по ключу характеристики значения товаров
print(f'analitics: {analitics_dict}')