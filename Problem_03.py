lis=[]#empty list
for i in range(int(input("How many no. of product you want to order : "))):#loop for product counting and naming
    lis.append(input("Order name : "))
    i+=1
print("You have ordered : ",lis)

def get_order(orders):#define function for correct arrangement of preparing and dispatch items
        for ele in lis:
            print("Preparing Your Order - ",ele)
        if lis:
            lis.reverse()
        print("Dispatched items : ")
        while lis:#loop for pop or removing order 
            print(lis.pop())
        
orders="order"
get_order(orders)