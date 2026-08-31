#Adding functions to electricity bill
subscribers=["Ali", "Ahmet","Mehmet"]
subscriber_name=input('Please enter your name here: ').strip().capitalize()
def checking_subscriber(subscriber_name):
    
    if subscriber_name in subscribers:
        electricity_usage=float(input("Please enter your electricity usage here "))
        def bill_calculator(kwh):
            if 0<electricity_usage<=250:
                bill=electricity_usage*kwh
                round(bill,1)
                return bill
            elif electricity_usage>250:
                bill=electricity_usage*kwh
                round(bill,1)
                return bill
            else:
                False
        def taxe_calculater(taxe_percantage,bill):
            total_taxe=bill*(taxe_percantage/100)
            round(total_taxe)
            return total_taxe
        print("Your total bill is: ",bill_calculator(1.28))
        print("Your total taxe is: ",taxe_calculater(20,bill_calculator(1.28)))
    else:
        return "İnvlaid electricity usage!"
    return "Process is successed"


x=checking_subscriber(subscriber_name)
print(x)

