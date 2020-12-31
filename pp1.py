while True:
	file = open("pp1.txt", "r")
	genap = 0
	ganjil = 0
	for i in file:
		if int(i) % 2 == 0:
			genap += 1
		else:
			ganjil += 1
	file.close()
	juml = {"genap" : genap, "ganjil" : ganjil}
	print("Banyaknya bilangan genap :", juml.get('genap'))
	print("Banyaknya bilangan ganjil :", juml.get('ganjil'))
	break