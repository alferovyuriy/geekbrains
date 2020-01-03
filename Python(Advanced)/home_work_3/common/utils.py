"""Utils"""


import json
from common.constants import MAX_PACK_SIZE, ENCODING_TYPE


def get_message(income_socket):
    """
    Функция декодирования сообщения из bytes в json
    :param income_socket: socket
    :return: json obj
    """
    data = income_socket.recv(MAX_PACK_SIZE)
    if isinstance(data, bytes):
        decode_response = data.decode(ENCODING_TYPE)
        js_response = json.loads(decode_response)
        if isinstance(js_response, dict):
            return js_response
        raise ValueError
    raise ValueError


def send_message(socket_type, message):
    """
    Кодирует сообщение для отправки из json obj в bytes и отправляет его
    :param socket_type: socket
    :param message: dict
    :return: None
    """
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING_TYPE)
    socket_type.send(encoded_message)
