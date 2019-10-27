"""
Описаны классы: TownCar, SportCar, WorkCar, PoliceCar. У каждого класса
имеются атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые сообщают, что машина поехала, остановилась, повернула (куда).
"""


class TownCar:
	"""
	определены атрибуты класса TownCar
	:param speed: int
	:param color: str
	:param name: str
	:param is_police: bool
	"""
	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		"""
		сообщает что машина движется
		:return: None
		"""
		print(f'{self.name} moving')

	def stop(self):
		"""
		сообщает что машина стоит на месте
		:return: None
		"""
		print(f'{self.name} standing')

	def turn(self, direction):
		"""
		сообщает что машина повернула
		:param direction: str
		:return: None
		"""
		print(f'{self.name} turn to the {direction}')


class SportCar:
	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		print(f'{self.name} moving')

	def stop(self):
		print(f'{self.name} standing')

	def turn(self, direction):
		print(f'{self.name} turn to the {direction}')


class WorkCar:
	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		print(f'{self.name} moving')

	def stop(self):
		print(f'{self.name} standing')

	def turn(self, direction):
		print(f'{self.name} turn to the {direction}')


class PoliceCar:
	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police

	def go(self):
		print(f'{self.name} moving')

	def stop(self):
		print(f'{self.name} standing')

	def turn(self, direction):
		print(f'{self.name} turn to the {direction}')


town_car = TownCar(60, 'white', 'Lada', False)
sport_car = SportCar(300, 'red', 'Ferrari', False)
work_car = WorkCar(80, 'yellow', 'Ford', False)
police_car = PoliceCar(350, 'black', 'Porsche', True)

town_car.stop()
sport_car.go()
work_car.turn('left')
police_car.turn('right')
