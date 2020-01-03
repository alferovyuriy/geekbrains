"""Constants"""


import logging


# Порт используемый поумолчанию для сетевого взаимодействия
DEFAULT_PORT = 7777
# IP адрес используемый поумолчанию для подключения клиента
DEFAULT_IP_ADDRESS = '127.0.0.1'
# Максимальная очередь подключений
MAX_QUEUE_CONN = 5
# Максимальный размер покета в байтах
MAX_PACK_SIZE = 1024
# Тип кодировки
ENCODING_TYPE = 'utf-8'

# Основные константы для JIM протокола
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACCOUNT_NAME = 'account_name'
SENDER = 'sender'

# Прочие константы для JIM протокола
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
MESSAGE = 'message'
MESSAGE_TEXT = 'mess_text'

# Константы для логирования
LOGGING_LEVEL = logging.DEBUG
