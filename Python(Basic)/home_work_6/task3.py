"""
Реализован базовый класс Worker (работник), в котором определены атрибуты: name, surname,
position (должность), income (доход) защищенный и ссылается на словарь. Создан класс Position (должность)
на базе класса Worker. В классе Position реализованы методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_full_profit). Проверена работа примера (созданы экземпляры класса Position,
переданы данные, проверены значения атрибутов, вызваны методы экземпляров).
"""


class Worker:
	"""
	Базовый класс Worker (работник)
	"""
	def __init__(self, name, surname, position, income):
		"""
		определены атрибуты: name, surname, position (должность), __income (доход) защищенный атрибут
		:param name: str
		:param surname: str
		:param position: str
		:param income: dict
		"""
		self.name = name
		self.surname = surname
		self.position = position
		self.__income = income


class Position(Worker):
	"""
	Дочерний класс Position (должность) на базе класса Worker
	"""
	def __init__(self, name, surname, position, income={}):
		"""
		Передает атрибуты в родительский класс Worker
		:param name: str
		:param surname: str
		:param position: str
		:param income: dict
		"""
		super().__init__(name, surname, position, income)

	def get_full_name(self):
		"""
		Метод получения полного имени сотрудника
		:return: str, str
		"""
		return self.name, self.surname

	def get_full_profit(self):
		"""
		Метод получения дохода сотрудника с учетом премии
		:return: int
		"""
		return sum(self._Worker__income.values())


worker1 = Position('Vasia', 'Petrov', 'manager', {'profit': 10000, 'bonus': 5000})
print(worker1.get_full_name())
print(worker1.position)
print(worker1.get_full_profit())
try:
	worker2 = Position('Ivan', 'Ivanov', 'intern')
	print(worker2.get_full_name())
	print(worker2.position)
	print(worker2.get_full_profit())
except AttributeError as e:
	print(e)
