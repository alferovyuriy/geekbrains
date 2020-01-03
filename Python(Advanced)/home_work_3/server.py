"""
Server
"""


import json
import sys
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import get_message, send_message
from common.constants import ACTION, ACCOUNT_NAME, RESPONSE, MAX_QUEUE_CONN, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT


def create_response(message):
    """
    Принимает декодированное сообщение от клиента и создает ответ клиенту
    :param message: dict
    :return: dict
    """
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
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта.')
        sys.exit(1)
    except ValueError:
        print('В качестве порта может быть указано значение от 1024 до 65535.')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.insex('-a') + 1]
        else:
            listen_address = ''
    except IndexError:
        print('После параметра -\'a\' необходимо указать слушающего сервера.')
        sys.exit(1)

    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind((listen_address, listen_port))
    server_socket.listen(MAX_QUEUE_CONN)

    while True:
        income_socket, income_addr = server_socket.accept()
        try:
            income_message = get_message(income_socket)
            print(f'Incoming message {income_message}')
            message = create_response(income_message)
            send_message(income_socket, message)
            income_socket.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение от клиента.')
            income_socket.close()


if __name__ == '__main__':
    main()
