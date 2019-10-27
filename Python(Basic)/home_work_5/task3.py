"""
Определяет, кто из сотрудников имеет оклад менее 20 тыс., выводит фамилии этих сотрудников.
Выполняет подсчет средней величины дохода сотрудников.
"""

try:
	with open('employees.txt', 'r') as file:
		sum_salery = 0
		counter = 0
		for i, employee in enumerate(file.readlines(), 1):
			surname, salary = employee.split()
			if salary.isdigit() and int(salary) < 20000:
				print(f'employee with salary < 20000: {surname}')
			sum_salery += int(salary)
			counter += 1
		print(f'average salary: {sum_salery/counter}')
except IOError as e:
	print(e)
