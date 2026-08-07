#Applicant Profie
applicant_name=input('Please, enter your name here: ')
applicant_age=int(input('Please, enter your age here: '))
applicant_adress=input('Please, enter your adress here: ')
applicant_department=input('Please, enter your department here: ')
applicant_position=input('Please enter the position here: ')
applicant_expected_salary=int(input('Please, enter your expected salary: '))
applicant_profile=f'Applicant Name: {applicant_name} | Applicant Age: {applicant_age}\nApplicant Adress: {applicant_adress}\nApplicant Deparment: {applicant_department} | Applicant Position: {applicant_position} | Applicant Expected Salay: {applicant_expected_salary}'
print(applicant_profile)


#Requirement Profile:
salary_limit=5000 #per month
#Requirement positions:
requirement_position1='Software Engineer'
requirement_position2='Computer Engineer'
requirement_position3='ML Engineer'

#requirement position check and experience check:
if applicant_position==requirement_position1 or applicant_position==requirement_position2 or applicant_position==requirement_position3:
    print('Applicant afford positions that company want.')
    applicant_Experience=int(input('Please, specify your years of experience: '))
    if applicant_Experience >=3 :
        salary_limit*=4/3
        offered_sallary=applicant_expected_salary*5/4
        
        if offered_sallary<=salary_limit:
            print(f'We would like to extend a salary offer of :{round(offered_sallary)}$ per month')
        else:
            print('Your salary expectetion is above our budget\n please update your salary request')
    elif 1<=applicant_Experience<3:
        salary_limit*=6/5
        offered_sallary=applicant_expected_salary*7/6
        if offered_sallary<=salary_limit:
            print(f'We would like to extend a salary offer of :{round(offered_sallary)}$ per month')
        else:
            print('Your salary expectetion is above our budget\n please update your salary request')
    elif 0<applicant_Experience<1 :
        offered_sallary=applicant_expected_salary*4/5
        if offered_sallary<=salary_limit:
            print(f'We would like to extend a salary offer of :{round(offered_sallary)}$ per month')
        else:
            print('Your salary expectetion is above our budget\n please update your salary request')
    else:
        print('Please, enter your experience year')
else:
    print('You job application requset was rejected due to it does not afford our positions that we want it.')



#Comparing employe profile and requirement profile
#sending refuse message and allow mesage