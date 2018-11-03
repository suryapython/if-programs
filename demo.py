bol=bool(input("bool:"))
hour=float(input("value:"))
def parrot(bol,hour):
    if hour <= 7 or hour >= 20:

        if bol==False:
            return False
        else:
            return True

    else:
        return False
print(parrot(bol,hour))


