import datetime

tahun = int(input("Masukan Tahun : "))
bulan = int(input("Masukan Bulan : "))
tanggal = int(input("Masukan Tanggal : "))

tanggal_input = datetime.date(tahun, bulan, tanggal)
nama_hari = tanggal_input.strftime("%A")
tanggal_format = tanggal_input.strftime("%d %B %Y")

print(f"Tanggal {tanggal_format} adalah hari {nama_hari}")