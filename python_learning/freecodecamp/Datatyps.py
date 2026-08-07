#veri türleri
int_var = 10
float_var = 20.5
str_var = "Hello, World!"
boolean_var = True
set_var = {1,'apple', 3.14} # set() fonksiyonu ile oluşturulur. set() fonksiyonu ile oluşturulan setler, listelerden farklı olarak, aynı elemanları birden fazla kez saklamazlar.set() fonksiyonu ile oluşturulan setler, listelerden farklı olarak, sıralı değildirler. set() fonksiyonu ile oluşturulan setler, listelerden farklı olarak, değiştirilemezler.
dictonary_var = {"name": "John", "age": 30, "city": "New York"}
# print(dictonary_var) #  key-value şeklinde veri saklamaya yarar.
tuple_var = (1, "banana", 3.14) # tuple değiştirilemez. listeler değiştirilebilir.
range_var = range(5) # 0,1,2,3,4 0 dan 5 e kadar olan sayıları üretir. range(5) 0 dan 5 e kadar olan sayıları üretir.
list_var = [1, "orange", 3.14] # farklı türde veri tipleri saklayabilir. listeler [] ile tanımlanır. tuple () ile tanımlanır.
none_var = None #  boş değer saklamak için kullanılır.

print(type(int_var)) # <class 'int'> değişkeninin veri tipini verir
print(isinstance(int_var, float)) # False döner. isinstance() fonksiyonu bir değişkenin belirli bir veri tipine ait olup olmadığını kontrol eder.


