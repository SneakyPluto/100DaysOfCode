def bill_split(value, num_people):
    return value / num_people

dict_friends = dict()
num_friends = int(input("Enter the number of friends joining (including you): "))
if not num_friends.is_integer() or num_friends <= 0:
        print("No one is joining for the party")
else:
    print(f"{num_friends} people are joining the party!")
    for i in range(num_friends):
        friend_name = input("Enter friend's name: ")
        dict_friends[friend_name] = 0 # Add the friend's name to the list
    total_bill = int(input("Enter the total bill value: "))
    # Some basic user input handling for a bill
    if not total_bill.is_integer() or total_bill <= 0:
         print("Please enter a bill value > 0 or a valid integer")
    for j in range(num_friends):
         dict_friends[j] = bill_split(total_bill, num_friends)
    print(dict_friends)
