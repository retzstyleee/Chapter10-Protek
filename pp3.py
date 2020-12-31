file = open("DataMhs.txt", "r")
data = []
for i in file:
	ambil = i.split()
	isi = {'nim' : ambil[0], 'nama' : ambil[2], 'alamat' : ambil[4]}
	data.append(isi)
file.close()
print(data)