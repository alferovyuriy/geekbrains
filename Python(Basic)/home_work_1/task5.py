# запрашиваем сколько спортсмен пробежал в первый день и какой результат нужно достичь
firstday_result = input('enter kilometers of first day: ')
final_reult = input('enter final result kilometers: ')
# проверяем что введено число
if firstday_result.isdigit() and final_reult.isdigit():
	firstday_result = int(firstday_result)
	final_reult = int(final_reult)
	if firstday_result >= final_reult:	# проверяем и выводим если результат достигнут в первый день
		print('required result in first day')
	else:
		days = 1	# счетчик дней
		result = firstday_result	# задаем переменную в которую будем считать результат
		while 1: # цикл для посчета результат
			days += 1
			result += result + result * 0.1
			if result >= final_reult:	# проверяем достигнут ли результат, выводим и выходим из цикла
				print('final result reached in %s day' % (days))
				break
else:
	print('ValueError')	# если введено не верное значение