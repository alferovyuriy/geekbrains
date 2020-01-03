"""
Server
"""


import argparse
import logging
import logs.config_server_log
import sys
import time
from select import select
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import get_message, send_message
from common.constants import ACTION, ACCOUNT_NAME, RESPONSE, MAX_QUEUE_CONN, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, MESSAGE, MESSAGE_TEXT, SENDER
from decorators import Log


# Создаем экземпляр логгера сервера
SERVER_LOGGER = logging.getLogger('server')


@Log()
def create_response(message, messages, client):
    """
    Принимает декодированное сообщение от клиента и создает ответ клиенту
    :param message: dict
    :param messages: list
    :param client: client socket
    :return: None
    """
    SERVER_LOGGER.info('create_response')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
                and USER in message and message[USER][ACCOUNT_NAME] == 'Guest':
        send_message(client, {RESPONSE: 200})
        return
    elif ACTION in message and message[ACTION] == MESSAGE and TIME in message \
                and MESSAGE_TEXT in message:
        messages.append((message[USER][ACCOUNT_NAME], message[MESSAGE_TEXT]))
        SERVER_LOGGER.info('Response added to messages')
    else:
        send_message(client, {
            RESPONSE: 400,
            ERROR: 'Bad Request'
        })
        return


@Log()
def new_listen_socket(address):
    """create listening socket"""
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(MAX_QUEUE_CONN)
    sock.settimeout(0.5)
    SERVER_LOGGER.info('Server socket created')
    return sock


@Log()
def arg_parse():
    """arguments parser"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', default=DEFAULT_PORT, nargs='?')
    parser.add_argument('-a', default='', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    listen_address = namespace.a
    listen_port = namespace.p

    if listen_port < 1024 or listen_port > 65535:
        SERVER_LOGGER.critical(f'Incorrect port: {listen_port}')
        sys.exit(1)

    return listen_address, listen_port


def main():
    """
    Основная функция сервера, создает сокет сервера и прослушиватель для входящих обращений,
    обрабатывает входящие обращения
    :return: None
    """
    SERVER_LOGGER.info('main() init')
    listen_address, listen_port = arg_parse()
    SERVER_LOGGER.info(f'Running server with address: {listen_address}, port: {listen_port}')

    server_socket = new_listen_socket((listen_address, listen_port))

    clients = []
    send_messages = []
    while True:
        try:
            income_socket, income_addr = server_socket.accept()
            SERVER_LOGGER.debug(f'income_socket {income_socket}, income_addr {income_addr}')
        except OSError:
            pass
        else:
            SERVER_LOGGER.info(f'connect with {income_addr}')
            clients.append(income_socket)

        clients_read = []
        clients_write = []
        clients_error = []
        try:
            clients_read, clients_write, clients_error = select(clients, clients, [], 0)
        except OSError:
            pass

        if len(clients_read):
            for client in clients_read:
                try:
                    create_response(get_message(client), send_messages, client)
                except:
                    SERVER_LOGGER.info(f'Client {client.getpeername()} disconnected from the server')
                    clients.remove(client)

        if len(send_messages) and len(clients_write):
            message = {
                ACTION: MESSAGE,
                SENDER: send_messages[0][0],
                TIME: time.time(),
                MESSAGE_TEXT: send_messages[0][1]
            }
            del send_messages[0]
            for client in clients_write:
                try:
                    send_message(client, message)
                except:
                    SERVER_LOGGER.info(f'Client {client.getpeername()} disconnected from the server')
                    clients.remove(client)


if __name__ == '__main__':
    main()
