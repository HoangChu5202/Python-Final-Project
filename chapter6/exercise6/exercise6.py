total = 0
count = 0
with open("./chapter6/exercise6/numbers.txt", "r") as file:
    for num in file:
        number = int(num.strip())
        total += number
        count += 1
print("Average:", format(total/count, ".2f"))