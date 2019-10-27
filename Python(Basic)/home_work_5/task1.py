"""
Создает программно файл в текстовом формате, записывает в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

data = []
while True:
	text = input()
	if text == '': break
	data.append(text)

try:
	with open('text_file.txt', 'a') as file:
		file.write('\n'.join(data))
except IOError as e:
	print(e)
