"""
Реализован проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (абстрактный класс Clothes) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто Coat и костюм Suit. У этих типов одежды существуют параметры:
размер size (для пальто) и рост height (для костюма) обычные числа. Для определения расхода ткани
по каждому типу одежды использованы формулы. Работа методов расчета проверена. Проверена работа декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
	"""
	Основная сущность (абстрактный класс Clothes)
	"""
	@abstractmethod
	def calc_textile(self, number):
		"""
		абстрактный метод расчета ткани
		:param number: int
		:return: float
		"""
		pass


class Coat(Clothes):
	"""
	класс пальто
	"""
	def __init__(self, name, size):
		"""
		В конструкторе определены параметры названия и размера пальто
		:param name: str
		:param size: int
		"""
		self.__name = name
		self.size = size

	@property
	def name(self):
		"""
		метод используется как атрибут класса
		:return: str
		"""
		return self.__name

	def calc_textile(self, number=1):
		return (self.size / 6.5 + 0.5) * number


class Suit(Clothes):
	"""
	класс костюм
	"""
	def __init__(self, name, height):
		"""
		В конструкторе определены параметры названия и роста человека
		:param name: str
		:param height: int
		"""
		self.__name = name
		self.height = height

	@property
	def name(self):
		return self.__name

	def calc_textile(self, number=1):
		return (self.height * 2 + 0.3) * number


coat = Coat('Coat', 48)
suit = Suit('Suit', 182)
print(coat.name)
print(suit.name)
print(coat.size)
print(suit.height)
print(coat.calc_textile(10))
print(suit.calc_textile(15))
