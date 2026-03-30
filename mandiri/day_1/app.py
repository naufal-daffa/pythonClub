pesan = input("Masukkan pesan: ")
geser = 3
hasil = ""

for huruf in pesan:
    if huruf.isalpha(): #isalpha() → cek apakah huruf
        huruf_baru = ord(huruf.upper()) + geser #ord() → ubah huruf jadi angka
        if huruf_baru > ord('Z'):
            huruf_baru -= 26
        hasil += chr(huruf_baru) #chr() → ubah angka jadi huruf
    else:
        hasil += huruf

print("Pesan terenkripsi:", hasil)