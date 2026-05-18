t = int(input("enter temperature:"))
upper_limit = int(input("enter upper limit:"))
lower_limit = int(input("enter lower limit:"))
if(t > upper_limit or t <lower_limit):
    print("extreme temperature")
else:
    print("normal")