jumlah_angka = int(input("Masukan Jumlah Angka: "))
total = 0 
for i in range (jumlah_angka):
    angka = float(input(f"Masukan Angka ke - {i + 1}"))
    total += angka
    
rata_rata = total / jumlah_angka
print(f"Rata - rata dari angka - angka tersebut adalah {rata_rata}")