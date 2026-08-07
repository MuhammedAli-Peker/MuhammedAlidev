# Operators in integer numbers
my_int1=40
my_int2=60
my_sum=my_int1+my_int2
print("The sum of my_int1 and my_int2 is:", my_sum)
my_multiplication=my_int1*my_int2
print("The multiplication of my_int1 and my_int2 is:", my_multiplication)
my_division=my_int1/my_int2
print("The division of my_int1 and my_int2 is:", my_division)

#Operators in float numbers
my_float1=12.5
my_float2=25.25
my_sum=my_float1+my_float2
print("The sum of my_float1 and my_float2 is:", my_sum)

sum=my_int1+my_float1
print("The sum of my_int1 and my_float1 is:", sum)
print(type(sum))

mod_ints=my_int1%my_int2
print("The modulus of my_int1 and my_int2 is:", mod_ints) #bölme işlemi sonucu kalanı verir. kalansız bir bölme işlemi için kullanılır. Örn: 5%2=1, 4%2=0, 7%3=1
mod_floats=my_float1%my_float2
print("The modulus of my_float1 and my_float2 is:", mod_floats)

floor_division=my_int1//my_int2
print("The floor division of my_int1 and my_int2 is:", floor_division) #bölme işlemi sonucu tam sayı kısmını verir. Örn: 5//2=2, 4//2=2, 7//3=2  !!!ÖNEMLİ

exp_int=my_int1**my_int2
print("The exponentiation of my_int1 and my_int2 is:", exp_int) #üs alma işlemi yapar. Örn: 2**3=8, 3**2=9, 4**0.5=2.0 !!!ÖNEMLİ

my_number=10
my_number=float(my_number) #int tipindeki bir sayıyı float tipine dönüştürür. Örn: 10 -> 10.0
print(f"The type of my_number is: {my_number}" )
print(f"The type of my_number is: {type(my_number)}" )

str_number="10"
str_float_number="10.5"
number_int=int(str_number) #str tipindeki bir sayıyı int tipine dönüştürür. Örn: "10" -> 10
float_number=float(str_float_number) #str tipindeki bir sayıyı float tipine dönüştürür. Örn: "10.5" -> 10.5
print(f"The type of number_int is: {number_int}" )
print(f"The type of number_int is: {type(number_int)}" )
print(f"The type of float_number is: {float_number}" )
print(f"The type of float_number is: {type(float_number)}" )


my_number_x=3.251
my_number_y=2.357
rounded_number=round(my_number_x) #float tipindeki bir sayıyı en yakın tam sayıya yuvarlar. Örn: 3.251 -> 3, 3.5 -> 4, 3.75 -> 4 
rounded_number_y=round(my_number_y,1) #float tipindeki bir sayıyı belirtilen ondalık basamak sayısına yuvarlar. Örn: 2.357 -> 2.4, 2.35 -> 2.4, 2.34 -> 2.3
print(f"The rounded number is: {rounded_number}" )
print(f"The rounded number_y is: {rounded_number_y}" )

#mutlak değer alma işlemi
my_number_z=-5
absolute_value=abs(my_number_z) #mutlak değer alma işlemi yapar. Örn: -5 -> 5, 5 -> 5, -3.5 -> 3.5
print(f"The absolute value of my_number_z is: {absolute_value}" )


power_number=pow(3,4) #3 sayısının 4. kuvvetini alır. Örn: 3^4=81, 2^3=8, 5^2=25
print(f"The power of 3 to the 4 is: {power_number}" )
power_number2=pow(2,3,5) #2 sayısının 3. kuvvetini alır ve 5 ile mod alır. Örn: 2^3 mod 5=3, 3^4 mod 5=1, 5^2 mod 3=1
print(f"The power of 2 to the 3 mod 5 is: {power_number2}" )

#augmented operators
x=5
x+=3 #x=x+3
print(f"The value of x is: {x}" )
x-=2 #x=x-2
print(f"The value of x is: {x}" )
x*=5
print(f'The value of the x is: {x}')
x//=6
print(f'The value of the x is: {x}')
x%=4
print(f'The value of the x is: {x} ')
x**=5
print(f'The value of x is: {x}')
gretting='hello'
gretting+=' world'
print(gretting)
example='meal'
example*=5
print(example)