from sys import argv


def calc_salary(hours, rate, bonus):
	"""
	рссчитывает зарабатную плату сотрудника
	:param hours: int
	:param rate: int
	:param bonus: int
	:return: int
	"""
	return hours * rate + bonus


try:
	script_name, hours, rate, bonus = argv	# параметры указываются при запуске скрипта
	print(f'salary: {calc_salary(int(hours), int(rate), int(bonus))}')
except ValueError as e:
	print(e)
