import helper 
import math

SQ_FT_PER_GALLON = 112
HRS_LABOR_PER_GALLON = 8
CHARGE_PER_HOUR = 35

square_feet = helper.getNum("Enter the square feet of wall space to be painted: ", 0)
price_per_gallon = helper.getNum("Enter the price per paint gallon", 0)

def calc_gallons_of_paint(square_feet):
  gallons_of_paint = square_feet / SQ_FT_PER_GALLON
  return gallons_of_paint

def calc_hours_of_labor(gallons_of_paint):
  hours_of_labor = gallons_of_paint * HRS_LABOR_PER_GALLON
  return hours_of_labor

def calc_labor_charges(hours_of_labor):
  labor_charges = hours_of_labor * CHARGE_PER_HOUR
  return labor_charges

def calc_cost_of_paint(gallons_of_paint, price_per_gallon):
  cost_of_paint = gallons_of_paint * price_per_gallon
  return cost_of_paint

def calc_total_cost(cost_of_paint, labor_charges):
  total_cost = cost_of_paint + labor_charges
  return total_cost


gallons_of_paint = calc_gallons_of_paint(square_feet)
gallons_of_paint = math.ceil(gallons_of_paint)
hours_of_labor = calc_hours_of_labor(gallons_of_paint)
labor_charges = calc_labor_charges(hours_of_labor)
cost_of_paint= calc_cost_of_paint(gallons_of_paint, price_per_gallon)
total_cost = calc_total_cost(labor_charges, cost_of_paint)

print("Number of gallon required:", format(gallons_of_paint, ","))
print("Hours of labor required:", format(hours_of_labor, ","))
print("Cost of paint: $" + format(cost_of_paint, ",.2f"))
print("Labor charges: $" + format(labor_charges, ",.2f"))
print("Total cost: $" + format(total_cost, ",.2f"))