Mengapa paradigma penting? 
Kode Kecil = untuk program sederhana paradigma belum terlalu
Kode besar = Untuk kompleks pasti digunakan

3 paradigma
Prosedural = Mengelompokan tugas menjadi fungsi yang dapar digunakan berkali-kali
Fungsional = Fokus pada input output, fungsi mengembalikan nilai tanpa mengubah data langsung
OOP = Semua komponen berbasis objek

P vs F
P = Fungsi tidak mengembalkan nilai, menangani 1/0
F = Fungsi mengembalikan nilai, pemanggilan mengelola hasilnya


contoh Prosedural


contoh fungsional 

def hitung(alas, tinggi):
    return 0.5 * alas * tinggi

konsep dasar OOP
Identitas = atribut yang mengidentifikasin objek
Prilaku = metode yang objek dapat lakukan
Kelas = Blueprint untuk membuat objek

OOP Dalam PYTHON


class Segitiga: def __init__(self, alas, tinggi):
                        self.alas = alas
                        self.tinggi = tinggi