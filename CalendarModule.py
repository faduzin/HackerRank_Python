import calendar

if __name__ == '__main__' :
    month, day, year = map(int, input().split())
    weekdays = list(calendar.day_name)
    weekday = calendar.weekday(year, month, day)
    print(weekdays[weekday].upper())

# What I learned:
# 1. How to use calendar library
# 2. How to print the weekday based on an int
# 3. How to create a list containing values of 
# a library