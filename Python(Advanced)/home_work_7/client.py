"""
Client
"""


import argparse
import json
import logging
import logs.config_client_log
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import get_message, send_message
from common.constants import ACTION, ACCOUNT_NAME, PRESENCE, TIME, USER, \
    DEFAULT_IP_ADDRESS, DEFAULT_PORT, RESPONSE, ERROR, MESSAGE, MESSAGE_TEXT, SENDER
from decorators import log


# Создаем экземпляр логгера клиента
CLIENT_LOGGER = logging.getLogger('client')


@log
def server_message(message):
    """Read incoming messages"""
    if ACTION in message and message[ACTION] == MESSAGE and SENDER in message \
            and MESSAGE_TEXT in message:
        print(f'Incoming message from user {message[SENDER]}:'
              f'\n{message[MESSAGE_TEXT]}')
    else:
        CLIENT_LOGGER.error(f'Incorrect message from the server {message}')


@log
def create_message(sock, action_type, account_name='Guest'):
    """
    Создает словарь для JIM протокола
    :param sock: сокет клиента
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
    if action_type == MESSAGE:
        message = input('Enter message or \'exit\': ')
        if message == 'exit':
            sock.close()
            CLIENT_LOGGER.info(f'Socket closed by user: {account_name}')
            print('Socket closed, see you later!')
            sys.exit(0)
        output_message[MESSAGE_TEXT] = message
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


@log
def arg_parse():
    """arguments parser"""
    try:
        CLIENT_LOGGER.debug('try to parse args')
        parser = argparse.ArgumentParser()
        parser.add_argument('address', default=DEFAULT_IP_ADDRESS, nargs='?')
        parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
        parser.add_argument('-m', '--mode', default='listen', nargs='?')
        namespaces = parser.parse_args(sys.argv[1:])
        server_address = namespaces.address
        server_port = namespaces.port
        client_mode = namespaces.mode
        CLIENT_LOGGER.debug('Create namespaces')
        if not 1023 < server_port < 65536:
            CLIENT_LOGGER.critical(f'server_port {server_port} out of range')
            sys.exit(1)
        if client_mode not in ('listen', 'send'):
            CLIENT_LOGGER.critical(f'unknown mod {client_mode}')
            sys.exit(1)
        return server_address, server_port, client_mode
    except Exception as e:
        CLIENT_LOGGER.error(f'Error {e}')


def main():
    """
    Основная функция клиента, связывается с сервером, отправляет ему сообщение
    и получает ответ от него.
    :return: None
    """
    CLIENT_LOGGER.info('main() init')
    server_address, server_port, client_mode = arg_parse()
    CLIENT_LOGGER.info(f'Running client with server address: {server_address}; '
                       f'server port: {server_port}; client mode: {client_mode}')

    try:
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((server_address, server_port))
        message_to_server = create_message(client_socket, PRESENCE)
        send_message(client_socket, message_to_server)
        answer = get_answer(get_message(client_socket))
        CLIENT_LOGGER.debug(f'Client connected to server. Server answer: {answer}')
        print('Client connected to server')
    except (ValueError, json.JSONDecodeError) as e:
        CLIENT_LOGGER.error(f'Не удалось декодировать сообщение сервера. {e}')
    except ConnectionRefusedError as error:
        CLIENT_LOGGER.critical(f'fail connect to {server_address}:{server_port} {error}')
    else:
        if client_mode == 'send':
            print('Client mode - send messages')
        else:
            print('Client mode - receiving messages')
        while True:
            if client_mode == 'send':
                try:
                    send_message(client_socket, create_message(client_socket, MESSAGE))
                except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
                    CLIENT_LOGGER.error(f'Lost connection to server {server_address}')
                    sys.exit(1)
            else:
                try:
                    server_message(get_message(client_socket))
                except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
                    CLIENT_LOGGER.error(f'Lost connection to server {server_address}')
                    sys.exit(1)


if __name__ == '__main__':
    main()
