from datetime import datetime

tanggal_lahir = input("Masukan tanggal lahir anda (YYYY-MM-DD) : ")
tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")

tanggal_sekarang = datetime.now()

umur = tanggal_sekarang - tanggal_lahir

umur_tahun = umur.days // 365
sisa_hari = umur.days % 365
umur_bulan = sisa_hari // 30
sisa_hari = sisa_hari % 30

print(f"Umur Anda : {umur_tahun} Tahun, {umur_bulan} Bulan, {sisa_hari} Hari")
