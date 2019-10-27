"""
Записает в файл набор чисел, разделенных пробелами.
Программа подсчитывает сумму чисел в файле и выводит ее на экран.
"""

numbers = input('enter numbers: ')
try:
	with open('numbers.txt', 'w') as write_file:
		write_file.write(numbers)
	with open('numbers.txt', 'r') as read_file:
		numbers_sum = sum([int(elem) for elem in read_file.readline().split() if elem.isdigit()])
	print(f'sum: {numbers_sum}')
except IOError as e:
	print(e)
