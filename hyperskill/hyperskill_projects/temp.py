# dict_friends = dict()
# user_input = int(input("Enter the number of friends joining (including you): "))
# if user_input <= 0:
#     print("No one is joining for the party")
# else:
#     print(f"{user_input} people are joining the party!")
#     for i in range(user_input):
#         friend_name = input("Enter friend's name: ")
#         dict_friends[friend_name] = 0 # Add the friend's name to the list
#     print(dict_friends)

# the function is fine, you do not need to change it
def square_odds(a, b):
    start = a
    if a % 2 == 0:
        start += 1
    end = b + 1
    for odd in range(start, end, 2):
        print(odd ** 2)


# from 22 to 42
square_odds(22, 42)

# from 15 to 31
square_odds(b=15, a=31)

# from 42 to 49
square_odds(49, 42)