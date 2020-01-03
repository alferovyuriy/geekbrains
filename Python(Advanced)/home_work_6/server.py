"""
Server
"""


import json
import sys
import logging
import logs.config_server_log
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import get_message, send_message
from common.constants import ACTION, ACCOUNT_NAME, RESPONSE, MAX_QUEUE_CONN, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT
from decorators import Log


# Создаем экземпляр логгера сервера
SERVER_LOGGER = logging.getLogger('server')


@Log()
def create_response(message):
    """
    Принимает декодированное сообщение от клиента и создает ответ клиенту
    :param message: dict
    :return: dict
    """
    SERVER_LOGGER.info('create_response')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
                and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    """
    Основная функция сервера, создает сокет сервера и прослушиватель для входящих обращений,
    обрабатывает входящие обращения
    :return: None
    """
    SERVER_LOGGER.info('main() init')
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        SERVER_LOGGER.debug(f'listen_port {listen_port}')
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError as e:
        SERVER_LOGGER.error(f'После параметра -\'p\' необходимо указать номер порта. {e}')
        sys.exit(1)
    except ValueError as err:
        SERVER_LOGGER.error(f'В качестве порта может быть указано значение от 1024 до 65535. {err}')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.insex('-a') + 1]
        else:
            listen_address = ''
        SERVER_LOGGER.debug(f'listen_address {listen_address}')
    except IndexError as error:
        SERVER_LOGGER.error(f'После параметра -\'a\' необходимо указать слушающего сервера. {error}')
        sys.exit(1)

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((listen_address, listen_port))
    server_socket.listen(MAX_QUEUE_CONN)

    while True:
        income_socket, income_addr = server_socket.accept()
        SERVER_LOGGER.debug(f'income_socket {income_socket}, income_addr {income_addr}')
        try:
            income_message = get_message(income_socket)
            SERVER_LOGGER.debug(f'Incoming message {income_message}')
            message = create_response(income_message)
            send_message(income_socket, message)
            income_socket.close()
        except (ValueError, json.JSONDecodeError) as er:
            SERVER_LOGGER.error(f'Принято некорректное сообщение от клиента. {er}')
            income_socket.close()


if __name__ == '__main__':
    main()
