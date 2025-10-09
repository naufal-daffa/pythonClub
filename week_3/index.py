#soal 3
username: str = input("Masukan username : ")
password: str = input("Masukan password : ")

if username == "admin" and password == "12345":
    print("Login berhasil")
else:
    print("Login gagal")