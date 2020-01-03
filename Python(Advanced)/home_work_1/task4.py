"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового
представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""


WORDS = ['разработка', 'администрирование', 'protocol', 'standard']
ENCODED_WORDS = [word.encode('utf-8') for word in WORDS]
RECODED_WORDS = [word.decode('utf-8') for word in ENCODED_WORDS]
