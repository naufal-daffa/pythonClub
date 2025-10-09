import random

angka_acak = random.randint(1, 10)
tebakan = 0

while True:
    tebakan = int(input("Tebak angka dari 1-10"))
    if tebakan < angka_acak:
        print("angka anda terlalu kecil")
    elif tebakan > angka_acak:
        print("angka anda terlalu besar")
    else:
        print("tebakan anda benar!")
        break