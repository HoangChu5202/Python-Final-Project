with open("./chapter6/myProgramLab/data1.txt", "r") as file1:
    with open("chapter6/myProgramLab/data2.txt", "r") as file2:
        scalar_product = 0
        while True:
            input1 = file1.readline().strip()
            input2 = file2.readline().strip()
            if input1 == "" or input2 == "":
                break
            else:
                input1 = int(input1)
                input2 = int(input2)
            scalar_product += input1 * input2
print(scalar_product)