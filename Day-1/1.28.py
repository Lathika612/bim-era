temp = int(input("enter temperature:"))
safe = temp>20 and temp<50
if not(safe):
    print("temperature is not saafe")
else:
    print("temperature is safe")