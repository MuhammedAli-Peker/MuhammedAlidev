#Enumarete and Zip Function
#döngüde çevirilen değerlerini index'ini takip etme

languages=["Java","Python","C","Rust"]
index=0
for language in languages:
    print(f"Index {index} and {language}")
    index+=1
    
#döngülerde enumarete() fonksiyonu ile bunu daha basit bir şekilde yapabiliriz :

list(enumerate(languages))
print(list(enumerate(languages)))

for index,language in enumerate(languages):
    print(f"index: {index} and language: {language}")



for index,language in enumerate(languages,2):  #  hangi sıradan başlamasi gerektiğini seçebiliyoruz
    print(f"index: {index} and language: {language}")
    
    


#Zip() fonksiyonu ile birden fazla listeyi döngülerde kullanmak. Listeleri tuple olarak birleştirir
foods=["Apple","Watermelon","Cherry","Orange"]
frices=[10,20,15,30]

for food,frice in list(zip(foods,frices)):
    print(f"Food: {food}")
    print(f"Price: {frice}")



#List comprehensions and useful functions with lists:
#Boş bir listeye eleman eklemek:

even_number=[]
for num in range(21):
    if  num % 2 ==0:
        even_number.append(num)

print(even_number)

#list comprehensions

even_numbers=[num for num in range(21) if num % 2 ==0] # daha kısa hali
print(even_numbers)


numbers=[1,2,3,4,5]
result=[("even",num) if num %2==0 else (num,"odd") for  num in numbers]
print(result)

#filter() fonksiyonu
words=["tree","cloud","mountain,","river","sky","apple","app","Hi"]

def is_long_word(word):
    return len(word)  < 4

long_words=list(filter(is_long_word,words)) #dönügen belirli elemanlari seçiyor
print(long_words)

#map() fonksiyonu, Fonksiyonlar için döngüden elemanları argümana çeviriyor

#örneğin celcius'u fahrenite'a çevirmek:
celcius=[0,10,20,30,40]

def to_fahrenheit(tempreture):
    return (tempreture* 9/5) + 32

fahrenheit=list(map(to_fahrenheit,celcius))
print(fahrenheit)

#sum() fonksiyonu(toplama fonksiyonu):
numbers=[10,20,30,40]
print(sum(numbers))
print(sum(numbers,10)) #posisyonel argüman yanindaki değeri de ekliyor toplama
print(sum(numbers,start=20))



#Lambda Fonksiyonlari:
def square(num):
    return num**2
print(square(4))
lambda num : num**2  #anonim bir fonksiyon özel tanimlanmiş değil .çoğu yerde kullanilabilir

numbers=[1,2,3,4,5]
even_number=list(filter(lambda x: x%2==0,numbers)) # daha öz daha basit daha sade daha kullanişli
print(even_number)                                 #amaç basitlik daha karmaşik yapilar oluşturmamalisin