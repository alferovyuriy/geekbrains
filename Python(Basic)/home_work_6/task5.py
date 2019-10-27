"""
Реализован класс Stationery (канцелярская принадлежность), в котором определен атрибут
title (название) и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.”
Созданы три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов
реализовано переопределение метода draw. Для каждого из классов методы выводят
уникальное сообщение. Созданы экземпляры классов и проверены, что выводит описанный метод для каждого экземпляра.
"""


class Stationery:
	"""
	Родительский класс Stationery (канцелярская принадлежность)
	"""
	def __init__(self, title):
		"""
		определен атрибут title (название)
		:param title: str
		"""
		self.title = title

	def draw(self):
		"""
		Метод выводит сообщение “Запуск отрисовки.”
		:return: None
		"""
		print('Start drawing.')


class Pen(Stationery):
	"""
	Дочерний класс Pen (ручка)
	"""
	def __init__(self, title):
		super().__init__(title)

	def draw(self):
		"""
		Переопределенн метод родительского класса, который выводит уникальное сообщение
		:return: None
		"""
		print(f'class {self.title}')


class Pencil(Stationery):
	"""
	Дочерний класс Pencil (карандаш)
	"""
	def __init__(self, title):
		super().__init__(title)

	def draw(self):
		print(f'class {self.title}')


class Handle(Stationery):
	"""
	Дочерний класс Handle (маркер)
	"""
	def __init__(self, title):
		super().__init__(title)

	def draw(self):
		print(f'class {self.title}')


stationery = Stationery('Stationery')
pen = Pen('Pen')
pencil = Pencil('Pencil')
handle = Handle('Handle')

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
