"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
«сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл
в формате Unicode и вывести его содержимое.
"""


WORDS = ['сетевое программирование', 'сокет', 'декоратор']
FILE = 'test_file.txt'

with open(FILE, 'w', encoding='utf-8') as file:
    file.writelines('\n'.join(WORDS))
    print(f'file encoding: {file.encoding}')

with open(FILE, encoding='utf-8') as f:
    for line in f:
        print(line, end='')
