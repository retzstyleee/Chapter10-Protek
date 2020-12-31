file = open("dataBil.txt", "r")
for i in file:
	ambil = i.split("|")
	hasil = int(ambil[0]) + int(ambil[1])
	print(hasil)
file.close()