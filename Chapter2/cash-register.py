cost = int(float(input("What is the cost of the item? ")) * 100)
payment = int(float(input("How much cash dare you paying? ")) * 100)

QUARTER = 25
DIME = 10
NICKEL = 5
PENY = 1

change = payment - cost
change_quarter = change // QUARTER
change = change % QUARTER   
change_dime = change // DIME
change = change % DIME
change_nickel = change // NICKEL
change = change % NICKEL
change_peny = change // PENY

print(change_quarter, "Quarter", change_dime, "Dime", change_nickel, "Nickle", change_peny, "Peny")