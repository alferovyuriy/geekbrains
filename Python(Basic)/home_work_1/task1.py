# coding: utf8
# запрашиваем секунды
seconds = int(input('enter seconds: '))
# переводим секунды в формат чч:мм:сс
hours = seconds // 3600				# вычисляем сколько часов
minutes = (seconds % 3600) // 60	# вычисляем сколько минут
sec = (seconds % 3600) % 60			# вычисляем сколько секунд
# выводим форматированный результат
print('{0}:{1}:{2}'.format(hours, minutes, sec))