#get input from the user
def get_name():
    name=input("Enter your name : ")
    return name

#get tshirt brand name
def get_tshirt(brand_name, size=0):
    user_name = get_name()
    
    Brands=[]#empty brand list
    for i in range(int(input("Total no of brand Available :"))):#loop for entering brand name of tshirt
        Brands.append(input(f"Enter brand name {i}: "))
        i=i+1
    print("Available brands:", Brands)
    n=input("Brand name you are Looking for : ")#input for searching the brand
    if n in Brands:
        new=f"Hi {user_name}, the brand you are looking for is available in our store "
        if size:
            size=input("Enter your tshirt size : ")
            new+=f"and Size {size} is also available."
        print(new)
    else:
        print(f"Hi {user_name}, Unfortunately the brand you are looking for is not available in our store.")
#object declaration
brand_name = "Brands"
size = "size"
get_tshirt(brand_name,size)