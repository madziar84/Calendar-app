DAYS_IN_MONTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


# function calculating a leap year

def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


# function calculating the number of days in a month

def days_in_month(month, year):
    if month == 2 and leap_year(year):
        return 29
    else:
        return DAYS_IN_MONTHS[month - 1]


# function calculating the day of the year

def day_of_the_year(day, month, year):
    total = sum(DAYS_IN_MONTHS[:month - 1]) + day
    if month > 2 and leap_year(year):  # == True:
        total += 1
    return total


# validate the data

while True:
    try:
        year = int(input("Enter the year: "))
    except ValueError:
        print("Please type in a number!")
        continue
    if 0 < year < 10000:
        break
    else:
        print("Please enter a number above 0 and below 10000")

while True:
    try:
        month = int(input("Enter the month: "))
    except ValueError:
        print("Please type in a number!")
        continue
    if 0 < month < 13:
        break
    else:
        print("Please enter a number above 0 and below 13")

while True:
    try:
        day = int(input("Enter the day: "))
    except ValueError:
        print("Please type in a number!")
        continue
    if 0 < day < 32:
        break
    else:
        print("Please enter a number above 0 and below 32")

print(f"Is {year} a leap year?", leap_year(year))
print(f"The {month} month of {year} year has", days_in_month(month, year), "days")
print(f"The {day} day of {month} month of {year} year is", day_of_the_year(day, month, year), "day of the year")
