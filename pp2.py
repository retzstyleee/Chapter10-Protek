print("----------------------")
print("PROGRAM PENYIMPAN DATA")
print("----------------------")

data = open("DataMhs.txt", "w")
while True:
	data = open("DataMhs.txt", "a")
	no = input("\nMasukkan NIM		: ")
	name = input("Masukkan Nama Mhs	: ")
	add = input("Masukkan Alamat 	: ")
	tamb = input("\nTambah data lagi (y/n)	: ")
	if tamb == 'y' or tamb =='Y':
		data.write(' | '.join([no, name, add]) + '\n')
		continue
	elif tamb == 'n' or tamb == 'N' :
		data.write(' | '.join([no, name, add]) + '\n')
		data = open("DataMhs.txt", "r")
		file = data.read()
		print(file)
		break
	else:
		print("Input tidak valid\n")
		continue
	break
