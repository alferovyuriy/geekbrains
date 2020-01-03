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
from threading import Thread
from common.utils import get_message, send_message
from common.constants import ACTION, ACCOUNT_NAME, PRESENCE, TIME, USER, \
    DEFAULT_IP_ADDRESS, DEFAULT_PORT, RESPONSE, ERROR, MESSAGE, MESSAGE_TEXT, SENDER
from decorators import log


# Создаем экземпляр логгера клиента
CLIENT_LOGGER = logging.getLogger('client')


@log
def server_message(sock):
    """Read incoming messages"""
    while True:
        message = get_message(sock)
        if ACTION in message and message[ACTION] == MESSAGE and SENDER in message \
                and MESSAGE_TEXT in message:
            print(f'Incoming message from user {message[SENDER]}:'
                  f'\n{message[MESSAGE_TEXT]}')
        else:
            CLIENT_LOGGER.error(f'Incorrect message from the server {message}')


def create_output_message(sock, action_type, account_name, message='', to_user='Guest'):
    CLIENT_LOGGER.info('Creating output message')
    ontime = time.time()
    output_message = {
        ACTION: action_type,
        TIME: ontime,
        SENDER: account_name
    }
    if action_type == MESSAGE:
        output_message[MESSAGE_TEXT] = message
        output_message[USER] = to_user
    send_message(sock, output_message)


@log
def create_message(sock, action_type, account_name='Guest'):
    """
    Создает словарь для JIM протокола
    :param sock: сокет клиента
    :param action_type: метод протокола
    :param account_name: имя аккаунта
    :return: dict
    """
    while True:
        message = input('Enter message or \'exit\': ')
        if message == 'exit':
            CLIENT_LOGGER.info(f'Socket closed by user: {account_name}')
            print('Socket closed, see you later!')
            break
        to_user = input('Enter user name for send message: ')
        create_output_message(sock, MESSAGE, account_name, message, to_user)
        CLIENT_LOGGER.debug(f'create_message with ACTION: {action_type}, TIME: '
                            f'{time.ctime()}, ACCOUNT_NAME: {account_name}')


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
            print('Client connected to the server')
            return '200 : OK'
        print('Connection error')
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
        parser.add_argument('-n', '--name', default='Guest', nargs='?')
        namespaces = parser.parse_args(sys.argv[1:])
        server_address = namespaces.address
        server_port = namespaces.port
        client_name = namespaces.name
        CLIENT_LOGGER.debug('Create namespaces')
        if not 1023 < server_port < 65536:
            CLIENT_LOGGER.critical(f'server_port {server_port} out of range')
            sys.exit(1)
        return server_address, server_port, client_name
    except Exception as e:
        CLIENT_LOGGER.error(f'Error {e}')


def main():
    """
    Основная функция клиента, связывается с сервером, отправляет ему сообщение
    и получает ответ от него.
    :return: None
    """
    CLIENT_LOGGER.info('main() init')
    print('main() init')
    server_address, server_port, client_name = arg_parse()
    CLIENT_LOGGER.info(f'Running client with server address: {server_address}; '
                       f'server port: {server_port}; client name: {client_name}')

    try:
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((server_address, server_port))
        create_output_message(client_socket, PRESENCE, client_name)
        # send_message(client_socket, message_to_server)
        answer = get_answer(get_message(client_socket))
        CLIENT_LOGGER.debug(f'Client connected to server. Server answer: {answer}')
        print('Client connected to server')
    except (ValueError, json.JSONDecodeError) as e:
        CLIENT_LOGGER.error(f'Не удалось декодировать сообщение сервера. {e}')
    except ConnectionRefusedError as error:
        CLIENT_LOGGER.critical(f'fail connect to {server_address}:{server_port} {error}')
    else:
        print(f'User name: {client_name}')

        send_process = Thread(target=create_message, args=(client_socket, MESSAGE, client_name))
        send_process.daemon = True
        send_process.start()

        recv_process = Thread(target=server_message, args=(client_socket,))
        recv_process.daemon = True
        recv_process.start()

        while True:
            time.sleep(1)
            if send_process.is_alive() and recv_process.is_alive():
                continue
            break


if __name__ == '__main__':
    main()
