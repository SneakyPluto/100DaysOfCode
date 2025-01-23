largest = None
smallest = None
numbers = []

while True:
    user_num = input("Enter a number: ")
    if user_num.lower() == "done":
        break
    try:
            numbers.append(float(user_num))
            for num_large in numbers:
                if largest == None : 
                    largest = num_large
                elif num_large > largest:
                    largest = num_large

            for num_small in numbers:
                if smallest == None:
                    smallest = num_small
                elif num_small < smallest:
                    smallest = num_small
    except:
        print("Invalid input")
print("Maximum is", round(largest))
print("Minimum is", round(smallest))
