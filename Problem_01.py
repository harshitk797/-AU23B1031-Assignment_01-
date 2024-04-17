def get_name():
    name=input("Enter your name : ")
    return name

def get_tshirt(brand_name):
    user_name = get_name()
    
    Brands=[]
    for i in range(int(input("Total no of brand Avalable :"))):
        Brands.append(input(f"Enter brand name {i}: "))
        i=i+1
    print("Available brands:", Brands)
    n=input("Brand name you are Looking for : ")
    if n in Brands:
        print(f"Hi {user_name}, the brand you are looking for is available in our store.")
    else:
        print(f"Hi {user_name}, Unfortunately the brand you are looking for is not available in our store.")
            
brand_name = "Brands"
get_tshirt(brand_name)