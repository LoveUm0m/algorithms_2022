def rec(pos, mass, argline):
	list_of_ascii = mass
	i = pos + 1
	st = str()
	if pos % 10 == 2:
		line = argline + 1
		if pos != 32:
			for k in range(len(list_of_ascii[argline])):
				st += list_of_ascii[argline][k]
			print(st)
	elif pos == 128:
		for k in range(len(list_of_ascii[argline])):
			st += list_of_ascii[argline][k]
		print(st)
	else:
		line = argline
	if i > 128:
		pass
	else:
		list_of_ascii[line].append(f'{pos} - {chr(pos)} ')
		rec(i, list_of_ascii, line)



mass = [[], [], [], [], [], [], [], [], [], []]
rec(32, mass, -1)