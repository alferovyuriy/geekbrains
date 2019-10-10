viruchka = int(input('Введите выручку: '))
izdergki = int(input('Введите издержки: '))

if izdergki > viruchka:
	print('Убыток: ', izdergki - viruchka)
else:
	pribil = viruchka - izdergki
	print('Прибыль: ', pribil)
	print('Рентабельность: ', pribil/viruchka)
	workers = int(input('Сотрудников в фирме: '))
	print('Прибыль на одного сотрудника: ', pribil/workers)