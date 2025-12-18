class BankAccount:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.__saldo = saldo_awal
        
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, jumlah):
        if jumlah < 0:
            print('Tidak boleh negatif')
        else:
            self.__saldo = jumlah
            print(f'saldo anda : {self.__saldo}')
            
    def deposit(self, jumlah):
        if(jumlah > 0):
            self.__saldo += jumlah
            print(f"Saldo bertambah: {jumlah}, Saldo anda sekarang : {self.saldo}")
        else:
            print('Tidak boleh negatif')
            
            
            
    def withdraw(self, jumlah):
        if jumlah > 0 and jumlah <= self.saldo:
            self.__saldo -= jumlah
            print(f"Berhasil menarik {jumlah}, Saldo anda: {self.saldo}")
        else:
            print("Gagal")
            
akun = BankAccount('Budi', 2000)
print(akun.get_saldo)

akun.set_saldo(2000)
akun.deposit(500)
akun.withdraw(500)