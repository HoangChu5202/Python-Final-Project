from helper import getNum

def getRainfallData():
    result = []
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    for month in months:
        question = "Enter " + month + "'s rainfall total"
        result.append(getNum(question, 0, 100))
    return result

def getSum(rainfall):
    sum = 0
    for el in rainfall:
        sum += el
    return sum

def getAverage(sum, count):
    return sum / count

def main():
    rainfall = getRainfallData()
    total = getSum(rainfall)
    average = getAverage(total, len(rainfall))
    print("Total rain fall:", format(total, ".2f"))
    print("Average monthly rain fall:", format(average, ".2f"))
    print("Highest monthly rainfall:", format(max(rainfall), ".2f"))
    print("Lowest monthly rainfall:", format(min(rainfall), ".2f"))
  
main()