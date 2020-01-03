"""
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.
"""


import yaml


YAML_FILE = 'file.yaml'
ITEMS = ['computer', 'printer', 'keyboard', 'mouse']
ITEMS_QUANTITY = len(ITEMS)
ITEMS_DATA = {
    ITEMS[0]: '200€-1000€',
    ITEMS[1]: '100€-300€',
    ITEMS[2]: '5€-50€',
    ITEMS[3]: '4€-7€'
}
DATA_TO_YAML = {'items': ITEMS, 'items_quantity': ITEMS_QUANTITY, 'items_data': ITEMS_DATA}

with open(YAML_FILE, 'w', encoding='utf-8') as y_file:
    yaml.dump(DATA_TO_YAML, y_file, default_flow_style=False, allow_unicode=True)

with open(YAML_FILE, 'r', encoding='utf-8') as r_file:
    print(r_file.read())
