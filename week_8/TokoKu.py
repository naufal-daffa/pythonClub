print("Toko Naufal Maju Jaya")

def total(harga, jumlah):
    return harga*jumlah

harga = int(input("masukan harga barang: "))
jumlah = int(input("masukan jumlah baju yang dibeli : "))
total_belanja = total(harga, jumlah)

if total_belanja > 100000:
    total_belanja =  total_belanja - (total_belanja*0.05)
    
print(f"Total harga =  Rp. {total_belanja}")
bayar = int(input("Masukan nominal uang : "))
kembalian = total_belanja - bayar

print(f"uang Kembalian = Rp. {kembalian}")