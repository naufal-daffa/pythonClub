# number_one = input("Masukan nilai pertama : ")
# number_two = input("Masukan nilai kedua : ")
# number_three = input("Masukan nilai ketiga : ")
def check_highest_number(n1, n2, n3):
    if (n1 > n2 and n1 > n3):
        return print ("Nomor pertama adalah nilai terbesar : " + str(n1))
    elif (n2 > n1 and n2 > n3):
        return print ("Nomor kedua adalah nilai terbesar : " + str(n2))
    else:
        return print ("Nomor ketiga adalah nilai terbesar : " + str(n3))
    

# check_highest_number(number_one, number_two, number_three)

# str_input = input("Masukan input : ")
# grade = int(str_input)

# if (grade == 100):
#     print("Perfect")
# elif (grade >= 85):
#     print("Awesome")
# elif (grade >= 65):
#     print("Passed The Exam")
#     if (grade <= 70):
#         print("But you need to improve it!")
#     else:
#         print("With ok grade")
# else:
#     print("Bellow the passing grade")
    



try:
    angka = input("Masukan angka : ")
    if (angka % 2 != 0):
        print("Angka anda adalah bilangan ganjil")
    else:
        print("Angka anda adalah bilangan genap")
except ValueError:
    print("Harap masukan angka!")

# def check_number(cek):
#     if cek.isalnum() == True :
#         return print("Input harus angka")
#     else:
#         if (cek % 2 != 0):
#             return print("Angka anda adalah bilangan ganjil")
#         else:
#             return print("Angka anda adalah bilangan genap" + str(cek))
    
# check_number(angka) 

