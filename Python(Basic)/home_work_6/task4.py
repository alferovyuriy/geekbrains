"""
Определен базовый класс Car. Описаны подклассы: TownCar, SportCar, WorkCar, PoliceCar. У каждого класса
имеются атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), show_speed,
которые сообщают, что машина поехала, остановилась, повернула (куда), скоросто машины.
"""


class Car:
	"""
	Базовый класс Car
	"""
	def __init__(self, speed, color, name, is_police):
		"""
		определены атрибуты базового класса Car
		:param speed: int
		:param color: str
		:param name: str
		:param is_police: bool
		"""
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

	def show_speed(self):
		"""
		показывает скорость машины
		:return: None
		"""
		print(f'speed: {self.speed}')


class TownCar(Car):
	"""
	дочерний класс TownCar базового класса Car
	"""
	def __init__(self, speed, color, name, is_police):
		"""
		переопределены атрибуты класса TownCar
		:param speed: int
		:param color: str
		:param name: str
		:param is_police: bool
		"""
		super().__init__(speed, color, name, is_police)

	def show_speed(self):
		"""
		переопределен метод базового класса, сообщает если скоросто машины превышена
		:return: None
		"""
		if self.speed > 60:
			print('Car speed too much!')
		else:
			print(f'speed: {self.speed}')


class SportCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)


class WorkCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)

	def show_speed(self):
		if self.speed > 40:
			print('Car speed too much!')
		else:
			print(f'speed: {self.speed}')


class PoliceCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)


town_car = TownCar(60, 'white', 'Lada', False)
sport_car = SportCar(300, 'red', 'Ferrari', False)
work_car = WorkCar(80, 'yellow', 'Ford', False)
police_car = PoliceCar(350, 'black', 'Porsche', True)

town_car.stop()
town_car.go()
town_car.show_speed()
sport_car.go()
work_car.turn('left')
work_car.show_speed()
police_car.turn('right')
