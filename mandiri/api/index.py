import requests

url = "https://fakestoreapi.com/products"
response = requests.get(url)

if response.status_code == 200:
    products = response.json()
    for p in products[:9]:
        print(f"{p['id']} - {p['title']} (${p['price']})")
else:
    print("Error:", response.status_code)