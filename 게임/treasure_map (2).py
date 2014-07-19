with file("treasure_map.txt", "r") as text:
	for line in text:
		i = filter(lambda x:x.isdigit()==True, line)
		print line[int(i)],


with file("treasure_map.txt", "r") as text:
	for line in text:
		for x in line:
			if "!@#$%"+x in line:
				print x,
				break