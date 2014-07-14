with file("treasure_map.txt", "r") as text:
	for line in text:
		i = filter(lambda x:x.isdigit()==True, line)
		print line[int(i)],

with file("treasure_map.txt", "r") as text:
	for line in text:
		if "!@#$%" in line:
			print line