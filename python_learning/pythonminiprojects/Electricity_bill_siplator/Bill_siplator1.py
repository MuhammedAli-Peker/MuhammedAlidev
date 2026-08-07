subscriber_name=input('Please, enter your name here: ')
street_name=input('Please, enter your street name here: ')
apartman_name=input('Please, enter your apartman name here: ')
building_number=input('Please, enter your building number here: ')
flat_number=input('please enter your flat number here: ')
subscriber_adress=f'Street: {street_name} | Apartman: {apartman_name} | Building No: {building_number} | Flat No: {flat_number}'
password=True
kw1=1.27 #1 kw electricity price
electricity_usage=float(input('Please enter your electricity usage here '))

#electricity bill creating
if electricity_usage <=250 and password==True :
    
   bill=electricity_usage*kw1
   print(f'Subscriber Name: {subscriber_name} \nSubscriber Adress:[ {subscriber_adress} ]\n Electricity Bill: {bill}$ ')
   
elif electricity_usage >250 and password==True :
    kw1+=1
    bill=electricity_usage*kw1
    print(f'Subscriber Name: {subscriber_name} \nSubscriber Adress:[ {subscriber_adress} ]\n Electricity Bill: {bill}$ ')
else:
    print('You have to enter your electricity usage here!')

#Abone olup olmadıgını kontol etme eklenecek
