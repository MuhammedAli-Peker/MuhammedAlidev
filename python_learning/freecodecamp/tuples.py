#A tuples is a Python data type used to create an ordered sequence of values. Tuples can contain a mixed set of data types like this
#tuple'dan listelerde olduğu gibi ekleme çikarma yapilamaz
#tupel'a eklenen eleman bir daha değiştirilemez!

names=("Ali","Burak","Aykut","Eylül")
print(names[2])
print(names[-1])

print(len(names))

names_sorted=sorted(names)
print(names_sorted)

print("Ali" in names)

"""new_names= names + ("Greenwood")  print(new_names)
                      Bu şekilde tupellara ekleme yapamiyoruz
              """
              
developer="Ali"
print(tuple(developer)) #listelerdeki gibi

numbers=(3,4)   #listedeki gibi
number1,number2=numbers
print(number1)
print(number2)

print(names[1:3])

"""
Tupellari nerede kullaniyoruz:
                            If you need a dynamic collection of elements where you can add, remove and update elements,
                            then you should use a list. If you know that you are working with a fixed and immutable collection of data,
                            then you should use a tuple.
    """


#Yaygın Tuple metotları:
my_list=(1,1,"Data","world","Software","Data","Software")
list_count=my_list.count("Software") #tuple dan seçili elman sayisini buluyor. değer girilmezse hata verir.
print(list_count)

my_list.index("Data") #istenen öğenin sirasini belirtir
print(my_list.index("Data",3)) #yanındaki sayı kaçinci siradan itibaren bakacağini gösterir. ikinci sirdadaki data'yi atlayip 4.siradakini bulacak.

#Tupellari özelleştirmek için  ,reverse= siralamayi terse çeviriyor
#Key= , tuperllari özelleştirmeye yarayan parametre.
# normalde sayılar büyükten küçüğe ve harfler alfabetik olarak sırlanır ,key veya revrse ile bu parametreleri özelleştirebiliriz
languages=("java","Rust","C++","Pyhton","Javascript","Go")
print(sorted(languages,key=len)) #karakter uzunluğuna göre sıralar
print(sorted(languages,key=str.lower)) # tüm harfleri küçük yaparak siralar
print(sorted(languages,reverse=True))
print(sorted(languages,key=len,reverse=True)) # uzunuklara göre tersten sıraladık örnek