def year_helper(day_calc, year):
    """A helper function for computing the year. It accounts for leap years."""
    while True:
        if year % 100 == 0: #Leap year check for century years
            leap_year = (year % 400 == 0) #400 exception
        else: #Else a leap year if divisible by 4
            leap_year = (year % 4 == 0)
        if leap_year:
            year_days = 366
        else:
            year_days = 365
        if day_calc >= year_days: #Checks if possible to subtract a year
            day_calc -= year_days
            year += 1 #Moves to the next year after subtracting it
        else: #Else returns the remaining days, the current year, and whether a leap year
            return day_calc, year, leap_year

def month_helper(day_calc, leap_year):
    """A helper function for computing the month. It accounts for leap year days in February."""
    month = 1 #January
    while True:
        if month == 2:
            if leap_year:
                month_days = 29
            else:
                month_days = 28
        elif month in (1, 3, 5, 7, 8, 10, 12):
            month_days = 31
        else:
            month_days = 30
        if day_calc >= month_days:
            day_calc -= month_days
            month += 1
        else:
            return day_calc, month

def my_datetime(num_sec):
    """A function that takes an integer value for the number of seconds since January 1st, 1970.
    It converts num_sec to a date and returns it in MM-DD-YYYY format."""
    day_calc = num_sec // 86400
    day_calc, year, leap_year = year_helper(day_calc, 1970)
    day_calc, month = month_helper(day_calc, leap_year)
    day = day_calc + 1
    return f"{month:02d}-{day:02d}-{year}"

#print(my_datetime(0))

#print(my_datetime(123456789))

#print(my_datetime(9876543210))

#print(my_datetime(201653971200))