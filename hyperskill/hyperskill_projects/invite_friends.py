dict_friends = dict()
user_input = int(input("Enter the number of friends joining (including you): "))
if user_input <= 0:
    print("No one is joining for the party")
else:
    print(f"{user_input} people are joining the party!")
    for i in range(user_input):
        friend_name = input("Enter friend's name: ")
        dict_friends[friend_name] = 0 # Add the friend's name to the list
    print(dict_friends)
