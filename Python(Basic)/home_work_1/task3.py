# coding: utf8

n = int(input('enter Number > 0: '))

nmax = 0

while 1:
	nnext = n % 10
	numbers = n // 10

	if nnext > nmax: nmax = nnext
	if numbers == 0: break
	n = n // 10

print('max: %s' % (nmax))