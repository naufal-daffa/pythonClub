number = int(input("masukkan angka"))

def Cek(number):
    if(number > 0):
        print('bilangan anda bernilai positif')
    elif(number < 0):
        print('bilangan anda bernilai negatif')
    else:
        print('bilangan anda bernilai 0')
        
Cek(number)