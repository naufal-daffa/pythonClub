# variabel with data type
nama: str = "naufal"
hobi: str = 'game'
umur: int = 18
laki: bool = True
nilai_ujian: float = 99.2

# variabel with many declarations
nilai1, nilai2, nilai3, nilai4 = 24, 25, 26, 21
nilai_rata_rata = (nilai1 + nilai2 + nilai3 + nilai4) / 4
print("rata-rata nilai: %f" % (nilai_rata_rata))

# variabel

nama = "Naufal"
hobi = 'ngagame'
umur = 18
laki_laki = True

print("==== biodata ====")
print("nama: %s" % (nama))
print("hobi: %s, umur: %d, laki: %r" % (hobi, umur, laki_laki))

#proses memasukan data ke dalam variabel
nama = "John Doe"
print(nama)

#nilai dan tipe data dalam variabel dapat diubah
umur = 20 
print(umur)
type(umur)
umur = "dua puluh satu"
print(umur)
type(umur)

namaDepan = "Budi"
namaBelakang = "Susanto"
nama = namaDepan + " " + namaBelakang
umur = 22
hobi = "Berenang"
print("Biodata\n", nama, "\n", umur, "\n", hobi)

inivariabel = "Halo"
ini_juga_variabel = "Hai"
inivariabeljuga = "Hi"
inivariabel222 = "Bye"

panjang = 10
lebar = 5
luas = panjang * lebar
print(luas)