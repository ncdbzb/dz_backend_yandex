import requests

# 1. Продукты, цена которых < 20
content = requests.get('https://fakestoreapi.com/products').json()

for item in content:
    if item['price'] < 20:
        print(f'Продукт: {item["title"]} Цена: {item["price"]}')


# 2. Все категории
content = requests.get('https://fakestoreapi.com/products/categories').json()

for i in content:
    print(i)


# 3. Все продукты с категорией jewelery
content = requests.get('https://fakestoreapi.com/products/category/jewelery').json()

for i in content:
    print(i['title'])
    