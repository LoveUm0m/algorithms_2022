def rec(sumarg,numarg,k):
	n = k
	summ = sumarg
	num = numarg
	n += -1
	if n <= 0:
		print(summ)
	else:
		summ += - (num / 2)
		num = - num / 2	
		rec(summ, num, n)
rec(1, 1, 3)