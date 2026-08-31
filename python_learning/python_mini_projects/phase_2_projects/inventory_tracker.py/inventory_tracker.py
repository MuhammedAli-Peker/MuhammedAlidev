
#envanter listesi:
inventory = []

#kullanici isimini almak:
def get_username():
    while True:
        name = input("\nPlease, enter your username here(max 16 character.): ").strip().capitalize()
        if 0 < len(name) <= 16:
            print(f"--> Welcome {name}")
            return name
        else:
            print("your username have to be greater than 0 ,and less or equal to 16!")
            

#listeyi görüntüleme
def check_list(inventory):
    print("\n---Inventory List---")
    
    if not inventory:
        print("Your inventory is empty.")
        return
    
    for index, item in enumerate(inventory, 1):
        print(f"\n{index}. {item['name']}")
        print(f"   Category : {item['category']}")
        print(f"   Situation: {item['situation']}")
        print(f"   Place    : {item['place']}")
        print(f"   Price    : {item['price']}")
#eşya görüntüleme > eşya bilgisi güncelleme(yes/no)
def check_item(inventory):
    while True:
        check_list(inventory)
        try:
            item_index = input("Enter the number of the item that you want to show up: ").strip()
            real_item_index = int(item_index) - 1
            
            if 0 <= real_item_index < len(inventory):
                print(inventory[real_item_index])
                
            else:
                print("invalid number! You have to enter a number currently in the your inventory.")    
                
        except ValueError:
            print("Invalid data! You have to enter a number.")
            
        while True:    
            ask_update = input("do you want to update your items?(yes/no)").strip().lower()  
            if ask_update == "no":
              break
            elif ask_update == "yes":
              while True:
                  try:
                        update_index = input("Enter the number of the item that you want to update: ").strip()
                        real_update_index = int(update_index) - 1
                        if 0 <= real_update_index < len(inventory):
                            update_item(inventory,real_update_index)
                            break 
                        else:
                            print("Wrong number! You have to enter a number in the your inventory")
                  except ValueError:
                        print("Invalid data! You have to enter a number currently in your inventory.")
                                           
            else:
                print("Answer with yes or no!")    
        
        try_again = input("\nDo you want to look any of the item again?(yes/no): ").strip().lower()
        if try_again == "no":
            break
        
#eşya verileri güncelleme:
def update_item(inventory,index):
    
    result = inventory[index] #önemli burada result = inventory oluyor alias oluyorlar yani resultta yaptığım 
                            #değişiklik envaterde yansıyor envanteri parametre olarak girdiğim için
    while True:
        print("--------------------------")
        for key,value in result.items():
            print(f"{key}:{value}")
        
        ask_user_request = input("Enter what would you want to change from your item(name/category/place/price/situation): ").strip().lower()
        #name change condition
        if ask_user_request == "name":
            name_change = input("Enter the name change here: ").strip().lower()
            result["name"] = name_change
        #category change condition    
        if ask_user_request == "category":
            category_change = input("enter the category change here: ").strip().lower()
            result["category"] = category_change
        #place change condition    
        if ask_user_request == "place":
            place_change = input("Enter the place change here: ").strip().lower()
            result["place"] = place_change
        #price change condition
        if ask_user_request == "price":
            while True:
                    try:
                        price_change = input("Enter the price change here: ").strip()
                        result["price"] = float(price_change)
                    except ValueError:
                        print("invalid data you have to entera float number")
        #situation change condition:
        if ask_user_request == "situation":
            situation_change = input("enter the situation change here: ").strip().lower()
            result["situation"] = situation_change
        
        
        break


#listeye eşye ekleme:        
def add_items(inventory):
    while True:
        user_answer = input("Do you want to add a new item?(yes/no): ").strip().lower()
        if user_answer == "no":
            break
        
        check_list(inventory)
        print("\nPlease, enter the item details below that you want to add to your inventory.")
        

        item_name = input("Enter the item name here: ").strip().capitalize()
        item_category = input("Enter the item category here(clothes,weapon etc.): ").strip().capitalize()
        item_situation = input("Enter  current situation of the item. (broken/ missing / existing): ").strip().capitalize()
        item_place = input("Enter place of the item.(unkown/home/school/garden/in inventory etc.): ").strip()
        
        while True:
            try:
                item_price = float(input("Enter the price of the item here: "))
                break
            except ValueError:
                print("invalid data! You have to enter a number!")
                
        result = {
        "name": item_name,
        "category": item_category,
        "situation": item_situation,
        "place": item_place,
        "price": item_price
    }        
                
                    
        inventory.append(result)
        print("\n--- Item was successfully added to your inventory! ---")
        
#listeden eşya silme:
def delete_items(inventory):
    while True:
        user_answer = input("Do you want to delete a item in your inventory(yes/no): ").strip().lower()
        if user_answer == "no":
            break
        
     
        while True:
            check_list(inventory)     
            try:
                item_index = input("\nEnter the item number that you want to delete from your inventory: ").strip()
                real_item_index = int(item_index) - 1
                
                if 0 <= real_item_index < len(inventory):
                    print(f"{inventory[real_item_index]['name']} was successfully  deleted from your inventory!")
                    inventory.pop(real_item_index)
                    break
                else:
                    print("You have to enter a number of the item currently existing in your inventory!")
            except ValueError:
                print("Invalid data! You have to enter a number")
#exit:
def exit_button(name):
    print(f"\n---Thanks for trying inventory tracker {name}---")
#main:
def main():
    print("\n---Welcome to Inventory Tracker ---")
    print("--->You can check your items with that application")
    inventory = []
    user_name = get_username()
    while True:
        print("----------------")
        choices = ["1-Check list","2-Add items","3-Delete items","4-Check items","5-Exit from the program"]
        for choice in choices:
            print(choice)

        while True:
            try:
                user_process = input("\n-->Enter the number of the process that you want to do: ")
                real_user_process = int(user_process) - 1
                if 0 <= real_user_process < len(choices) :
                    break
                else:
                    print("The number is not existing in the list. Try Again!")   
            except ValueError:
                print("You have to enter a number in the process list!")

        if real_user_process == 0:
            check_list(inventory)
        if real_user_process == 1:
            add_items(inventory)
        if real_user_process == 2:
            delete_items(inventory)
        if real_user_process == 3:
            check_item(inventory)
        if real_user_process == 4:
            exit_button(user_name)
            break



if __name__ == "__main__":
    main()