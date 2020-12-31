file = open("DataMhs.txt", "r")
data = file.read()
data = data.replace(" | ", " ")
data = data.replace("\n", " ")
data = data.split(" ")
data.remove("")
while True:
	cari = input("Masukkan NIM yang akan dicari : ")
	if cari in data:
		temu = data.index(cari)
		print("Data Mahasiswa")
		print("NIM\t\t: ", data[temu])
		print("Nama\t\t: ", data[temu + 1])
		print("Alamat\t\t: ", data[temu + 2])
	else:
		print("Data tidak ditemukan")
	menu = input("Ulangi lagi (y/n) ? ")
	menu = menu.lower()
	if menu == "y":
		continue
	elif menu == "n":
		break
	else:
		print("Input tidak valid")
		break