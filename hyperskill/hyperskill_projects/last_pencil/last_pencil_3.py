#Module imports
import random

#Player namers
name_1 = "John"
name_2 = "Travis"

#Basic input handling
def get_num():
    try:
        return int(input())
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def get_string():
    try:
        return str(input())
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print("How many pencils would you like to use:")
num_pencils = get_num()

print(f"Who will be the first ({name_1}, {name_2}): ")
who_first = get_string()

# Update the players list dynamically based on who goes first
if who_first == name_1:
    players = [name_1, name_2]
elif who_first == name_2:
    players = [name_2, name_1]
else:
    # In case of invalid input, default to John as the first player
    print("Invalid input. Defaulting to John as the first player.")
    players = [name_1, name_2]

# print(f"{who_first}'s turn: ")
print("|" * num_pencils)


#Turn requirements
players = [name_1, name_2]
turn = 0

while num_pencils > 0:
    # Who's turn
    print(f"{players[turn]}'s turn:")

    #Game functionality (substracting pencils)
    subtract_amount = get_num()

    #Update the number of pencils
    num_pencils -= subtract_amount
    print("|" * num_pencils)

    # Switch to the next player.
    turn = (turn + 1) % 2

