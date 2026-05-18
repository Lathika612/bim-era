days = int(input("enter days:"))
percentage = int(input("enter percentage:"))
if(days==0 and percentage>80):
    print("project meets the deadline")
else:
    print("project not meets the deadline")