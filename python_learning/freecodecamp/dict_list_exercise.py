inventory = [
    {"name": "elma", "price": 10},
    {"name": "armut", "price": 15},
    {"name": "muz", "price": 8}
]
print(inventory[0]["name"])
print(inventory[1]["price"])


for item in inventory:
    print(item["name"],"-",item["price"])
    
#for- else yapısındaki else eğer döngü break ile kesilmezse birkezlik çalışır    
total = 0

for item in inventory:
    total += item["price"]

print(total)
print("--------------------------")


numbers = [4, 8, 15, 16, 23, 42]
result = {"even":[],
          "odd":[],
          "even_count":0,
          "odd_count":0
          }


for number in numbers:
    if number % 2 == 0:
        result["even"].append(number)
        result["even_count"] += 1
    else:
        result["odd"].append(number)
        result["odd_count"] += 1
    
print(result)

print("-------------------------")

products = [
    {"name": "elma", "price": 10, "stock": 5},
    {"name": "armut", "price": 15, "stock": 0},
    {"name": "muz", "price": 8, "stock": 3},
    {"name": "çilek", "price": 20, "stock": 0}
]
stock = {
    "in_stock": [],
    "out_stock": []
}
total_price = 0

for product in products:
   if  product["stock"] > 0:
       stock["in_stock"].append(product["name"])
       total_price += product["price"] * product["stock"]
   elif  product["stock"] == 0:
       stock["out_stock"].append(product["name"])
       



print(stock)
print(f"Total price: {total_price}")

print("---------------------")

products = [
    {"name": "elma", "price": 10, "stock": 5},
    {"name": "armut", "price": 15, "stock": 0},
    {"name": "muz", "price": 8, "stock": 3},
    {"name": "çilek", "price": 20, "stock": 0},
    {"name": "karpuz", "price": 25, "stock": 2},
    {"name": "kiraz", "price": 30, "stock": 1}
]

result = {
    "cheap": {"items":[] , "count" : 0 , "total_value"  :0},
    "expensive" : {"items": [], "count":0 , "total_value":0}
}

for product in products:
    
    if product["price"] <= 15 :
        result["cheap"]["items"].append(product["name"])
        result["cheap"]["count"] += 1
        result["cheap"]["total_value"] += product["price"] * product["stock"]
    elif product["price"] > 15:
        result["expensive"]["items"].append(product["name"])
        result["expensive"]["count"] += 1
        result["expensive"]["total_value"] += product["price"] * product["stock"]


        
print(result)