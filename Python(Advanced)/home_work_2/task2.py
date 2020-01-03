"""
Есть файл orders в формате JSON с информацией о заказах. Написать скрипт,
автоматизирующий его заполнение данными.
"""


import json


RES_PATH = 'res/'
JSON_FILE = 'orders.json'
DATA = [
    {
        'item': 'printer',
        'quantity': '10',
        'price': '6700',
        'buyer': 'Ivanov I. I.',
        'date': '24.09.2017'
    },
    {
        'item': 'сканер',
        'quantity': '10',
        'price': '6700',
        'buyer': 'Петров П. П.',
        'date': '24.09.2017'
    }
]


def write_order_to_json(item, quantity, price, buyer, date):
    """
    rewrite *.json file with new data
    :param item:
    :param quantity:
    :param price:
    :param buyer:
    :param date:
    :return:
    """
    new_order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }
    orders = []
    loaded = []

    with open(RES_PATH + JSON_FILE, 'r', encoding='utf-8') as load_file:
        loaded_data = json.load(load_file)
        for order in loaded_data['orders']:
            loaded.append(order)

    with open(RES_PATH + JSON_FILE, 'w', encoding='utf-8') as dump_file:
        orders.append(new_order)
        if bool(loaded):
            for data in loaded:
                orders.append(data)
        json.dump({'orders': orders}, dump_file, ensure_ascii=False, indent=4)


write_order_to_json(DATA[0]['item'], DATA[0]['quantity'], DATA[0]['price'], DATA[0]['buyer'], DATA[0]['date'])
write_order_to_json(DATA[1]['item'], DATA[1]['quantity'], DATA[1]['price'], DATA[1]['buyer'], DATA[1]['date'])
