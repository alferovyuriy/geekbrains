"""
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе используя маркировку b.
"""


def check_convert(word):
    """
    функция проверки конвертации строки в байтовый тип, т.е. состоит ли она из символов ascii
    :param word: str
    :return: str, None
    """
    try:
        word.encode('ascii')
    except UnicodeEncodeError:
        return word
    return None


WORDS = ['attribute', 'класс', 'функция', 'type']

NOT_CONVERTED = [word for word in WORDS if check_convert(word)]
