maxvalue = -1
runsum = 0
with open("./chapter6/myProgramLab/51360/numbers.txt", "r") as file:
    for line in file:
        num = int(line.strip())
        if (num > maxvalue):
            maxvalue = num
            runsum += maxvalue
        
print(runsum)