def future_gain():#define the future gain with the help of function
    n= (ASP*ICR//CCR - ASP) * ((1+i) ** EPL- 1) // i - IMC * ((1+i)**EPL)
    return n
def total_gain():#define the total gain with the help of function
    a=n/(1+i)**EPL
    return a
def Annual_gain():#define the annual gain with the help of function
    b=a/EPL
    return(b)
def Annual_ROI():#define the annual ROI with the help of function
    c=b/IMC
    return c
def Total_ROI():#define the total ROI with the help of function
    t=a/IMC
    return t
# ASKING USER TO INPUT ALL VALUES WHICH ARE REQUIRED TO FINDING TOTAL ROI
ASP=int(input("Enter Annual Site Profit : "))
ICR=int(input("Enter Improved Conversion Rate: "))
CCR=int(input("Enter Current Conversion Rate : "))
EPL=int(input("Enter Expected Project Life : "))
IMC=int(input("Enter Improvement Cost : "))
i=float(input("Enter interest rate : "))
n= (ASP*ICR//CCR - ASP) * ((1+i) ** EPL- 1) // i - IMC * ((1+i)**EPL)# Formula for future gain
a=n/(1+i)**EPL# Formula for Total_gain 
b=a/EPL # Formula for Annual_gain
c = int(float(b)) / IMC # Formula for Annual_ROI
d = int(float(a)) / IMC # Formula for Total_ROI
print("Future Gain from Improvement = ",int(float(n)))
print("Total Gain from Improvement = ",int(float(a)))
print("Annual Gain from Improvement = ",int(float(b)))
print("Annual ROI = ",int(float(b)), ":", IMC,"=",c) # Convert float into integers
print("Total ROI = ",int(float(a)), ":", IMC,"=",d) # Convert Float into integers