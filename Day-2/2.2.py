maths = int(input("enter maths marks:"))
science = int(input("enter science marks:"))
english = int(input("enter english marks:"))
if(maths>75 and science>75 and english>=75):
    print("Distinction")
elif(maths>75 and science>35 and english>35):
    print("pass")
else:
    print("fail")