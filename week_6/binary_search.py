def binary_search(data, target):
    low, high = 0, len(data)-1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

angka = [10, 20, 30, 40, 50]
print(binary_search(angka, 50))