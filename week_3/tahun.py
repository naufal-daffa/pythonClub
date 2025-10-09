year = int(input("Masukan tahun : "))

if year % 400 == 0:
    print("Tahun ini adalah tahun kabisat")
elif year % 100 == 0:
    print("Tahun ini bukanlah tahun kabisat")
elif year %  4 == 0:
    print("Tahun ini adalah tahun kabisat")
else :
    print("Tahun ini bukan tahun kabisat")
# def check()


    
