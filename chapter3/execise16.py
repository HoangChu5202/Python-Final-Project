year = int(input("Enter the year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print("In " + str(year) + " February has 29 days")
    else:
        print("In " + str(year) + " February has 28 days")
else:
    if year % 4 == 0:
        print("In " + str(year) + " February has 29 days")
    else:
        print("In " + str(year) + " February has 28 days")
