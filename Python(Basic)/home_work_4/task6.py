from itertools import count, cycle

# бесконечный итератор, генерирующий целые числа, начиная с указанного
for num in count(3):
	if num > 10: break
	print(num)

counter = 0
# бесконечный итератор, повторяющий элементы заранее определенного списка
for elem in cycle(['Hello World!']):
	print(elem)
	counter += 1
	if counter > 3: break
