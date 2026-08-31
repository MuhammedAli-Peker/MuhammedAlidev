#listeler ve döngüler üzerine örnek bir proje

#müşteri ürürn listesi:
products = []
prices = []
#kataloglar:
catalogs = {
    "foods" : ["apple","banana","orange","cherry","watermelon","strawberry"],
    "toys" : ["dinosaur","knight","spiderman","puzzle","robot"],
    "electronics" : ["phone","computer","watch","mouse","keyboard"],
    "clothes" : ["shirt","sock","sweatshirt","pant","coat"]
}
#katalog seçme:
def get_catalog_choice():
    print("---Catalog List---")
    for no,catalog in enumerate(catalogs,1):
        print(f"Catalog: {no}-{catalog}")
    
    while True:
        catalog_choice = input("Please choice a catalog in catalog list! ").strip().lower()
        if catalog_choice in catalogs:
            print(f"Your catalog choice: {catalog_choice}")
            return catalog_choice
        else:
            print("Please enter a catalog in the catalog list")
#ürün ekleme:
def add_product(chosen_catalog):
    while True:
        print(f"-->{chosen_catalog}")
        user_product = input("Enter the product here that you chose in the catalog: ").strip().lower()
        if user_product in catalogs[chosen_catalog]:
            return user_product
        else:
            print("The product that you want to add wasn't included in the catalog!\nPlease enter the product in the catalog that you chose.")
            print(f"Your catalog: {chosen_catalog}")
#Liste görüntüleme:
def get_user_list(chosen_products):
    print("--- Your Chosen Products List ---")
    if not chosen_products:
        print("--> Your product list empty!")
    else:
        for product in chosen_products:
            print("->",product)

#Ürün silme:
def delete_product(chosen_products):
    if chosen_products != []:   
        while True:
            deleted_product = input("Enter the name of the product that you want to remove.\n")
            print(chosen_products)
            if deleted_product in chosen_products:
                chosen_products.remove(deleted_product)
                print(f"{deleted_product} was removed from your list.")
            else:
                print("Enter the product name that you want to remove! ")
    else:
        print("Your list was empty.There is nothing to remove")
            
            
        
        
#temel algritma kismi main() planlama
#1- kullanıcında 3 işlem'den birisi seçmesi istencek eğer ürün ekle seçilirse katalog seçilecek daha sonra o kataloğa ait
# ürün seçilip ekelencek ve kullanciya tekrar ürün eklemek isteyip istemedği sorulacak
#kullanıcı diğer ürün seçmeyi bırakırsa ana noktaya dönülecek ve tekara üç işlemden birini seçmesi istencek ve buy seçeneği eklenecek

#ana kısım:
def main():
    print("--- Welcome Sopping list creator demo ---")
    while True:
        user_process = input("Choose the action you want to perform(1,2,3)")
        
        
""" ŞİMDİLİK ARA DAHA SONRA YENİDEN YAPİLACAK BAŞTAN!"""