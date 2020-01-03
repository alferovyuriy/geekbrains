"""
Client config logger
"""


import sys
import os
import logging
from common.constants import LOGGING_LEVEL
sys.path.append('../')

# Задаем путь лог-файлу
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(DIR_PATH, 'client.log')

# Определяем формат сообщения
CLIENT_FORMATER = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s %(message)s')

# Задаем потоковый обработчик
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(CLIENT_FORMATER)
STREAM_HANDLER.setLevel(logging.ERROR)

# задаем файловый обработчик
FILE_HANDLER = logging.FileHandler(LOG_FILE_PATH, encoding='utf8')
FILE_HANDLER.setFormatter(CLIENT_FORMATER)

# Создаем экземпляр логгера клиента
FILE_LOGGER = logging.getLogger('client')
FILE_LOGGER.addHandler(STREAM_HANDLER)
FILE_LOGGER.addHandler(FILE_HANDLER)
FILE_LOGGER.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
	FILE_LOGGER.critical('Critical Error')
	FILE_LOGGER.error('Error')
	FILE_LOGGER.debug('Debug')
	FILE_LOGGER.info('Info')
