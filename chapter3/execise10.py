print("*** Exercise 10. Money Counting Game ***")
'''
- Authors: <Hoang>, <Jacob>
- Task: Enter the number of coins required to make exactly one dollar.
- Inputs: (1) Name: num_pennies, Type: int, Expected values: between 0 and 100, 
        (2) Name: num_nickels, Type: int, Expected values: between 0 and 100, 
        (3) Name: num_dimes, Type: int, Expected values: between 0 and 100, 
        (4) num_quarters, Type: int, Expected values: between 0 and 100.
- Processes: (1) value_pennies = num_pennies * 1, 
        (2) value_nickels = num_nickels * 5, 
        (3) value_dimes = num_dimes * 10, (4) value_quarters = num_quarters * 25, 
        (5) total_value = value_pennies + value_nickels + value_dimes + value_quarters
- Outputs: if total_value == 100 (1) Type: str, Expected value: "Congratulations for winning the game"; otherwise if total_value > 100 (2) Type: str, Expected value: "Your amount entered was XX cents more than one dollar."; otherwise if total_value < 100 (3) Type: str, Expected value: Your amount entered was XX cents less than one dollar.
'''
# Type your code here
num_pennies = int(input("Enter number pennies: "))
num_nickeks = int(input("Enter number nickels: "))
num_dimes = int(input("Enter number dimes: "))
num_quarters = int(input("Enter number quarters: "))

value_pennies = num_pennies * 1
value_nickels = num_nickeks * 5
value_dimes = num_dimes * 10
value_quarters = num_quarters * 25
total_value = value_pennies + value_nickels + value_dimes + value_quarters

if total_value == 100:
    print("Congratulations for winning the game!!!!")
elif total_value > 100:
    print("You are over 100")
else:
    print("You are under 100")
