class Siswa:
    nis =''
    nama = ''
    
    def __init__(self, x, y):
        self.nis = x
        self.nama = y
        
    def printSiswa(self):
        print(self.nis)
        print(self.nama)
        
daffa = Siswa('12', 'akus')

daffa.printSiswa()