print("*** Male and Female Percentages ***")

male = int(input("Number of Male in class: "))
female = int(input("Number of Female in class: "))

total = male + female
malePercent = male / total * 100
femalePercent = female / total * 100

print("Male: " + format(malePercent, ".0f") + "%")
print("Female: " + format(femalePercent, ".0f") + "%")