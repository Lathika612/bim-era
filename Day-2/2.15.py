amount = int(input("enter amount:"))
coupon = (input("coupon status:"))
premium = (input("premium status:"))
if( amount>10000 and coupon == "yes" and premium == "yes"):
    print("maximum discount")
elif(amount>10000 and coupon == "yes"):
    print("medium discount")
else:
    print("no discount")