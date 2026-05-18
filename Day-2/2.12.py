helmet = input("helmet status:")
license = input("license status:")
speed = int(input("speed status:"))
if(helmet=="yes" and license=="yes" and speed<80):
    print("no fine")
elif(helmet=="yes" and license=="yes" and speed>80):
    print("heavy fine")
else:
    print("noml fine")