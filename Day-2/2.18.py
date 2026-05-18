buget = int(input("enter buget:"))
ram = int(input("enter ram:"))
storage = int(input("enter storage:"))
if(buget>100000 and ram>=16 and storage>=512):
    print("gaming laptop")
elif(buget>100000 and storage>=512):
    print("office laptop")
else:
    print("basic laptop")