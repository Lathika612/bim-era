id = input("enter id:")
finger = input("enter finger:")
access = int(input("enter access:"))
if(id=="yes" and finger=="yes" and access>5):
    print("access ganted")
else:
    print("access restricted")