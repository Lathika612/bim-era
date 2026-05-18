p = 612
pin = int(input("enter pin:"))
face = input("enter face:")
finger = input("enter finger:")
if(p==pin and face=="yes" and finger=="yes"):
    print("mobile unloked")
else:
    print("mobile locked")