total = 0
count = 0
try: 
    with open("./chapter6/exercise9/numbers.txt", "r") as file:
        for num in file:
            try:
                number = int(num.strip())
            except ValueError:
                print("ERORR: Can not convert string to number!!!")
                total = 0
                count = 0
                break
            total += number
            count += 1
except IOError:
    print("ERORR: File not found!!!")

if (total != 0) and (count != 0):
    print("Average:", format(total/count, ".2f"))