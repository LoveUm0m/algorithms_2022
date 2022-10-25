def rec(number, rebmun):
	num = number
	mun = rebmun
	mun = mun + str(int(num%10))
	num = num // 10
	print(f'--{num}-1')
	print(f'--{mun}-2')
	if  num != 0:
		rec(num, mun)
	else:
		print(f'--{mun}--')


mun = str()
rec(2794343256347260,mun)