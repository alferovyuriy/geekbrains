"""
Построчно прочитает файл с данными компаний, вычисляет прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включает.
Реализует список, содержащий словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавляет ее в словарь (со значением убытков).
"""
import json


try:
	with open('firms.txt', 'r') as file:
		firms_dict2 = dict([(firma, int(rev) - int(cost)) for firma, _, rev, cost in \
							[line.split() for line in file.readlines()]])
		aver_profit = [profit for profit in firms_dict2.values() if profit > 0]
		aver_profit = {'aversge_profit': sum(aver_profit)/len(aver_profit)}
		res = [firms_dict2, aver_profit]

		with open('firms.json', 'w') as write_f:
			json.dump(res, write_f)
except IOError as e:
	print(e)
