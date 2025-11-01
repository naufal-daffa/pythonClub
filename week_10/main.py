import module.Diskon as md

harga = int(input("Masukan harga : "))
jumlah = int(input("Masukan jumlah : "))

Bayar = md.bayar(harga, jumlah)
Diskon = md.diskon(harga)
Total = md.total(Bayar, Diskon)

print("Total harga : ", Total)
print("Diskon : ", Diskon)
tagihan = int(input("Jumlah nominal uang anda : "))
Kembalian = tagihan-Total
print("Kembalian : ", Kembalian)