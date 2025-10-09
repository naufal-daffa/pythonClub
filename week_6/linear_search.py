def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


angka = [10, 20, 30, 40, 50]
print(linear_search(angka, 30))