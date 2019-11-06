"""
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
"""


class MyException(Exception):
	"""
	собственный класс-исключение
	"""
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return self.message


my_list = []
while True:
	try:
		value = input('Enter digit (q - for exit): ')
		if value == 'q':	# если ввели 'q', то цикл завершается и выводится получившийся список
			print(f'Result: {my_list}')
			break
		if not value.isdigit():	# если введено не число, то возбуждается исключение
			raise MyException('Type of value must be digit')
		my_list.append(float(value)) if '.' in value else my_list.append(int(value))
	except MyException as e:
		print(e)
