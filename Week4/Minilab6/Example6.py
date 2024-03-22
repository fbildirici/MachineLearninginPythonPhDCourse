def find_next_20_leap_years(current_year):
    leap_years = []
    while len(leap_years) < 20:
        if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
            leap_years.append(current_year)
        current_year += 1
    return leap_years

# assume the this year current
current_year = 2024
next_20_leap_years = find_next_20_leap_years(current_year)
next_20_leap_years

print(next_20_leap_years)