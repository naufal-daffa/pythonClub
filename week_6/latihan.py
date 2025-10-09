data = [12, 15, 80, 100, 94, 40]

def linear_search(data, angka):
    for i in range(len(data)):
        if data[i] == angka:
            return i       
    return "data tidak ditemukan"

print(linear_search(data, 80))

def binary_search(data, target):
    low, high = 0, len(data)-1 
    while low <= high: #0 < 4
        mid = (low + high) #mid = (0+4)/2
        if data[mid] == target: #data[2] == 40
            return mid
        elif data[mid] < target: #data[2] < 40
            low = mid + 1 #data
        else:
            high = mid - 1
    return "data tidak ditemukan"

print(binary_search(data, 40))


# data_tertinggi = max(data)

# print(data_tertinggi)