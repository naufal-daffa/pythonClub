def encrypt(pesan, key):
    hasil = ""
    for huruf in pesan:
        if huruf.isalpha():
            base = ord('A') if huruf.isupper() else ord('a')
            hasil += chr((ord(huruf) - base + key) % 26 + base)
        else:
            hasil += huruf
    return hasil


def decrypt(pesan, key):
    return encrypt(pesan, -key)


pesan = input("Masukkan pesan: ")
key = int(input("Masukkan key (angka): "))

terenkripsi = encrypt(pesan, key)
terdekripsi = decrypt(terenkripsi, key)

print("Encrypted :", terenkripsi)
print("Decrypted :", terdekripsi)
