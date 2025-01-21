try:
    user_range = float(input("Enter a number between 0.0 and 1.0 "))
    if user_range < 0 or user_range > 1:
        print("Please enter a float between 0.0 and 1.0 ")
    else:
        if user_range >= 0.9:
            print("A")
        elif user_range >= 0.8:
            print("B")
        elif user_range >= 0.7:
            print("C")
        elif user_range >= 0.6:
            print("D")
        elif user_range < 0.6:
            print("F")
except ValueError:
    print("Please enter a float between 0.0 and 1.0 ")
