import random

dict_friends = dict()

def bill_split(value, num_people):
    bill = value / num_people
    return round(bill, 2)

def lucky(new_dict):
    return random.choice(list(new_dict.keys()))

def who_is_lucky():
    print("""Do you want to use the "Who is lucky?" feature? Write Yes/No: """)
    lucky_input = input()
    if lucky_input.lower() == "yes":
        #do some code
        name_list = lucky(dict_friends)
        print(f"{name_list} is the lucky one!")
    else:
        print("No one is going to be lucky") 

# Get the number of friends joining with exception handling
try:
    num_friends = int(input("Enter the number of friends joining (including you): "))
    if num_friends <= 0:
        print("No one is joining for the party")        
    else:
        print(f"{num_friends} people are joining the party!")
        for i in range(num_friends):
            friend_name = input("Enter friend's name: ")
            dict_friends[friend_name] = 0 # Add the friend's name to the dictionary
            
        # Get the total bill with exception handling
        try:
            total_bill = int(input("Enter the total bill value: "))
            if total_bill <= 0:
                print("Please enter a bill value greater than 0.")  
            else:
                who_is_lucky()
                # Split the total bill among friends
                # for friend in dict_friends:
                #     dict_friends[friend] = bill_split(total_bill, num_friends)
                # print(dict_friends)
        except ValueError:
            print("Please enter a valid number for the total bill.")
except ValueError:
    print("Please enter a valid number.")

