# просим пользователя ввести номер месяца
month = input('enter month number (1 - 12): ')
# список времен года
list_seasons = [
	[(1, 2, 3), 'Winter'],
	[(4, 5, 6), 'Spring'],
	[(7, 8, 9), 'Summer'],
	[(10, 11, 12), 'Autumn']]
# словарь времен года
dict_seasons = {
	(1, 2, 3):    'Winter',
	(4, 5, 6):    'Spring',
	(7, 8, 9):    'Summer',
	(10, 11, 12): 'Autumn'
}
# проверяем что пользователь ввел допустимое по условиям значение
if month.isdigit() and 0 < int(month) < 13:
	month = int(month)
	# цикл проверки времени года
	for keys, season in dict_seasons.items():	# для итерации списка list_seasons заменить dict_seasons.items()
		if month in keys:
			print(f'season is {season}')
else:
	print('ValueError')