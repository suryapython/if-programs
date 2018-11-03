no1 = int(input("1st no:"))
no2 = int(input("2nd no:"))
bol=bool(input("Enter bool:"))

def number(bol,no1,no2):

    if no1 < 0 or no2 < 0:
        if bol == False:
            return True

    else:
        if no1 < 0 and no2 < 0:
            if bol==True:
                return False

print(number(bol,no1,no2))





