"""
Создатся класс TrafficLight (светофор) с атрибутом color (цвет)
и методом running (запуск). Атрибут реализован как приватный. В рамках метода
реализовано переключение светофора в режимы: красный, желтый, зеленый.
Время перехода между режимами составляет 7 и 2 секунды. Проверка работы примера осуществляется
созданием экземпляра и вызовом описанного метода.
"""
import time


class TrafficLight:

	def __init__(self):
		self.__color = None

	def running(self):
		for color, sleep in [('Red', 7), ('Yellow', 2), ('Green', 7)]:
			self.__color = color
			time.sleep(sleep)


traffic_light = TrafficLight()
traffic_light.running()
