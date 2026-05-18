age = int(input("enter age:"))
membership = input("membership status:")
day = input("day status:")
if(age>18 and membership=="yes" and day=="sunday"):
    print("50% discount")
elif((membership=="yes")):
    print("25% discount")
else:
    print("no discount")