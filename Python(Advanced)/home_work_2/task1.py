"""
Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.
"""


import csv
import re


CSV_FILE = 'data.csv'
RES_PATH = 'res/'
FILES = ['info_1.txt', 'info_2.txt', 'info_3.txt']
PATTERNS = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']


def get_data():
    """
    parced data from .*txt files
    :return: list
    """
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    for txt_file in FILES:
        with open(RES_PATH + txt_file) as res_file:
            lines = res_file.readlines()
            os_prod_list.append([re.split(r'\b: *', line)[-1].rstrip('\n') for line in lines \
                                if re.search(PATTERNS[0], line)][0])
            os_name_list.append([re.split(r'\b: *', line)[-1].rstrip(' \n') for line in lines \
                                if re.search(PATTERNS[1], line)][0])
            os_code_list.append([re.split(r'\b: *', line)[-1].rstrip('\n') for line in lines \
                                if re.search(PATTERNS[2], line)][0])
            os_type_list.append([re.split(r'\b: *', line)[-1].rstrip('\n') for line in lines \
                                if re.search(PATTERNS[3], line)][0])

    main_data = [data for data in (PATTERNS, os_prod_list, os_name_list, os_code_list, os_type_list)]
    return main_data


def write_to_csv(ref_csv):
    """
    write data in *.csv file
    :param ref_csv: references to *.csv file
    :return: None
    """
    data = get_data()
    with open(ref_csv, 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)


write_to_csv(CSV_FILE)
with open(CSV_FILE, encoding='utf-8') as file:
    print(file.read())
