def getInput():
    price_per_package = float(input("What is the price per package? "))
    packages_purchased = int(input("How many packages are you purchasing? "))
    return price_per_package, packages_purchased

def calc_amount(price_per_package, packages_purchased):
    if packages_purchased > 100:
        discount = .4
    elif packages_purchased > 50:
        discount = .3
    elif packages_purchased > 20:
        discount = .2
    elif packages_purchased > 10:
        discount = .1
    else:
        discount = 0
    purchase_amount = price_per_package * packages_purchased
    discount_amount = purchase_amount * discount
    total_amount = purchase_amount - discount_amount
    return purchase_amount, discount_amount, total_amount

def print_result(purchase_amount, discount_amount, total_amount):
    print(f"The initial cost is $" + format(purchase_amount, ",.2f"))
    print(f"The discount is $" + format(discount_amount, ",.2f"))
    print(f"The final cost is $" + format(total_amount, ",.2f"))

def main():
    price_per_package, packages_purchased = getInput()
    purchase_amount, discount_amount, total_amount = calc_amount(price_per_package, packages_purchased)
    print_result(purchase_amount, discount_amount, total_amount)

main()