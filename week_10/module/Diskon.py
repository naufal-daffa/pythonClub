def total(harga: int, jumlah: int):
    return harga*jumlah

def diskon(harga: int):
    if(harga < 500000):
        potongan=harga*0.1
    else:
        potongan= harga*0.05
    return potongan

def bayar(harga: int, potongan: int):
    return harga-potongan