"""
«Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников отдельных типов техники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
любую подходящую структуру, например словарь.
Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров,
отправленных на склад, нельзя использовать строковый тип данных.
По возможности реализовать в проекте «Склад оргтехники» максимум возможностей ООП.
"""
from abc import ABC, abstractmethod


class Department(ABC):
	"""
	абстрактный класс подразделение компании, которое принимает технику
	"""
	@abstractmethod
	def add(self, type_technic, data):
		pass


class MyTypeError(Exception):
	"""
	собственный класс исключение типа объекта
	"""
	def __init__(self, message):
		self.message = message

	def __str__(self):
		return self.message


class Storage:
	"""
	класс склада техники
	"""
	def __init__(self):
		self.__storage = {}

	@property
	def storage(self):
		"""
		получение закрытого атрибута
		:return: dict
		"""
		return self.__storage

	def add_technic(self, technic, number):
		"""
		добавление иехники на склад, включает валидацию
		:param technic: obj
		:param number: int
		:return: None
		"""
		try:
			if not isinstance(number, int):
				raise MyTypeError('type of number must be int')
			technic.params['number'] = number
			if not self.__storage.get(technic.type_technic):
				self.__storage[technic.type_technic] = {technic.name: technic.params}
			else:
				self.__storage[technic.type_technic].setdefault(technic.name, technic.params)
		except MyTypeError as e:
			print(e)

	def transfer_to_department(self, technic, department):
		"""
		передача техники подразделению
		:param technic: obj
		:param department: obj
		:return: None
		"""
		department.add(technic.type_technic, self.__storage.get(technic.type_technic))


class TransportDepartment(Department):
	"""
	транспортное подразделение, реализация абстрактного класса Подразделение компании
	"""
	def __init__(self):
		self.__storage = {}

	@property
	def storage(self):
		return self.__storage

	def add(self, type_technic, data):
		"""
		добавляет технику в подразделение
		:param type_technic: str
		:param data: dict
		:return: None
		"""
		if not self.__storage.get(type_technic):
			self.__storage[type_technic] = data
		else:
			self.__storage[type_technic].setdefault(data)


class OfficeTechnics:
	"""
	базовый класс офисной техники
	"""
	def __init__(self, name: str, color: str):
		"""
		общие атрибуты классов наследников
		:param name: str
		:param color: str
		"""
		self.name = name
		self.color = color


class Printer(OfficeTechnics):
	def __init__(self, name: str, color: str, speed: int):
		super().__init__(name, color)
		self.type_technic = self.__class__.__name__
		self.print_speed = speed
		self.params = {'name': self.name, 'color': self.color, 'print_speed': self.print_speed}


class Scanner(OfficeTechnics):
	def __init__(self, name: str, color: str, speed: int):
		super().__init__(name, color)
		self.type_technic = self.__class__.__name__
		self.scan_speed = speed
		self.params = {'name': self.name, 'color': self.color, 'scan_speed': self.scan_speed}


class Copier(OfficeTechnics):
	def __init__(self, name: str, color: str, speed: int):
		super().__init__(name, color)
		self.type_technic = self.__class__.__name__
		self.copy_speed = speed
		self.params = {'name': self.name, 'color': self.color, 'copy_speed': self.copy_speed}


if __name__ == '__main__':
	printer = Printer('HP', 'Black', 12)
	scaner = Scanner('Canon', 'White', 15)
	copier = Copier('Canon', 'Gray', 23)
	print(f'printer: {printer}')
	print(f'scaner: {scaner}')
	print(f'copier: {copier}')
	storage = Storage()
	storage.add_technic(printer, 20)
	storage.add_technic(scaner, 50)
	print(f'storage: {storage.storage}')
	transportDep = TransportDepartment()
	storage.transfer_to_department(scaner, transportDep)
	print(f'transportDep storage: {transportDep.storage}')
