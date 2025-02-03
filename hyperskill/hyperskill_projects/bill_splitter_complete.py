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
        lucky_one = lucky(dict_friends)
        print(f"{lucky_one} is the lucky one!\n")
        
        #Split the total bill among friends
        for friend in dict_friends:
            dict_friends[friend] = round(bill_split(total_bill, (num_friends-1)), 2)
            # Set the lucky one to a value of 0
            dict_friends[lucky_one] = 0
        print(dict_friends)
    else:
        print("No one is going to be lucky \n") 
        for friend in dict_friends:
            dict_friends[friend] = round(bill_split(total_bill, (num_friends)), 2)
        print(dict_friends)

# Get the number of friends joining with exception handling
try:
    num_friends = int(input("Enter the number of friends joining (including you): "))
    if num_friends <= 0:
        print("No one is joining for the party")        
    else:
        # print(f"{num_friends} people are joining the party!")
        print("Enter the name of every friend (including you), each on a new line: ")
        for i in range(num_friends):
            friend_name = input("> ")
            dict_friends[friend_name] = 0 # Add the friend's name to the dictionary
            
        # Get the total bill with exception handling
        try:
            total_bill = int(input("Enter the total bill value: "))
            if total_bill <= 0:
                print("Please enter a bill value greater than 0.")  
            else:
                who_is_lucky()
        except ValueError:
            print("Please enter a valid number for the total bill.")
except ValueError:
    print("Please enter a valid number.")

