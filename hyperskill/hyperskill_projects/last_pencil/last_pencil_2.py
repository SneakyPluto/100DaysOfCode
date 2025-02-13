#Module imports
import random

#Player namers
name_1 = "John"
name_2 = "Travis"

#Basic input handling
def get_num():
    try:
        return int(input("How many pencils would you like to use: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def get_string():
    try:
        return str(input())
    except ValueError:
        print("Invalid input. Please enter a valid number.")

num_pencils = get_num()

print(f"Who will be the first ({name_1}, {name_2}): ")
who_first = get_string()

print(f"{who_first} is going first!")

print("|" * num_pencils)