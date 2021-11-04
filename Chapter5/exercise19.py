import helper

def calc_Money(curMoney, interestRate, month):
    future = curMoney * (1 + interestRate) ** month
    return future

def getInput():
    currentMoney = helper.getNum("How much you have in account now?", 0)
    interestRate = helper.getNum("What is monthly interest?", 0)
    month = helper.getNum("How long you want to keep saving money?[In month]",0)
    return currentMoney, interestRate, month

def main():
    curMoney, interestRate, month = getInput()
    accFuture = calc_Money(curMoney, interestRate, month)
    print("After", int(month), "month you will have: $" + format(accFuture, ",.2f"))

main()