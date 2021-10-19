print("*** Exercise 4. Distance Traveled ***")
'''
- Authors: Hoang, Stephen
- Task: Display the distance a vehicle has traveled for each hour of a time period.
- Inputs: (1) Name: speed, Type: int, Expected values: between 0 and 100, 
        (2) Name: hours_traveled, Type: int, 
            Expected values: between 0 and 100, 
            Note: hours_traveled will be used to control the loop.
- Processes: (1) distance_traveled = speed * loop_count
- Outputs: (1) Name: hour_count, Type: int, Expected values: between 1 and hours_traveled, 
            (2) Name: distance_traveled, Type: int, 
                Expected values: between speed and speed * hours_traveled.
'''

while True:
    try:
        speed = int(input("How many mph you traveling? ")) 
    except ValueError:
        print("Number only")
        continue
    if 0 < speed < 100:
        break
    else:
        print("Please input number between 0 and 100")
while True:
    try:
        hour = int(input("How many hour did you travel? "))
    except ValueError:
        print("Number only")
        continue
    if 0 < hour < 100:
        break
    else:
        print("Please input number between 0 and 100")
print("Hour \t Distance Traveled")
for i in range(hour):
    print(format(i+1, "3,.0f") + "\t\t" + format((i+1)*speed, "6,.0f")) 