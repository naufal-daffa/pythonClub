# class Penjumlahan:
#     def hasil(self, bil1, bil2):
#         print(bil1 + bil2)
#     def hasil(self, bil1, bil2, bil3):
#         print(bil1 + bil2 + bil3)
        
    
# class Penjumlahan:
#     def hasil(self, *args):
#         sum = 0
#         for num in args:
#             sum += num
#         print(sum)
        
class Penjumlahan:
    def hasil(self, *args):
        if(len(args) <= 4):
            for num in args:
                sum += num
            print(sum)
        else:
            print('Maksimal 4 angka')

coba = Penjumlahan()
coba.hasil(1, 2, 6, 4, 5)
    
    
# method nama nya sama dengan parameter yang berbeda
# parameter khusus dipython *args => mendefinisikan fungsi atau method atau arugument