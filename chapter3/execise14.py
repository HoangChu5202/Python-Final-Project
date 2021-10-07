weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

bmi = weight * (703 / height ** 2)

print("Your BMI is: ", format(bmi, ".1f"))
if bmi < 18.5:
    print("You are underweight.")
elif bmi <= 25:
    print("You are optimal.")
else:
    print("You are overweight.")