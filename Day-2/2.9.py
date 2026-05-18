rooms = int(input("enter rooms:"))
days = int(input("enter days:"))
bugets = int(input("enter buget:"))
if(rooms>2 and days>3 and bugets>50000):
    print("luxury booking")
elif(rooms>2  and bugets>50000):
    print("standad booking")
else:
    print("budget booking")