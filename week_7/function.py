# A. Pengenalan Function
# Function adalah code program yang terisolasi dalam satu blok kode, yang bisa dipanggil sewaktu-waktu
# Function memiliki beberapa atribut seperti, nama fungsi, isi gfungsi, parameter dan argumen, 

def say_hello():
    print("hello")
    
say_hello()
say_hello()
say_hello()

# suatu fungsi hanya bisa diakses atau dipanggil setelah fungsi tersebut dideklarasikan 

def print_something():
    print('hello')
    
    today = "Thursday"
    print(f"happy {today}")
    
    for i in range(5):
        print(f"i: {i}")
                
print_something()


# isi statement posisinya tidak boleh sejajar vertikal

# Parameter dan argument

# fungsi bisa memiliki parameter denagan adanya paramater, suatu nilai bisa di_sisipkan ke-dalam fungsi secara otomatis/dinamis

def calculate_circle_area(message: str, r: int):
    area = 3.14 * (r ** 2)
    print(message, area)
    
calculate_circle_area("area of circle is ", 788)

# nama fungsi dianjurkan untuk ditulis menggunaakn snake case
# penulisan nama parameter/argument adalah sama sseperti nama variable, yaitu snake case