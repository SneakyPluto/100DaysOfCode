def life_in_weeks(age):
    #Do calculation
    weeks_in_life = 4680
    weeks_in_year = 52
    weeks_left = weeks_in_life - (age * weeks_in_year)
    #print calculation
    print(f"You have {weeks_left} weeks left.")


# Call your function with hard coded values
life_in_weeks(56)