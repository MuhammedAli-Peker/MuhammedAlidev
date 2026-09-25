
information_notebook = []

#kullanici adi alma:
def get_username():
    while True:
        user_name = input("Please enter your username here: ").strip().capitalize()
        if 0 < user_name <= 16:
            print(f"--> Welcome {user_name} <--")
            return user_name
        else:
            print("your username has to be greater than 0 and lower or equal to 16!")

#adress listesi görüntüleme
def get_information_list(notebook):
    print("\n---Information Notebook---")

    if not notebook:
        print("Your notebook is empty")
        return
    
    for index , info in enumerate(notebook,1):
        print(f"\n{index}. {info["name"]}")
        print(f"-->     Phone Number: {info["phone"]}")
        print(f"-->     Address: {info["address"]}")
        print(f"-->     Email: -{info["email"]}")

   
#adress bilgisi ekleme:
def add_information(notebook):
    while True:
        
        person_name = input("Please enter the person'S name  here: ").strip().title()
        
        while True:
            try:
                person_phone = input("Enter the person'S phone number here: ").strip()
                if len(person_phone) == 8:
                    break
                else:
                    print("phone number Must be 8 digits long!")
                
            except ValueError:
                print("Invalid data. You have to enter numbers not letters!")
                
        person_address = input("Enter the person's adress here(street etc.): ").strip().capitalize()
        
        while True:
            ask_choice = input("Do you want to add the person's email?(yes/no): ").strip().lower()
            if ask_choice == "no":
                person_email == ""
                break
            
            while True:
                person_email = input("Enter the person's email here: ").strip().lower()
                
            