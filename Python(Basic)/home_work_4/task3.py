# выводит все числа от 20 до 240 кратные 20 или 21
my_lst = [arg for arg in range(20, 240) if arg % 20 == 0 or arg % 21 == 0]
print(my_lst)
