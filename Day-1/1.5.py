temp = int(input("enter temp value:"))
lower_limit = int(input("enter lower value:"))
upper_limit = int(input("enter upper value:"))
if(temp>lower_limit & temp<upper_limit):
    print("temperature within safe ranges")
else:
    print("temperature is not safe ranges")