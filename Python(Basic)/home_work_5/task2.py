"""
Выполняет подсчет количества строк, количества слов в каждой строке.
"""
try:
	with open('text_file.txt', 'r') as file:
		for i, string in enumerate(file.readlines(), 1):
			print(f"line {i} words:{len(string.split())}")
except IOError as e:
	print(e)
