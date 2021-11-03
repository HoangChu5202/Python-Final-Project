import helper
STATETAX = 0.05
COUNTYTAX = 0.025

def getInput():
    totalSales = helper.getNum("What is total sales for month?", 0)
    return totalSales

def saleTax(totalSales):
    state_salesTax = totalSales * STATETAX
    county_salesTax = totalSales * COUNTYTAX
    return state_salesTax, county_salesTax

def printResult(county_salesTax, state_salesTax):
    print("County sales Tax:\t$" + format(county_salesTax, ",.2f"))
    print("State sales Tax:\t$" + format(state_salesTax, ",.2f"))
    print("Total sale Tax:\t\t$" + format(state_salesTax + county_salesTax, ",.2f"))

def main():
    sale = getInput()
    state, county = saleTax(sale)
    printResult(county, state)

main()
