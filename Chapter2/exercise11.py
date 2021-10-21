print("*** Male and Female Percentages ***")
def main():
    male = int(input("Number of Male in class: "))
    female = int(input("Number of Female in class: "))
    calculate(male, female)

def calculate(male, female):
    total = male + female
    malePercent = male / total 
    femalePercent = female / total 
    print("Male: " + format(malePercent, ".2%"))
    print("Female: " + format(femalePercent, ".2%"))

main()