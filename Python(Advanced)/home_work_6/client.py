"""
Client
"""


import json
import sys
import time
import logging
import logs.config_client_log
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import get_message, send_message
from common.constants import ACTION, ACCOUNT_NAME, PRESENCE, TIME, USER, \
    DEFAULT_IP_ADDRESS, DEFAULT_PORT, RESPONSE, ERROR
from decorators import log


# Создаем экземпляр логгера клиента
CLIENT_LOGGER = logging.getLogger('client')


@log
def create_message(action_type, account_name='Guest'):
    """
    Создает словарь для JIM протокола
    :param action_type: метод протокола
    :param account_name: имя аккаунта
    :return: dict
    """
    ontime = time.time()
    output_message = {
        ACTION: action_type,
        TIME: ontime,
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    CLIENT_LOGGER.debug(f'create_message with ACTION: {action_type}, TIME: {ontime}, ACCOUNT_NAME: {account_name}')
    return output_message


@log
def get_answer(message):
    """
    Получает декодированное сообщение от сервера и выводит ответ
    :param message: dict
    :return: str
    """
    CLIENT_LOGGER.debug(f'get_answer with message: {message}')
    if RESPONSE in message:
        if message[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {message[ERROR]}'
    CLIENT_LOGGER.error(f'Response {RESPONSE} not in message {message}')
    raise ValueError


def main():
    """
    Основная функция клиента, связывается с сервером, отправляет ему сообщение
    и получает ответ от него.
    :return: None
    """
    CLIENT_LOGGER.info('main() init')
    try:
        CLIENT_LOGGER.debug('try get args from sys.argv')
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            CLIENT_LOGGER.error(f'server_port {server_port} out of range')
            raise ValueError
    except IndexError as err:
        CLIENT_LOGGER.error(f'IndexError: {err}')
        server_address = DEFAULT_IP_ADDRESS
        server_port = DEFAULT_PORT
        CLIENT_LOGGER.debug(f'server_address {server_address}, server_port{server_port}')
    except ValueError as e:
        CLIENT_LOGGER.error('В качестве порта может быть указано значение от 1024 до 65535.')
        sys.exit(1)

    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_address, server_port))
    message_to_server = create_message(PRESENCE)
    send_message(client_socket, message_to_server)
    try:
        answer = get_answer(get_message(client_socket))
        CLIENT_LOGGER.debug(f'Server answer: {answer}')
    except (ValueError, json.JSONDecodeError) as e:
        CLIENT_LOGGER.error(f'Не удалось декодировать сообщение сервера. {e}')
    except ConnectionRefusedError as error:
        CLIENT_LOGGER.critical(f'fail connect to {server_address}:{server_port} {error}')


if __name__ == '__main__':
    main()
