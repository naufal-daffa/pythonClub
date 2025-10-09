profile_1 = [
    {
        "name": "Noval",
        "hobbies": ["gaming", "learning"]
    },
    {
        "name": "Ali",
        "hobbies": ["gaming", "listening"]
    }
]

set_1 = {"pineapple", "spaghetti"}
for set in set_1:
    print(set)

for profile in profile_1:
    print(profile["name"])
    

#operator membership (in)

sample_list = [2, 3, 4]
is_3_exists = 3 in sample_list
print(is_3_exists)

sample_tuple = ("hello", "python")
is_hello_exists = "hello" in sample_tuple
print(is_hello_exists)

sample_dict = { "nama": "noval", "age": 12 }
is_key_nama_exists = "nama" in sample_dict
print(is_key_nama_exists)