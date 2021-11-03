from math import e
import helper

MIN_GRADE_A = 90
MIN_GRADE_B = 80
MIN_GRADE_C = 70
MIN_GRADE_D = 60

totalGrade = 0
testlScore = []

def calc_average(test1, test2, test3, test4, test5): #They want 5 test score as agruments
    totalScore = test1 + test2 + test3 + test4 + test5
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
    for i in range(1,6):
        testlScore[i] = helper.getNum(("Enter your score of test" , i , ": "), 0, 100)
    avgScore =  calc_average(testlScore[1], testlScore[2], testlScore[3], testlScore[4], testlScore[5])
    avgGrade = determine_grade(avgScore)
    print("Your average score:", format(avgScore, ".2f"))
    print("Your final Grade is: ", avgGrade)

main()