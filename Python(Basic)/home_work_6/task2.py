"""
Реализует класс Road (дорога), в котором определены защищенные атрибуты:
length (длина), width (ширина). Значения атрибутов передаются при создании экземпляра класса.
Определен метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использована формула: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см*число см толщины полотна. Проверена работа метода.
"""


class Road:

	def __init__(self, length, width):
		"""
		Определяет атрибуты класса Road
		:param length: int
		:param width: int
		"""
		self.__length = length
		self.__width = width

	def calc_mas(self, mass, thickness):
		"""
		Получает атрибуты массы асфальта на 1 кв.м. и толщину асфальта в метрах.
		Рассчитывает массу асфальта для покрытия дорожного полотна
		:param mass: int
		:param thickness: float
		:return: float
		"""
		result = self.__length * self.__width * mass * thickness
		return result


road = Road(20, 5000)
print(road.calc_mas(25, 0.05))
