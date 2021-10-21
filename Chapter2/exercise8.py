print("*** Exercise 8. Tip, Tax, and Total***")
'''
- Authors: Hoang, Eric
- Task: Write a program that calculates the total amount of a meal purchased at a restaurant.
- Inputs: 
  (1) Name: food_charge, Type: float, 
    Expected values: between 0 and 1000000
- Processes: 
  (1) tip = food_charge * 0.18, 
  (2) sales_tax = food_charge * 0.07, 
  (3) total_charge = food_charge + tip + sales_tax
- Outputs: 
  (1) Name: tip, Type: float, 
      Format: displayed with 2 decimals, 
      Expected values: between 0.00 and 180000.00, 
  (2) Name: sales_tax, Type: float, 
      Format: displayed with 2 decimals, 
      Expected values: between 0.0 and 70000.0, 
  (3) Name: total_charge, Type: float, 
      Format: displayed with 2 decimals, 
      Expected values: between 0.0 and 1250000.0 
'''
# Type your code here
def main():
  food_charge = float(input("Enter cost food: "))
  calTotal(food_charge)

def calTotal(food_charge):
  tip = food_charge * 0.18
  sales_tax = food_charge * 0.07
  total_charge = sales_tax + tip + food_charge
  print("Food Charge:\t", format(food_charge, "10,.2f"))
  print("Tip:\t\t", format(tip, "10,.2f"))
  print("Tax:\t\t", format(sales_tax, "10,.2f"))
  print("Total:\t\t", format(total_charge, "10,.2f"))

main()
