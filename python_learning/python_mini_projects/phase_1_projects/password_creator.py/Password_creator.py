import random
import string
#şifre alimi ve karakter kontrolü:
def get_password():
    while True:
        password = input("Enter your new password here: ").strip()
        if len(password) < 8:
            print("Your password has to be longer than 8 character. Please enter again!")
        elif len(password) > 20:
            print("You password gas to be shorter than 20 character. Please enter again!")
        else:
            return password
#Büyük harf kontrolü:
def check_upper_case(password):
    for char in password:
        if char in string.ascii_uppercase:
            return True
    else:
        return False
#küçük harf kontrolü
def check_lower_case(password):
    for char in password:
        if char in string.ascii_lowercase:
            return True
    else:
        return False
#Özel karakter kontrolü:
def check_special_case(password):
    for char in password:
        if char in string.punctuation:
            return True
    else:
        return False
#Rakam kontrolü:
def check_digits(password):
    for char in password:
        if char in string.digits:
            return True
    else:
        return False

#Main fonksiyonuda bütün işlemleri birleştirme ve eklemeler yapma
def main():
    print("---Welcome to Password Creator---")
    passwords = []
    while True:
        user_password =  get_password()
        lower_case = check_lower_case(user_password)
        upper_case = check_upper_case(user_password)
        digit_case = check_digits(user_password)
        special_case = check_special_case(user_password)
        while True:
            if lower_case == True:
                if upper_case == True:
                    if digit_case == True:
                        if special_case == True:
                            print(f"You password was justified\nYour New Password : {user_password}")
                            passwords.append(user_password)
                            break
                        else:
                            print("Your password has to have at least one special character(!'^+%&*?<<#$)! Please try again with special character. ")
                            break
                    else:
                        print("Your password has to have at least one digit character(0123456789)! Please try again with digit character. ")
                        break
                else:
                     print("Your password has to have at least one uppercase character(ABCD...)! Please try again with uppercase character. ") 
                     break          
            else:
                print("Your password has to have at least one lowercase character(abcd...)! Please try again with lowercase character. ")
                break
                
                
        create_again = input("Do you want to create a new password again?(yes/no): ").strip()
        if create_again != "yes":
            break
        print(f"\nUser's pervious created passwords: {passwords} ")    
        

if __name__ == "__main__":
    main()