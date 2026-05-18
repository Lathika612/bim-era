speed = int(input("enter speed:"))
fitness = int(input("enter fitness:"))
discipline = int(input("enter discipline:"))
if(speed>80 and fitness>80 and discipline>80):
    print("selected")
elif(speed>80 and discipline>80):
    print("waiting list")
else:
    print("rejected")