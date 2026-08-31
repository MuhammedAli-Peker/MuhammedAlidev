#After ı finished conditions and booleans in Freecodecamp.org, ı made this ticket booking calculator in 30 july.
#ı will upgrade this in future  if ı learn loops.



user_age=int(input('Please enter your age here: '))


if user_age >= 18:
    print('You can watch these movies.')
    #Movie choice
    movie1='Spiderman'
    movie2='Batman'
    movie3='Odyssey'
    base_price=20
    user_movie=input('Please enter your movie choice here: ')

    if user_movie==movie1:
            print('you chosed the movie now you need to choice seat')
            user_seat=input('Please Enter your seat type here.')
            seat_type1='Premium'
            seat_type2='Vip'
            seat_type3='Normal'
        
            #Seat choice
            if user_seat == seat_type1:
                print('You chosed premium seat it took 20 dolars.')
                seat_type1=20
                user_seat=seat_type1
                ticket_price=base_price+user_seat
                print('Your ticket price:', ticket_price)
                print('Your seat choice was justified.')
            elif user_seat == seat_type2:
                print('You chosed Vip seat it took 10 dolars.')
                seat_type2=10
                user_seat=seat_type2
                ticket_price=base_price+user_seat
                print('Your ticket price:', ticket_price)
                print('Your seat choice was justified.')
            elif user_seat==seat_type3:
                print('You chose normal type seat.')
                seat_type3=0
                user_seat=seat_type3
                ticket_price=base_price+user_seat
                print('Your ticket price:', ticket_price)
                print('Your seat choice was justified.')
            else:
                print('You have to chose seat type.')   
        
            

    elif user_movie==movie2:
             print('you chosed the movie now you need to choice seat')
             user_seat=input('Please Enter your seat type here.')
             seat_type1='Premium'
             seat_type2='Vip'
             seat_type3='Normal'
         
             #Seat choice
             if user_seat == seat_type1:
                 print('You chosed premium seat it took extra 20 dolars.')
                 seat_type1=20
                 user_seat=seat_type1
                 ticket_price=base_price+user_seat
                 print('Your ticket price:', ticket_price)
         
             elif user_seat == seat_type2:
                 print('You chosed Vip seat it took extra 10 dolars.')
                 seat_type2=10
                 user_seat=seat_type2
                 ticket_price=base_price+user_seat
                 print('Your ticket price:', ticket_price)
         
             elif user_seat==seat_type3:
                 print('You chose normal type seat.')
                 seat_type3=0
                 user_seat=seat_type3
                 ticket_price=base_price+user_seat
                 print('Your ticket price:', ticket_price)
         
             else:
                 print('You have to chose seat type.')   
         
             print('your seat choice was justified.')
             print('Movie will be in hall 2')
             print('Batman movie will start in 15 minutes')
    elif user_movie==movie3:
            print('you chosed the movie now you need to choice seat')
            user_seat=input('Please Enter your seat type here.')
            seat_type1='Premium'
            seat_type2='Vip'
            seat_type3='Normal'
        
            #Seat choice
            if user_seat == seat_type1:
                print('You chosed premium seat it took 20 dolars.')
                seat_type1=20
                user_seat=seat_type1
                ticket_price=base_price+user_seat
                print('Your ticket price:', ticket_price)
        
            elif user_seat == seat_type2:
                print('You chosed Vip seat it took 10 dolars.')
                seat_type2=10
                user_seat=seat_type2
                ticket_price=base_price+user_seat
                print('Your ticket price:', ticket_price)
        
            elif user_seat==seat_type3:
                print('You chose normal type seat.')
                seat_type3=0
                user_seat=seat_type3
                ticket_price=base_price+user_seat
                print('Your ticket price:', ticket_price)
        
            else:
                print('You have to chose seat type.')   
        
            print('your seat choice was justified.')
        
            print('Movie will be in hall 3')
            print('Odyssey movie will start in 25 minutes')
    else:
        print('you have to enter your movie here. Try again')
    
  
elif 7< user_age <18  :
    
    print('You can watch these movies')
    print('Superman ,Doctor Strange and İnside Out')
    movie1='Superman'
    movie2='Doctor Strange'
    movie3='İnside Out'
    seat_type1='Premium'
    seat_type2='Vip'
    seat_type3='Normal'
    base_price=20
    print('Ticket price is 20 dolar. if you are a student, you can use student discount. ')
    student_discount=10
    is_student=input('Please answer yes or no.')
    if is_student=='yes' and user_age > 13:
         print('You are eligible for the student discount.')
         user_movie=input('Please, enter your movie choice here. ')
         if user_movie==movie1:
            print('you chosed movie now you need to choice seat')
            user_seat=input('Please, enter your seat type here. ')
            if user_seat=='Premium' or user_seat =='Gold':
                 seat_type1=5
                 seat_type2=5
                 ticket_price=base_price+5-student_discount
                 print('your seat was justified')
                 print('Ticket Price: ', ticket_price)
            elif seat_type3=='Normal':
                 seat_type3=0
                 ticket_price=base_price-student_discount
                 print('Your seat was justified')
                 print('Tiket Price: ',ticket_price)
            else:
                 print('You have to choice seat type!')
         if user_movie==movie2:
            print('you chosed movie now you need to choice seat')
            user_seat=input('Please, enter your seat type here. ')
            if user_seat=='Premium' or user_seat =='Gold':
                 seat_type1=5
                 seat_type2=5
                 ticket_price=base_price+5-student_discount
                 print('your seat was justified')
                 print('Ticket Price: ', ticket_price)
            elif seat_type3=='Normal':
                 seat_type3=0
                 ticket_price=base_price-student_discount
                 print('Your seat was justified')
                 print('Tiket Price: ',ticket_price)
            else:
                 print('You have to choice seat type!')
         if user_movie==movie3:
            print('you chosed movie now you need to choice seat')
            user_seat=input('Please, enter your seat type here. ')
            if user_seat=='Premium' or user_seat =='Gold':
                 seat_type1=5
                 seat_type2=5
                 ticket_price=base_price+5-student_discount
                 print('your seat was justified')
                 print('Ticket Price: ', ticket_price)
            elif seat_type3=='Normal':
                 seat_type3=0
                 ticket_price=base_price-student_discount
                 print('Your seat was justified')
                 print('Tiket Price: ',ticket_price)
            else:
                print('You have to choice seat type!')
    elif is_student=='no'and user_age > 13 :
         print('You are not eligible for the student discount. ')
         user_movie=input('Please, enter your movie choice here. ')
                          
    else:
         print('Please answer with yes or no!')
else:
    print('You have to enter your age here. Please try again!')


 

 





