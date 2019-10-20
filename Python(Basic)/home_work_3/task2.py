# словарь с информацией о пользователе
user_info = {
	'name': str,
	'surname': str,
	'year': str,
	'city': str,
	'email': str,
	'phone_num': str,
}


def output_user_info(name, surname, year, city, email, phone_num):
	""" функция принимает именованные аргументы и выводит в одну строку """
	print(f'{name}, {surname}, {year}, {city}, {email}, {phone_num}')


# в цикле заполняем поля словаря
for key, value in user_info.items():
	user_info[key] = input(f'enter {key}: ')

# передаем в функцию заполненный словарь и преобразуем его в именованные аргументы
output_user_info(**user_info)
