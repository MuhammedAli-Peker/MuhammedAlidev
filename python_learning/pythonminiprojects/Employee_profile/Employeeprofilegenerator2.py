#Employee profile generator version 2 with functions

def admin_access(password,name):
    admin_name=input("Please enter your name here ").strip().title()       
    if admin_name.isalpha():
        if admin_name==name:
            admin_password=input("Please enter your password here ")
            if admin_password.isnumeric():
                if admin_password==password:
                    print(f"Welcome to employee managment system {name}!")
                    dep=input("Enter which department you want to perform the action on ").capitalize().strip()
                    return dep
                else:
                    print("Your password is wrong,try again!")               
            else:
                print("Your password must  consist only of numbers.")
        else:
            print("Your name is wrong,try again!")     
    else:
        print("Your username must consist only of letters.")
    
def employee_management(department):
    departments=["Marketing","Production","İnformation Technology"]
    if department in departments:
        employees=["Burak","Ahmet","Ali","Büşra"]
        employee_name=input("Please enter the employee's name here ").strip().title()
        if employee_name in employees:
            return f"Employee Name: {employee_name} \nDeparment Name: {department} | Employee Salary: 5000$"
        else:
            return "You must enter a employee name that is working for your company!"
    else:
        return "You must enter a department name in your company!"    
    
employee_deparment=admin_access("123","Ali")   
if employee_deparment:
    print(employee_management(employee_deparment))
else:
    print("Access denied. Employee management system was not started!")
    








    
"""Önemli bilgiler: 1- input fonksiyonunu inistance ile kontrol edemiyoruz çünkü bu fonksiyona girdiğimiz bütün ifadeler string algilanir
o yüzden kontrol etmemize gerek yok 2-password kullanici işlemleri gibi şeyleri string ifade olarak almaliyiz int ya da float değil.
3-strip,capitalize,upper,lower,title,startswith,endswith gibi fonksiyonlari hep kullancaiz bunlari iyi anla
4-isaplha=harf kontolü,  isdigit veya isnumeric rakam kontrolü
 """      