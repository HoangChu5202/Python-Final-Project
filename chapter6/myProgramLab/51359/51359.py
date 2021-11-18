with open("./chapter6/myProgramLab/51359/dataplus.txt", "w") as plus:
    pass
with open("./chapter6/myProgramLab/51359/dataminus.txt", "w") as minus:
    pass
with open("./chapter6/myProgramLab/51359/data.txt", "r") as file:
    for line in file:
        n = int(line.strip())
        if n > 0:
            with open("./chapter6/myProgramLab/51359/dataplus.txt", "a") as plus:
                plus.write(str(n) + "\n")
        elif n < 0:
            with open("./chapter6/myProgramLab/51359/dataminus.txt", "a") as minus:
                minus.write(str(n) + "\n")
       