temp = int(input("enter temp:"))
wind = int(input("wind status:"))
rain = input("rain status:")
if(temp>40 and wind >  50 and rain=="no"):
    print("heat alert")
elif(temp>40 and rain=="no"):
    print("stome alert")
else:
    print("normal whether")