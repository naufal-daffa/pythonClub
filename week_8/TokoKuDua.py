print("Toko Naufal Maju Jaya")

def total(harga, jumlah):
    return harga * jumlah

def diskon(total_harga):
    if total_harga <= 500000:
        potongan = total_harga * 0.1
    else:
        potongan = total_harga * 0.05
    return potongan

def bayar(total_harga, potongan):
    return total_harga - potongan

harga = int(input("Masukan harga barang: "))
jumlah = int(input("Masukan jumlah baju yang dibeli: "))

total_belanja = total(harga, jumlah)
diskon_beli = diskon(total_belanja)
bayar_belanja = bayar(total_belanja, diskon_beli)

print(f"Total yang harus dibayar = Rp. {bayar_belanja}")

uang = int(input("Masukan nominal uang: "))

kembalian = uang - bayar_belanja

if kembalian >= 0:
    print(f"Kembalian Anda = Rp. {kembalian}")
else:
    print(f"Uang Anda kurang Rp. {-kembalian}")
    
