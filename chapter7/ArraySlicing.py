# list_name[start : end: step]


days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

weekdays = days[1:6]
print(weekdays) # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

daysToStudy = days[:5]
print(daysToStudy) # ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']

weekend = days[6:] + days[0:1]
print(weekend) # ['Saturday', 'Sunday']

threeDayWeekend = days[5:] + days[0:1]
print(threeDayWeekend) # ['Friday', 'Saturday', 'Sunday']

fourDayWeekend = days[5:] + days[0:2]
print(fourDayWeekend) # ['Friday', 'Saturday', 'Sunday', 'Monday']

allDays = days[:]
print(allDays) # ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

mwf = days[1: 6: 2]
print(mwf) # ['Monday', 'Wednesday', 'Friday']

afterWednesday = days[-3:] #Negative number start from right and go back
print(afterWednesday) # ['Thursday', 'Friday', 'Saturday']