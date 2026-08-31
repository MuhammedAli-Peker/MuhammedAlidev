#mutable(değiştirilebilir), küme mantıği ile çalişir ayni eleman iki kez bulunamaz, siranin önemi yoktur.
#hızlı filtreleme ve kontrol: bir eleamin listede olup olmadğini çok hizli bir biçide kontrol etmek için kullanılır
#matematiksel küme işlemleri için kullanilir
#tekrarlayan sayilari silmek için kullanılır
#içine liste ve dict saklanamaz

my_set = {1,2,3,4,5,"a"}
print(my_set) # sıra önemsiz karışıkta verebilir

set() # set
{} #dict

my_set.add(6)
print(my_set)
my_set.add(1) # eleman zaten bulunduğu için eklemez
print(my_set)

#eleman silmenin sadece iki yolu var: .remove() ve .discard() metotları
#remove eleman yoksa hata veririr, discard vermez
my_set.remove(2)
my_set.discard(3)
print(my_set)
#.clear() tüm elemanları siler

#.supset() seçili kümenin diğer kümenin alt kümesi olup olmadığını döner True/False
#.superset() seçili elemanın diğer elemeanin üst kümesi olup olmadığını döner T/F

your_set = {4,5}
print(my_set.issubset(your_set))
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set))
print(your_set.issubset(my_set))

#isdisjoint() : ayrik küme olup olmadiğin kontrol ediyor eğer ortak eleman yoksa True  varsa False dönüyor.

their_set = {7,8,4}
my_set | their_set 
print(my_set | their_set) # iki setteki tüm elemanları döndürür
my_set & their_set
print(my_set & their_set) # ortak elemanları döndürür
my_set - their_set  # kümelerdeki temel mantık A dan olup B den olmayan elemanları dönüdürüyor burada my'da olup their'de olmayanları dönüdürecek
print(my_set - their_set)
my_set ^ their_set #sadece kesişim dışındaki elemalari aliyor:
print(my_set ^ their_set)

# |= &= -= ^=  bu operatörleri eşittir ile kullanırsak ilk seti direk güncelliyor


print(1 in my_set)