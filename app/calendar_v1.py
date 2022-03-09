# from sys import argv
# script, day, month, year = argv

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


# funcion validate the data

def get_int_from_user(prompt: str, int_range: tuple[int, int]) -> int:
    while True:
        try:
            user_data = int(input(prompt))
        except ValueError:
            print("Please type in a number!")
            continue
        try:
            if user_data in range(*int_range):
                return user_data
            else:
                print(f"Please enter a number from {int_range[0]} and below {int_range[1]}")
        except Exception as e:
            print(e)
            if debug:
                break


year = get_int_from_user("Enter the year: ", (1, 10000))
month = get_int_from_user("Enter the month: ", (1, 13))
day = get_int_from_user("Enter the day: ", (1, days_in_month(month, year) + 1))


def main():
    print(f"Is {year} a leap year?", leap_year(year))
    print(f"The {month} month of {year} year has", days_in_month(month, year), "days")
    print(f"The {day} day of {month} month of {year} year is", day_of_the_year(day, month, year), "day of the year")


if __name__ == "__main__":
    main()

