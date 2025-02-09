def human_years_cat_years_dog_years(human_years):
    # Your code here
    ages = [] #  [humanYears,catYears,dogYears]
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    elif human_years == 2:
        cat_years = 24
        dog_years = 24
    else:
        cat_years = 24 + (human_years - 2) * 4 
        dog_years = 24 + (human_years - 2) * 5 
    return [human_years, cat_years, dog_years]

print(human_years_cat_years_dog_years(10))

#You have passed all of the tests! :)