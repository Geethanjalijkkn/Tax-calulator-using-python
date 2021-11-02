# 24/10/21
#Geethajali
#tax calculator


#def Calculate_GST(org_cost, N_price):
     
    # return value after calculate GST%
 #   return (((N_price - org_cost) * 100) / org_cost);
 
#org_cost = input("enter the orginal  cost")
#N_price = input("enter the net cost")
#print("GST = ",end='')
 
#print(round(Calculate_GST(org_cost, N_price)),end='')
 
#print("%")


while True:
    income = float(input("Enter the annual income: "))

    tax = 0.0
    if income <= 85528:
        tax = income*0.18 - 556.02
        if tax<0:
            tax=0
    else:
        tax=(income-85528)*.32 + 14839.02
    tax = round(tax,0)
    print("The tax is:", tax)