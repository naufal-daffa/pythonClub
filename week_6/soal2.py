angka = [64, 34, 25, 12, 22, 11, 90]

def bubble_sort(data):
    n = len(data) #n = 7
    for i in range(n): # i di jarak 7-1 = 6
        for j in range(0, n-i-1):#  j = 0 di jarak dimulai 0 dan 6-0-1 = 5
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j] 
    return data


print(bubble_sort(angka))