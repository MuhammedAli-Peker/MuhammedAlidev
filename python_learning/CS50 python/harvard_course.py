name=input('Enter your name: ').strip().title() #Title capitalize first letter of each word  | Kodun okunabilirliği açısından hepsini tek satırda yazmak yani daha az satır kullnmak daha mantıklı
name=name.strip()   #remowe white space from str
print('Hello, ' + name + '!')
print(f"Hello, {name}")
first , last=name.split(" ")
print(first)
print(last)





















#Önemli :comment sectionları kodu yazmadan önce algoritma oluşturmak içn kullanabilir ve daha rahat bir yazı imkanı sunar . kodun daha düzenli olmasını sağlar
""" 
This is a comment section 
"""
