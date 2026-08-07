def hello():
    print('hello, World')
hello()
def sum(a,b):
    return  a+b
sum(2,3)
my_sum=sum(1,2)
print(my_sum)

#LEGB RULES
#İçten dışa doğru gider.
x='Global'
def enclosing():
    x='Enscope'
    y="World"
    def local1():
        x='local'
        print(x)
    local1()
    print(x)   
enclosing()
print(x)
# print(y) hata veririr çünkü y içerde tanımlandı dışarıda değil.
#dışarda tanımlana değeri içerde kullnabiliriz fakat içerde tanımlanan değeri dışarda kullanamayız.

def outer():
    msg="Hello There"
    res=" "
    def inner():
        nonlocal res #allow modification of an enclosing variable
        res="How are you?"
        print(msg) #accessing msg from outer function
        global  number #Globalleştirdi artık dışarıdada kullanılabilir sayı ayrıca sayıyı modifiye edebiliriz.
        number=25
        
    inner()
    print(res) #now res is accessible and modified
outer()
        
my_var=100 #Global scope heryerden erişilebilir