import random
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
# def square_odds(a, b):
#     start = a
#     if a % 2 == 0:
#         start += 1
#     end = b + 1
#     for odd in range(start, end, 2):
#         print(odd ** 2)


# # from 22 to 42
# square_odds(22, 42)

# # from 15 to 31
# square_odds(b=15, a=31)

# # from 42 to 49
# square_odds(49, 42)
some_dict = {"travis" : "Levine", "John" : "Osborne", "Seth" : "Wells", "Kestrel" : "Wrestle"}
def lucky(new_dict):
    return random.choice(list(new_dict.values()))

def who_is_lucky():
    print("""Do you want to use the "Who is lucky?" feature? Write Yes/No: """)
    lucky_input = input()
    if lucky_input.lower() == "yes":
        #do some code
        name_value = lucky(some_dict)
        print(f"{name_value} is the lucky one!")
    else:
        print("No one is going to be lucky") 

