"""
Server config logger
"""


import sys
import os
import logging
import logging.handlers
from common.constants import LOGGING_LEVEL
sys.path.append('../')

# Задаем путь лог-файлу
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
LOG_FILE_PATH = os.path.join(DIR_PATH, 'server.log')

# Определяем формат сообщения
SERVER_FORMATER = logging.Formatter('%(asctime)s [%(levelname)s] %(filename)s : %(message)s')

# Задаем потоковый обработчик
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(SERVER_FORMATER)
STREAM_HANDLER.setLevel(logging.ERROR)

# задаем файловый обработчик
ROT_FILE_HANDLER = logging.handlers.TimedRotatingFileHandler(LOG_FILE_PATH, encoding='utf8', interval=1, when='D')
ROT_FILE_HANDLER.setFormatter(SERVER_FORMATER)

# Создаем экземпляр логгера сервера
FILE_LOGGER = logging.getLogger('server')
FILE_LOGGER.addHandler(STREAM_HANDLER)
FILE_LOGGER.addHandler(ROT_FILE_HANDLER)
FILE_LOGGER.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
	FILE_LOGGER.critical('Critical Error')
	FILE_LOGGER.error('Error')
	FILE_LOGGER.debug('Debug')
	FILE_LOGGER.info('Info')
