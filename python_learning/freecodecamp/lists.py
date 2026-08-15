#The list data type is an ordered sequence of elements that can be comprised of strings,
#numbers, or even other lists. Lists are mutable and use zero-based indexing, meaning that the first element of the list is at index zero.

musics=["pop","rap","rock","classic"]
print(musics[1])
print("pop" in musics)
musics[2]="hiphop"
print(musics[2])
print(musics[-1])
box=[1,True,"Apple",3.14,"World",10]
print(box[2:5])
print(box[:3])

box.append("Code") #listeye yeni bir öğe ekliyoruz
box.extend(["Visual",100]) #Birden fazla öğeyi listeye eklemek için
box += ["Like",1] #Birden fazla öğeyi listeye eklemek için
print(len(box))
print(box)

box.remove(100) #listeden tek bir öğeyi kaldirmak için
print(box)

print(box.pop())#listedeki belirli bir öğeyi silmek için eğer değer girilmezse  son öğeyi bulur ve siler

#Listede spesifik bir noktaya öğe eklemek:
box.insert(1,"Cherry")
box.insert(2,"x")
print(box)
box[1:1]=["w","y"] #birden fazla öğeyi spesifik bir yere eklemek için
print(box)



#shorting lists
heroes=["superman","Batman","Antman","Thor","antman"]
heroes.sort() #listedeki ifadeleri eğer string iseler alfebetik siraya sokuyor (Büyük harfler öncelikli)
print(heroes)
heroes.sort(key=str.lower) # artik küçük ve büyük harflere bakmiyor
print(heroes)

heroescopy=heroes[:] #kopyaladik
print(heroescopy)
print(sorted(heroescopy,key=str.lower)) #kopyaladik

#Önemli sorted'da oluşan yeni bir liste oluyorken sort() metodundaki mevcut listeyi düzenliyor.

developer="jessica"
print(list(developer)) # harfleri tek tek listeler döngülerde lazim olacak
print("j" in list(developer))
name_words=list(developer)
del name_words[0:2] #listeden elemanli kaldirma (start:stop) stop dahil değil
print(name_words)

developer2=[1,"jessica",["dev",25,"python"]] #liste içinde liste index:2
print(developer2)


#listedeki değerleri değişkenlere atamak:
developer3=["Bob",23,"software engineer"]
name , age ,job = developer3  #eğer yeterli sayida öğe yoksa hata verir
print(name)
print(age)
print(job)
name,*others=developer3 # * ile listede geri kalan değerleri aliyoruz others=[23,"sofware engineer"]
print(others)

numbers=[1,2,3,4,5,6]
print(numbers[1::2])

numbers.clear() #listedeki bütün değerleri siler

numbers2=[1,2,3,4,5,6,7,8,9,10]
numbers2.reverse() #öğeleri tersten siralar
print(numbers2)

numbers2.index(3) #öğenini index'ini verir, reverse'den dolayi 7 geldi
print(numbers2.index(3))