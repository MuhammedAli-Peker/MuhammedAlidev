#zip function exercises

names = ["elma", "armut", "muz", "çilek"]
prices = [10, 15, 8, 20]

result = []
for name,price in zip(names,prices):
    product = {"name": name , "price": price}
    result.append(product)
    
print(result)
print("---------------------------")


names = ["elma", "armut", "muz", "çilek"]
prices = [10, 15, 8, 20]
stocks = [5, 0, 3, 0]

result = []
for name,price ,stock in zip(names,prices,stocks):
    products = {"name":name , "price": price , "stock":stock , "available":None} 
    if products["stock"] > 0 :
        products["available"] = True
        
    else:
        products["available"] = False
    result.append(products)
    
print(result)

#lambda function exercises

print(sorted(result , key=lambda product :product["price"])) # lambda fonksiyonu ile fiyatları küçükten büyüğe sıraladık
