while True:
    try:
        years = int(input("How many year do you want to calculate? "))
    except ValueError:
        print("Number only")
        continue
    if years >= 0:
        break

month = 0
total = 0
count = 1
while count <= years:
    for i in range(1,13):
        rainfall = float(input("How much rainfall for month", i, "? "))
        month += 1
        total += rainfall
    count += 1
print("Total month:", month)
print("Total inches of rain:", total)
print("Average rainfall per month:", format(total/month), ".2f")