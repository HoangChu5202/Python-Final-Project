sec = int(input("Give me a number of second: "))
SECONDINMINITUE = 60
SECONDINHOUR = 3600
SECONDINDAY = 86400
if sec < 60:
    print("It's " + str(sec) + " second.")
elif sec < 3600:
    minitue = sec // SECONDINMINITUE
    sec = sec % SECONDINMINITUE
    print("It's " + str(minitue) + " minute and " + str(sec) + " second.")
elif sec < 86400:
    hour = sec // SECONDINHOUR
    sec = sec % SECONDINHOUR
    minitue = sec // SECONDINMINITUE
    sec = sec % SECONDINMINITUE
    print("It's " + str(hour) + " hour " + str(minitue) + " minute and " + str(sec) + " second.")
else:
    day = sec // SECONDINDAY
    sec = sec % SECONDINDAY
    hour = sec // SECONDINHOUR
    sec = sec % SECONDINHOUR
    minitue = sec // SECONDINMINITUE
    sec = sec % SECONDINMINITUE
    print("It's " + str(day) + " day " + str(hour) + " hour " + str(minitue) + " minute and " + str(sec) + " second.")
