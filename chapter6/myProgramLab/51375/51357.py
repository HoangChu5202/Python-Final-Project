maxvalue = -1
with open("./chapter6/myProgramLab/51375/numbers.txt", "r") as file:
    for line in file:
        n = int(line.strip())
        if (n > maxvalue):
            maxvalue = n
    print(maxvalue)
