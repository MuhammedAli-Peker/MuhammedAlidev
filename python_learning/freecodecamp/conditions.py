#Compration operators
print(4<5)
print(1>2)
print(1==1)
print(5==4) # Equal
print(3!=4) # Not equal
print(3!=3)
print(5<=10) #Greater or euqal
print(5>=10) #Lower or equal

#if-else statement
age=20

if age == 10:
    print('You are ten years old.')

if age <= 18:
    print('You are a child!')
else:
    print('you are a adult.')

age1=18
if age1 < 18:
   print('you are a child.')
elif age1 == 18:
   print('you are a teenage.')
else:
    print('You are a adult.')

#elif ile istediğimiz kadar şart ekleyebiliyoruz(we can add as many conditions as we want with elif.)

is_citizen=False
citizen_age=17

if is_citizen == True:
    if age >= 18:
     print('You are eligible to vote.')
else:
   print('You are not eligible to vote.')

#turthy and falsy values
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(0.0))
print('') #bos string false
print(bool(True))
print(bool('1'))
print(bool(1))

#and operator
#ilk degeri kontorl eder eğer ilk deger yanlıssa 'false' doner.Eger ilk deger dogruysa iknici degere gecer ve onu kontrol eder o yanlıssa gene 'false' doner eger dogruysa(iki cevapta dogruysa.) 'true'doner cevap 'turhty value' olarak degerlendirilir.
print(is_citizen and citizen_age)

if is_citizen and citizen_age >= 18:
   print('you are eligible to vote.')
else:
   print('you are not eligible to vote.)')

#or operator
#iki cevaptan biri dogruysa true doner yoksa false olur.

studen_age=19
is_student=False
print(studen_age or is_student)

if studen_age < 18 or is_student:
   print('you are eligible for a student discount')
else:
   print('you are not eligible for a student discount.')

#Not operator
#Always turn 'false' to 'true' or 'true' to 'false'.

print(not '')
print(not '1')
print(not 1)

is_admin=False
if not is_admin:
   print('access denied for non-Administrators.')
else:
   print('welcome,Administrator!')

