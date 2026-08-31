import math
# module_name.funciton_name()

math.sqrt(26)
print(math.sqrt(36))  #karekök alma işlemi
#alias:
import math as m  # import module_name as alies
m.sqrt(100) #modül ismini kısalttık artık sadece m diye çağırarak işlemimizi uygulayabiliyoruz
print(m.sqrt(100))

#from: sadece modül içindeki spesifik fonksiyonlari çağirmak için:

from math import radians, tan, sin, cos
from math import  tan as t , sin as s

angel_degrees = 60
angel_radians = radians(angel_degrees)

tane_value = tan(angel_radians)
sine_value = sin(angel_radians)

print(round(sine_value,1))
print(round(tane_value,1))

from math import * #asterik : math yazmamıza gerek yok diğer fonksiyonların kendilerini kullanabilriiz fakat pek tercih edilmiyor, isim çakışmalarına sebebbiyet verebilir.
print(sqrt(4))


# DATETİME Modülü : tarihlerde bu modülü kullanıyoruz!

import datetime
birth_day = datetime.date(2001,5,12)
print(birth_day.day)
print(birth_day.month)
print(birth_day.year)


import statistics # king