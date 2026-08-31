my_box = {
    "foods" : ["apple","banana"],
    "toy" : "Spiderman",
    "money" : 40,
    "number" : 12.1
      
}

print(my_box["foods"])
print(my_box["money"])

products = dict([("cherry",20),("weapon","sword"),("price",15.5)]) #dict oluştuma metodu
print(products["weapon"])
print(products["price"])

#dict  value eklemek ve değiştirmek:
my_box["foods"] = "watermelon" # value yu bu şekilde değiştirebiliriz
print(my_box["foods"])

my_box["world"] = "Earth" #hiç olmayan bir key-value ikilisi ekledik
print(my_box["world"])

#Dictionary'deki temel metotlar:

#get() metodu sözlğkteki değeri döndürür eğer key bulamazsa default girilen değeri döndürür
print(my_box.get("toy"))
print(my_box.get("game","Fifa")) # "game" keyi bulunmadığı için default girdiğimiz değeri döndürdü
print(my_box.get("game")) # None döner default girilmediği için

#keys() ve values() , anahtarları ve değerleri görmek için
print(my_box.keys())
print(my_box.values())
#hepsini görmek için hem key hem value items() metodu:
print(my_box.items())

#clear() tüm key-value ikililerini siler:
products.clear()
print(products)

#pop() metodu: girilen key değrini value değeriyle beraber siler eğer key value dict'teki kayler ile eşleşmezse default girilen değeri döndürür
#eğer default değer yoksa *KEYERROR verir
my_box.pop("world") # world key ile valuesini siler
my_box.pop("game",10) # game key'i olmadiği için 10 döndürür eğer değer girilmezse hata verir!

#popitem() metodu: son siradaki key_value iklisini siler
my_box.popitem()
print(my_box)
#update() metodu: key-value değeri eklenir yeni bir dict ile eğer key halihazirda dic'te mevcutsa değerini eklenen değerle değiştirir sadece.
my_box.update({"world":"earth","Tokens":15})
print(my_box)
my_box.update({"money":100})
print(my_box) # var olan value değerini değiştirdi sadece