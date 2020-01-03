"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты
из байтовового в строковый тип на кириллице.
"""


import subprocess
import chardet


def ping_res(args):
    """
    функция осуществляет пинг ресурса и выводит преобразованные строки
    :param args: list
    :return: None
    """
    sub_process = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in sub_process.stdout:
        result = chardet.detect(line)
        print(line.decode(result['encoding']))


YANDEX_ARGS = ['ping', 'yandex.ru']
YOUTUBE_ARGS = ['ping', 'youtube.com']
ping_res(YANDEX_ARGS)
ping_res(YOUTUBE_ARGS)
