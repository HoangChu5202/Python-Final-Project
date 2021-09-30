print("*** Male and Female Percentages ***")

male = int(input("Number of Male in class: "))
female = int(input("Number of Female in class: "))

total = male + female
malePercent = male / total 
femalePercent = female / total 

print("Male: " + format(malePercent, ".0%"))
print("Female: " + format(femalePercent, ".0%"))