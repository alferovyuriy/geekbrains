# coding: utf8

sec = int(input('enter seconds: '))

h = sec // 3600
m = (sec % 3600) // 60
s = (sec % 3600) % 60

print('{0}:{1}:{2}'.format(h, m, s))