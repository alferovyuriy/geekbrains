"""
Client
"""


import json
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import get_message, send_message
from common.constants import ACTION, ACCOUNT_NAME, PRESENCE, TIME, USER, \
    DEFAULT_IP_ADDRESS, DEFAULT_PORT, RESPONSE, ERROR


def create_message(action_type, account_name='Guest'):
    """
    Создает словарь для JIM протокола
    :param action_type: метод протокола
    :param account_name: имя аккаунта
    :return: dict
    """
    output_message = {
        ACTION: action_type,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return output_message


def get_answer(message):
    """
    Получает декодированное сообщение от сервера и выводит ответ
    :param message: dict
    :return: str
    """
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    raise ValueError


def main():
    """
    Основная функция клиента, связывается с сервером, отправляет ему сообщение
    и получает ответ от него.
    :return: None
    """
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указано значение от 1024 до 65535.')
        sys.exit(1)

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_address, server_port))
    message_to_server = create_message(PRESENCE)
    send_message(client_socket, message_to_server)
    try:
        answer = get_answer(get_message(client_socket))
        print(f'Server answer: {answer}')
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
