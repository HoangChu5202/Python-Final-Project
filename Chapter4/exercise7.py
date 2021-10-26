day_working = int(input("How many day did you work? "))
day = 1
pennies = 0
total = 0
print("Day \t\t Today Earned")
print("__________________________________")
print()
while day <= day_working:
    earn = 1
    for i in range(1,day):
        earn *= 2
    pennies += earn 
    dollar = pennies / 100
    total += dollar
    print(day, "\t\t $" + format(earn/100, ",.2f"))
    day += 1
print("Total amout you earned: $" + format(total, ",.2f"))
