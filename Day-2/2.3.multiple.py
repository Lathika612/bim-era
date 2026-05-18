u1 = "lathika"
p1 = "la123@"
otp1 = "2525"
u2 = "pydi"
p2 = "1234"
otp2 = "2130"
user1 = input("enter user:")
pwd1 = input("enter pwd:")
otp1 = input("enter otp:")
user2 = input("enter user:")
pwd2 = input("enter pwd:")
otp2 = input("enter otp:")
if((u1==user1 and p1==pwd1 and otp1==otp1) or (u2==user2 and p2==pwd2 and otp2==otp2)):
    print("login succesfull")
else:
    print("not successfull")