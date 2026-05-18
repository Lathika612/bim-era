speed = int(input("speed:"))
data = int(input("data:"))
days = int(input("days:"))
if(speed>100 and data>500 and days>20):
    print("primium plan")
elif(speed>100 and days>20):
    print("standard plan")
else:
    print("base plan")