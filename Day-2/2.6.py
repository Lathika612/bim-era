ticket = input("enter ticket:")
passport = input("enter passport:")
luggage = int(input("enter luggage:"))
if(ticket=="yes" and passport=="yes" and luggage<30):
    print("boarding allowed")
else:
    print("boarding denied")