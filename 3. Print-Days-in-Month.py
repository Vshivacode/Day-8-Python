# Print Days in a month
def letter(word):
    if word == "":
        print("enter the values")
    return word.title()

def is_leap_year(year):
    if year %4 == 0:
        if year %100 == 0:
            if year %400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    if month == 2 and is_leap_year(year):
        return 29
    else:
        return month_days[month-1]
year = int(input("enter year: "))
month = int(input("enter month: "))
days = days_in_month(year, month)
print(f"{month} month has {days} days in year {year}")


# Output:
enter year: 2024
enter month: 2
2 month has 29 days in year 2024
