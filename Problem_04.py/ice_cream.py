def add_topping(scoop_size, *toppings):
    print("Adding toppings to", scoop_size ,"scoop ice cream:")
    for i in toppings:
        print("topping")

def make_shake(choice):
    if choice == "nuts":
        print("Making a nut shake")
    elif choice == "fruit":
        print("Making a fruit shake")