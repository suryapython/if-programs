name=input("name:")
salary=float(input("sal:"))
disgnation=input("disgnation is eaither manager/analyst/clerk:")
if disgnation == "manager":
    bonous = salary*20/100
    print("sal=",salary+bonous)

if disgnation == "analyst":
    bonous = salary*10/100
    print("sal=",salary+bonous)

if disgnation == "clerk":
    bonous = salary*5/100
    print("sal=",salary+bonous)