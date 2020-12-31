file = input("Nama file yang ingin dienkripsi : ")
key = int(input("Input key : "))
data = open(file + ".encrypt", "r")
isi = data.read()
hasil = ''
for i in isi:
	nomor = ord(i)-key
	if i == ' ':
		hasil += i
		continue
	if nomor > ord('Z'):
		nomor -= 26
	elif nomor < ord('A'):
		nomor += 26
	hasil += chr(nomor)

data.close()
enkrip = open(file + '.encrypt.decrypt', 'w')
enkrip.write(hasil)
enkrip.close()
print("File enskripsi : {}.encrypt.decrypt".format(file))