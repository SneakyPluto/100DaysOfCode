def is_leap_year(year):
    leap_year = False
    # Write your code here. 
    # Don't change the function name.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
        else:
            leap_year = True
    else:
        return leap_year
    return leap_year