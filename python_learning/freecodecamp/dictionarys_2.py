products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}
#anahtarları yazdırmak için
for price in products.values():
    print(price)

#value'ları yazdırmak için:   
for product in products.keys():
    print(product)
    
for product in products:
    print(product)
print("-------------------")    
#ikisinde yazdırmak için
for product in products.items():
    print(product)
    
for product,price in products.items():
    print(product,":",price)
print("------------------")    
#örneğin dicteki ürünlere tek tek indirim uygulayıp yazdırmak için:
for product,price in products.items():
    products[product] = round(price * 0.8)
    
print(products)

#enumerate() ile index çıkartma:
for product in enumerate(products):
    print(product)
    
for index,product in enumerate(products):
    print(index,product)
    
for index,price in enumerate(products.values()):
    print(index,price)
    
for index,product in enumerate(products.items()):
    print(index,product)
    
for index,product in enumerate(products.items(),1):   #indexlemeye 1.siradan başladi yanina verdiğimiz değerde nbaşliyor
    print(index,product)