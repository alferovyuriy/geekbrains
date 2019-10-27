"""
Программа открывает файл на чтение и считывает построчно данные.
Английские числительные заменяются на русские.
Новый блок строк записывается в новый текстовый файл.
"""
replace_table = {
	'One': 'Один',
	'Two': 'Два',
	'Three': 'Три',
	'Four': 'Четыре'
}

try:
	file_read = open('source_text.txt', 'r', encoding='UTF-8')
	file_write = open('modify_text.txt', 'a', encoding='UTF-8')
	for line in file_read.readlines():
		replace_element = line.split()[0]
		modify_line = line.replace(replace_element, replace_table[replace_element])
		file_write.write(modify_line)
	file_read.close()
	file_write.close()
except IOError as e:
	print(e)

