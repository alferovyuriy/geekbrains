"""
Читает текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Формирует словарь, содержащий название предмета и общее количество занятий по нему. Выводит словарь на экран.
"""

subjects_dict = {}
try:
	with open('subjects.txt', 'r') as file:
		for line in file.readlines():
			hours = sum([int(elem.split(':')[1]) for elem in line.split()[1:]])
			subjects_dict[line.split()[0]] = hours
		print(f'subjects: {subjects_dict}')
except IOError as e:
	print(e)
