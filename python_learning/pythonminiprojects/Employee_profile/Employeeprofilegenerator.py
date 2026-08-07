#My first project in python. This project is a simple employee profile generator. It takes the employee's information as input and generates a profile for the employee.


#Personel information
employee_name=input('please, enter your name here: ')
employee_age=int(input('please, enter your age here: '))
employee_gender=input('please, enter your gender here: ') 
employee_address=input('please, enter your address here: ')
#job information
employee_department=input('please, enter your department here: ')
position=input('please, enter your position here: ')
expected_salary=int(input('please, enter your expected salary here: '))
experience_years=int(input('please, enter your experience years here: '))

employee_profile=(f'Employee Name: {employee_name} | Employee Age: {employee_age} | Employee Gender: {employee_gender} | Employee Address: {employee_address} | Employee Department: {employee_department} | Employee Position: {position} | Employee Expected Salary: ${expected_salary} | Employee Experience Years: {experience_years}')
                                                                                                                                                                                                                                                                                                                    

print(employee_profile)
print('Employee profile has been generated successfully!')

#what is company expectations from the employee
expected_salary_range=50000
expected_experience_years=5
expected_age_range=30
minimum_age=24
expected_employee_position='Data analyst or Data scientist'



#checking if the employee meets the company expectations (after ı learned about if else statements)


#sending employee to refuse or allow message. after that creating person's  profile if he is allowed to job.

#güncellenecek boş zamanda
