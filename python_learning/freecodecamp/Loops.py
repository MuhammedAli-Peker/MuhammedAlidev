programming_languages=["java","python","C++","Rust","Javascript"]

#for döngüsü:
for language in  programming_languages:
    print(language)

for char in "code":  # string'in harflerini tek tek gezmek
    print(char)
     
         
#nested for döngüsü:
categories=["Fruit","vegetable"]
foods=["apple","carrot","banana"]
for category in categories:
    for food in foods:
        print(category,food)
        
#while döngüsü:
secret_number = 3
guess = 0

# while guess != secret_number:
#     guess = int(input("Guess the number (1-5): "))
#     if guess != secret_number:
#         print("Try again")

print("You got it!")

#break and continue
names=["Burak","Ali","Zeynep","Asya"]
for name in names:
    if name=="Asya":
        break #seçili öğeye gelice taramayi sonlandiriyor
    print(name)
    
for name in names:
    if name=="Zeynep":
        continue  #listede seçili öğeyi direk atliyor
    print(name)
    
words=["world","rythm","apple","sky","fly"]
for word in words:
    for letter in word:
        if letter.lower() in "aeiou":
            print(f"'{word}' contains the vowel '{letter}'")
            break
    else:  # else for  döngüsü ile aynı  hizada olmalı
        print(f"'{word} had no vowels")



for number in range(3): #sadece int value ile işlem yapabiliriz
    print(number)

for number in range(1,5):  # sadece stop ile çalişir. ve boş değer girilirse type error verir
    print(number)
    
for number in range(2,10,2):  #start,stop,step
    print(number)

print("------------")

for number in range(10,2,-2): #azalan hali
    print(number)
    
numbers=list(range(2,10,2)) # range() ile liste oluşturma
print(numbers)