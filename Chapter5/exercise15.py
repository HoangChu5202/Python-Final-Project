from math import e
import helper

MIN_GRADE_A = 90
MIN_GRADE_B = 80
MIN_GRADE_C = 70
MIN_GRADE_D = 60

def calc_average(totalScore): 
    average = totalScore / 5
    return average

def determine_grade(score):
    if score >= MIN_GRADE_A:
        grade = "A"    
    elif score >= MIN_GRADE_B:
        grade = "B"
    elif score >= MIN_GRADE_C:
        grade = "C"
    elif score >= MIN_GRADE_D:
        grade = "D"
    else:
        grade = "F"
    return grade

def main():
    totalScore = 0
    for i in range(5):
        totalScore += helper.getNum("Enter your score of test", 0, 100)
    avgScore =  calc_average(totalScore)
    avgGrade = determine_grade(avgScore)
    print("Your average score:", format(avgScore, ".2f"))
    print("Your final Grade is: ", avgGrade)

main()