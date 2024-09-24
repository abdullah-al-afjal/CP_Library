import calendar

year = int(input("Enter the year: "))
print(calendar.calendar(year))

month = int(input("Enter the month (1-12): "))

if 1 <= month <= 12:
    print(calendar.month(year, month))
else:
    print("Invalid Month")