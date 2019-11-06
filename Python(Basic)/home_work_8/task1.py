"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
	def __init__(self, date: str):
		self.date = date

	@classmethod
	def get_date_int(cls, date_str: str):
		day, month, year = map(int, date_str.split('-'))
		return day, month, year

	@staticmethod
	def validate_date(date_str: str):
		day, month, year = map(int, date_str.split('-'))
		return day <= 31 and month <= 12 and year <= 2999


if __name__ == '__main__':
	my_birthday = Date('13-04-1986')
	print(Date.validate_date(my_birthday.date))
	print(Date.get_date_int(my_birthday.date))
