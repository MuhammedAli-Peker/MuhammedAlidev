#Temel kısım
str_var='hello, my name is Ali'
print('my' in str_var) # True döner. 'my' stringi str_var değişkeninde var mı kontrol eder.
print('John' in str_var) # False döner. 'John' stringi str_var değişkeninde var mı kontrol eder.
print(len(str_var)) # 21 döner. str_var değişkeninin uzunluğunu verir.
print(len(str_var))
print(str_var[18]) # 18. indexteki karakteri verir. 'A' döner.
print(str_var[-5]) # -5. indexteki karakteri verir. 'A' döner.

my_str='my name is'
my_str2='Ali'
my_plus_str=my_str + ' ' + my_str2 # stringleri birleştirir. 'my is name Ali' döner.
print(my_plus_str)

sound='happy'
repeat_sound=sound *5 # stringi 5 kez tekrarlar. 'happyhappyhappyhappyhappy' döner.
print(repeat_sound)
# birleştirm e ve tekrar etme işlemleri stringlerde kullanılabilir.
number=99
print(sound+ ' ' + str(number)) # string ve integer birleştirilemez. integer'ı stringe çevirerek birleştirebiliriz. 'my name is Ali 99' döner.

sound+=str(number)
print(sound) # += birleştirme işlemi yapar. 'happy99' döner.

name='Ali'
age=20
print(f'My name is {name} and I am {age} years old.') # f-string kullanarak değişkenleri string içinde kullanabiliriz. 'My name is Ali and I am 20 years old.' döner.
num1=12
num2=13
print(f'sum {num1} + {num2} = {num1+num2}') # f-string kullanarak değişkenleri string içinde kullanabiliriz. 'sum 12 + 13 = 25' döner.

print(sound[1:5]) # 1. indexten 4. indexe kadar olan karakterleri verir. 'appy' döner.
print(sound[:3]) # 0. indexten 2. indexe kadar olan karakterleri verir. 'hap' döner.
print(sound[3:7]) # 3. indexten 6. indexe kadar olan karakterleri verir. 'py99' döner.
print(sound[0:4:2]) # 0. indexten 3. indexe kadar olan karakterleri 2 adımda verir. 'hp' döner. 

#methodlar
x='amazing MONSTER'
x_up=x.upper()
print(x_up) # tüm karakterleri büyük harfe çevirir. 'AMAZING MONSTER' döner.
x_low=x.lower()
print(x_low) # tüm karakterleri küçük harfe çevirir. 'amazing monster' döner.
x_str=x.strip()
print(x_str) # baştaki ve sondaki boşlukları siler. 'amazing MONSTER' döner.
x_replace=x.replace('MONSTER','ALI')
print(x_replace) # 'MONSTER' stringini 'ALI' stringi ile değiştirir. 'amazing ALI' döner.
x_split=x.split()
print(x_split) # stringi boşluklardan ayırarak listeye çevirir. ['amazing', 'MONSTER'] döner
x_split1=x.split('M')
print(x_split1) # stringi 'M' karakterinden ayırarak listeye çevirir. ['a', 'azing ', 'ONSTER'] döner. 'M' ile ayrılanları ayrı bir kelime kabul ediyor
x_join=' '.join(x_split)
print(x_join) # listeyi stringe çevirir. 'amazing MONSTER' döner. join() methodu ile listeyi stringe çevirebiliriz. join() methodu ile listeyi stringe çevirirken, join() methodunun önüne yazdığımız karakteri liste elemanlarının arasına ekler.
x_start=x.startswith('amazing')
print(x_start) # stringin 'amazing' ile başlayıp başlamadığını kontrol eder. True döner.
x_end=x.endswith('MONSTER')
print(x_end) # stringin 'MONSTER' ile bitip bitmediğini kontrol eder. True döner.
x_find=x.find('MONSTER')
print(x_find) # stringin 'MONSTER' stringinin başladığı indexi verir. boşlukları da sayar. 8 döner. find() methodu ile stringin içinde aradığımız stringin indexini bulabiliriz. find() methodu ile aradığımız stringi bulamazsak -1 döner.
x_count=x.count('M')
print(x_count) # stringin içinde 'M' karakterinin kaç kez geçtiğini verir. 1 döner. count() methodu ile stringin içinde aradığımız stringin kaç kez geçtiğini bulabiliriz.
x_cap=x.capitalize()
print(x_cap) # stringin ilk karakterini büyük harfe çevirir. 'Amazing MONSTER' döner. capitalize() methodu ile stringin ilk karakterini büyük harfe çevirebiliriz.
x_allup=x.isupper()
print(x_allup) # stringin tüm karakterlerinin büyük harf olup olmadığını kontrol eder. False döner. isupper() methodu ile stringin tüm karakterlerinin büyük harf olup olmadığını kontrol edebiliriz.
x_alllow=x.islower()
print(x_alllow) # stringin tüm karakterlerinin küçük harf olup olmadığını kontrol eder. False döner. islower() methodu ile stringin tüm karakterlerinin küçük harf olup olmadığını kontrol edebiliriz.
x_title=x.title()
print(x_title) # stringin tüm kelimelerinin ilk karakterini büyük harfe çevirir. 'Amazing Monster' döner. title() methodu ile stringin tüm kelimelerinin ilk karakterini büyük harfe çevirebiliriz.
