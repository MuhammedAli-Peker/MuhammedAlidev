def area_calculater(uzun_kenar,kisa_kenar):
    area=uzun_kenar*kisa_kenar
    
    if uzun_kenar==kisa_kenar:
        print('This is a square!')
    else:
        print('This is not a square!')
    return area
    


area_cal=area_calculater(20,5)
print(f"Are a of: {area_cal}")


def one_or_two(sayi):
    print("The first Number:",sayi)
    sayi=input("Please enter a number! ")
    number=int(sayi)
    if number%2==0:
        print('The number is double')
    else:
        print('The number is single')
one_or_two(100)